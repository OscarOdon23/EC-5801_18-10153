# HDD (MEMORIA MÁS LENTA)

class HDD:

    def __init__(self, N: int):

        self.memoria: list = [0] * N                       # Memoria del HDD

        self.retraso: int = 1000000                        # Retraso de acceso lento


    # LECTURA
    def leer(self, pos: int):

        print("HDD Leyendo...")
        for i in range(self.retraso):                      # Simulación de retraso de lectura

            pass

        return self.memoria[pos]

    # ESCRITURA
    def escribir(self, pos: int, data: int):

        print("HDD Escribiendo...")
        for i in range(self.retraso):
            pass

        self.memoria[pos] = data


# MEMORIA RAM (INTERMEDIA)

class RAM:

    def __init__(self, N: int):

        self.memoria: list = [0] * N                        # Memoria de la RAM

        self.retraso: int = 500000                          # Retraso intermedio


    def leer(self, pos: int):

        print("RAM Leyendo...")

        for i in range(self.retraso):
            pass

        return self.memoria[pos]

    def escribir(self, pos: int, data: int):

        print("RAM Escribiendo...")

        for i in range(self.retraso):
            pass

        self.memoria[pos] = data


# MEMORIA SRAM (RÁPIDA)

class SRAM:

    def __init__(self, N: int):

        self.memoria: list = [0] * N                    # Memoria de la SRAM

        self.retraso: int = 1000                        # Retraso mínimo


    def leer(self, pos: int):

        print("SRAM Leyendo...")

        for i in range(self.retraso):
            pass

        return self.memoria[pos]

    def escribir(self, pos: int, data: int):

        print("SRAM Escribiendo...")

        for i in range(self.retraso):
            pass

        self.memoria[pos] = data


# FUNCIONES POLIMÓRFICAS

# Función que realiza la LECTURA desde el dispositivo de memoria
def leer_memoria(dispositivo, pos: int):
    return dispositivo.leer(pos)


# Función que realiza la ESCRITURA en el dispositivo de memoria
def escribir_memoria(dispositivo, pos: int, data: int):
    dispositivo.escribir(pos, data)


# PRUEBA

hdd = HDD(5)
ram = RAM(5)
sram = SRAM(5)

# Escritura en diferentes tipos de memoria
escribir_memoria(hdd, 0, 100)
escribir_memoria(ram, 0, 200)
escribir_memoria(sram, 0, 300)

print()

# Lectura desde el dispositivo de memoria
print("HDD:", leer_memoria(hdd, 0))
print("RAM:", leer_memoria(ram, 0))
print("SRAM:", leer_memoria(sram, 0))