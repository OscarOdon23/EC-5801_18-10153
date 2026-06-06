import logging
import threading
from typing import Callable, Any, Dict, Optional

# Configuración básica de logging para ver la ejecución de los hilos
logging.basicConfig(level=logging.INFO, format="%(threadName)s - %(message)s")


class ThreadManager:
    # Clase que implementa un gestor de hilos con Backlog y callbacks

    def __init__(self, backlog: int):

        self.backlog = backlog

        # Semáforo: limita la cantidad de hilos en ejecución simultánea
        self.semaphore = threading.Semaphore(backlog)

        # Diccionario donde se almacenan los hilos registrados
        self.threads: Dict[str, Dict[str, Any]] = {}

    def Thread_Allocate(self, name: str, target: Callable, *args, **kwargs):

        self.threads[name] = {
            "target": target,             # Ejecutor del hilo
            "args": args,                
            "kwargs": kwargs,             
            "callback_start": None,       # Callback ejecutado al iniciar el hilo
            "callback_end": None,         # Callback ejecutado al finalizar el hilo
            "thread": None               
        }

    def Thread_Callback_Register(self, name: str, callback_start: Optional[Callable] = None, callback_end: Optional[Callable] = None):
        
        # Registra callbacks para el inicio y fin de un hilo
        if name not in self.threads:
            raise ValueError(f"Hilo '{name}' no registrado")

        # Guarda el callback ejecutado al iniciar el hilo
        self.threads[name]["callback_start"] = callback_start

        # Guarda el callback ejecutado al finalizar el hilo
        self.threads[name]["callback_end"] = callback_end

    def _thread_wrapper(self, name: str):

        with self.semaphore:

            # Obtiene los datos del hilo registrado
            data = self.threads[name]

            # Ejecuta callback de inicio (si existe)
            if data["callback_start"]:
                data["callback_start"](name)

            # Ejecuta la función principal del hilo
            data["target"](*data["args"], **data["kwargs"])

            # Ejecuta callback de finalización (si existe)
            if data["callback_end"]:
                data["callback_end"](name)

    def Thread_Start(self, name: str):
        # Verifica que el hilo esté registrado antes de iniciarlo
        if name not in self.threads:
            raise ValueError(f"Hilo '{name}' no registrado")

        thread = threading.Thread(target=self._thread_wrapper, args=(name,), name=name)

        self.threads[name]["thread"] = thread

        # Inicia la ejecución del hilo
        thread.start()