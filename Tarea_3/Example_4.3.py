import time
from threading_event import ThreadManager

# Función que se ejecuta en cada hilo
# Usa stop_event para poder detenerse de forma controlada
def tarea(stop_event, nombre):

    contador = 0

    # Mientras no se active la señal de stop, sigue ejecutando
    while not stop_event.is_set():
        print(f"{nombre}: {contador}")
        contador += 1
        time.sleep(1)

    # Mensaje cuando el hilo termina correctamente
    print(f"{nombre} Tarea END:)")

# Callback que se ejecuta al iniciar el hilo
def inicio(nombre):
    print(f"[CALLBACK START] {nombre}")

# Callback que se ejecuta al finalizar el hilo
def fin(nombre):
    print(f"[CALLBACK END] {nombre}")

# Se crea el gestor de hilos con un Backlog de 2
manager = ThreadManager(backlog=2)

# Registro de hilos con su función y parámetros
manager.Thread_Allocate("hilo1", tarea, "hilo1")
manager.Thread_Allocate("hilo2", tarea, "hilo2")

# Registro de callbacks para Hilo 1
manager.Thread_Callback_Register("hilo1", inicio, fin)

# Ejecucion de los hilos registrados
manager.Thread_Start("hilo1")
manager.Thread_Start("hilo2")

time.sleep(5)

# Se envía señal de STOP a los hilos
manager.Thread_End("hilo1")
manager.Thread_End("hilo2")

# Espera a que todos los hilos terminen
manager.Join_All()

print("Todos los hilos finalizaron :D")