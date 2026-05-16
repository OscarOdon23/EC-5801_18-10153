# Creamos la clase Matriz

class Matriz:

    def __init__(self, M: int, N: int, data: list):
        
        self.M: int = M                            # Guardar numero de filas
        self.N: int = N                            # Guardar numero de columnas
        self.data: list = data                     # Guardar datos de la matriz


    # SUMA DE MATRICES

    def __add__(self, other: "Matriz"):

        result: list = []                         

        for i in range(self.M):

            fila: list = []

            for j in range(self.N):
                value: float = self.data[i][j] + other.data[i][j]
                fila.append(value)
            result.append(fila)

        return Matriz(self.M, self.N, result)

    # RESTA DE MATRICES

    def __sub__(self, other: "Matriz"):

        result: list = []

        for i in range(self.M):
            
            fila: list = []

            for j in range(self.N):
                value: float = self.data[i][j] - other.data[i][j]
                fila.append(value)
            result.append(fila)

        return Matriz(self.M, self.N, result)



    # MULTIPLICACION

    def __mul__(self, other: "Matriz"):
        result: list = []

        for i in range(self.M):

            row: list = []

            for j in range(other.N):

                total: float = 0

                for k in range(self.N):
                    total += self.data[i][k] * other.data[k][j]
                row.append(total)

            result.append(row)

        return Matriz(self.M, other.N, result)


    # DIVISION DE MATRICES NO PERMITIDA

    def __truediv__(self, other: "Matriz"):

        raise Exception("Divison de Matrices No Permitida")

    # IMPRIMIR MATRIZ

    def print_matriz(self):

        for row in self.data:
            print(row)

# PRUEBAS

# Primera matriz_a de 4x4
matriz_a = Matriz(4, 4,
                  [
        [7, 2, 4, 12],
        [15, 5, 4, 3],
        [2, 1, 8, 7],
        [4, 5, 9, 19]
        ]
)

# Segunda matriz_b de 4x4
matriz_b = Matriz(4, 4,
                  [
        [16, 15, 14, 13],
        [12, 11, 10, 9],
        [8, 7, 6, 5],
        [4, 3, 2, 1]
        ]
)

# SUMA DE MATRICES

print("SUMA")

(matriz_a + matriz_b).print_matriz()

print()

# RESTA

print("RESTA")

(matriz_a - matriz_b).print_matriz()

print()

# MULTIPLICACION DE MATRICES

print("MULTIPLICACION")

(matriz_a * matriz_b).print_matriz()

# DIVISION DE MATRICES
print("DIVISION")

try:
    (matriz_a / matriz_b).print_matriz()

except Exception as e:
    print("Error:", e)
    