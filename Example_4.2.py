import time
from threading_manager import ThreadManager

# Simulacion de una tarea que demora en ejecutarse
def tarea(segundos):
    print(f"Tarea START ({segundos}s)")
    time.sleep(segundos)
    print("Tarea END")

# Callback ejecutado al iniciar un hilo
def inicio(nombre):
    print(f"[CALLBACK START] {nombre}")

# Callback ejecutado al finalizar un hilo
def fin(nombre):
    print(f"[CALLBACK END] {nombre}")

# Se crea el gestor de hilos con un Backlog de 2
manager = ThreadManager(backlog=2)

# Registro de hilos con su función y parámetros
manager.Thread_Allocate("Hilo1", tarea, 3)
manager.Thread_Allocate("Hilo2", tarea, 4)
manager.Thread_Allocate("Hilo3", tarea, 2)

# Registro de callbacks para Hilo1
manager.Thread_Callback_Register("Hilo1", callback_start=inicio, callback_end=fin)

# Ejecucion de los hilos registrados
manager.Thread_Start("Hilo1")
manager.Thread_Start("Hilo2")
manager.Thread_Start("Hilo3")