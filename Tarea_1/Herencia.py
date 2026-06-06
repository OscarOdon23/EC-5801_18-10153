# CREAMOS LA CLASE PADRE: PUNTO 3D

class Punto3D:

    def __init__(self, x: float, y: float, z: float):

        # Privados
        self.__x: float = x
        self.__y: float = y
        self.__z: float = z

    # GETTERS

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_z(self):
        return self.__z

    # SUMA DE UN ESCALAR EN LOS EJES

    def suma_escalar(self, escalar):
        self.__x = escalar + self.__x
        self.__y = escalar + self.__y
        self.__z = escalar + self.__z

    # MULTIPLICACION POR UN ESCALAR

    def multiplicacion_scalar(self, escalar):
        self.__x = escalar * self.__x
        self.__y = escalar * self.__y
        self.__z = escalar * self.__z


# CLASE HIJA: VECTOR

class Vector(Punto3D):

    # Magnitud del vector
    def magnitude(self):

        x: float = self.get_x()
        y: float = self.get_y()
        z: float = self.get_z()

        return (x**2 + y**2 + z**2) ** 0.5


# PRUEBA

print("HERENCIA - PUNTO Y VECTOR")

v = Vector(3, 4, 5)

print("x:", v.get_x())
print("y:", v.get_y())
print("z:", v.get_z())

v.suma_escalar(2)

print("\nDespues de suma escalar:")
print("x:", v.get_x())
print("y:", v.get_y())
print("z:", v.get_z())

v.multiplicacion_scalar(2)

print("\nDespues de multiplicacion:")
print("x:", v.get_x())
print("y:", v.get_y())
print("z:", v.get_z())

print("\nMagnitud del vector:")
print(v.magnitude())