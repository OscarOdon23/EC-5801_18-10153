import threading
from typing import Callable, Any, Dict, Optional


class ThreadManager:
    # Clase que implementa un gestor de hilos con Backlog, Callbacks y sincronización con Event

    def __init__(self, backlog: int):
        # Backlog: número máximo de hilos que pueden ejecutarse al mismo tiempo

        self.backlog = backlog

        # Semáforo que limita la cantidad de hilos en ejecución simultánea
        self.semaphore = threading.Semaphore(backlog)

        # Diccionario donde se almacenan los hilos registrados
        self.threads: Dict[str, Dict[str, Any]] = {}

    def Thread_Allocate(self, name: str, target: Callable, *args, **kwargs):

        # Detenemos el hilo
        stop_event = threading.Event()

        self.threads[name] = {
            "target": target,            # Ejecutor del hilo
            "args": args,  
            "kwargs": kwargs,
            "stop_event": stop_event,    # Event para control de detención del hilo
            "callback_start": None,      # Callback al iniciar el hilo
            "callback_end": None,        # Callback al finalizar el hilo
            "thread": None
        }

    def Thread_Callback_Register(self, name: str, callback_start=None, callback_end=None):
        # Registra callbacks para el inicio y fin de un hilo
        if name not in self.threads:
            raise ValueError(f"Hilo '{name}' no registrado")
        
        # Guarda el callback ejecutado al iniciar el hilo
        self.threads[name]["callback_start"] = callback_start

        # Guarda el callback ejecutado al finalizar el hilo
        self.threads[name]["callback_end"] = callback_end

    def _thread_wrapper(self, name):

        with self.semaphore:

            # Obtiene los datos del hilo registrado
            data = self.threads[name]

            # Ejecuta callback de inicio (si existe)
            if data["callback_start"]:
                data["callback_start"](name)

            # Se envía stop_event para permitir finalización controlada
            data["target"](data["stop_event"], *data["args"], **data["kwargs"])

            # Ejecuta callback de finalización (si existe)
            if data["callback_end"]:
                data["callback_end"](name)

    def Thread_Start(self, name):
        # Verifica que el hilo esté registrado antes de iniciarlo
        if name not in self.threads:
            raise ValueError(f"Hilo '{name}' no registrado")
                
        thread = threading.Thread(target=self._thread_wrapper, args=(name,), name=name)

        self.threads[name]["thread"] = thread

        # Inicia la ejecución del hilo
        thread.start()

    def Thread_End(self, name):
        # Señala la finalización del hilo con Event

        if name not in self.threads:
            raise ValueError("Hilo no encontrado")

        # Activa el Event: el hilo debe terminar
        self.threads[name]["stop_event"].set()

    def Join_All(self):

        # Espera a que los hilos terminen antes de continuar
        for data in self.threads.values():

            if data["thread"] is not None:
                data["thread"].join()