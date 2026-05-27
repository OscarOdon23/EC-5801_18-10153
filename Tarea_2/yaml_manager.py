# Usamos la libreria PyYAML

import yaml

from file_manager import FileManager                # Importamos la clase padre
from schema_validator import schema_validator       # Importamos el decorador


# Schema a validar

PERSON_SCHEMA = {
    "nombre": str,
    "altura": float,
    "peso": float,
    "edad": int,
    "habilidades": [str],
    "descripcion": str
}


# Aplicamos el decorador para validar los datos de la persona

@schema_validator(PERSON_SCHEMA)

def validate_person(data):                      # La funcion retorna los datos y el decorador valida
    return data


# CLASE YAML (Clase Hija de FileManager que hereda sus métodos)

class YAMLManager(FileManager):

    def __init__(self):

        self.__documents = {}           # Diccionario privado interno para guardar el diccionario obtenido


    # Cargamos el yaml: leemos el archivo

    def load_yaml(self, name: str, path: str):

        stream = self.read_file(path)               # Lee el archivo

        data = yaml.safe_load(stream)               # Convierte el Yaml en un diccionario de Python

        # VALIDACIÓN
        if isinstance(data, list):                  # Si el YAML es una lista de personas, validamos cada una

            for item in data:

                if validate_person(item) is None:

                    raise ValueError(
                        "Datos inválidos en YAML"
                    )

        else:

            if validate_person(data) is None:

                raise ValueError(
                    "Datos inválidos en YAML"
                )

        self.__documents[name] = {                          # Guarda el documento
            "path": path,
            "data": data                                    # Guarda el diccionario obtenido del YAML
        }

    # GETTER
    
    def get_document(self, name: str):                      # Verifica existencia del documento

        if name not in self.__documents:

            raise KeyError(
                f"No existe el documento: {name}"
            )

        return self.__documents[name]

    # UPDATE: Método adicional que permite modificar un diccionario

    def update_document(
        self,
        name: str,
        new_data
    ):

        if name not in self.__documents:

            raise KeyError(
                f"No existe el documento: {name}"
            )

        # VALIDACIÓN
        if isinstance(new_data, list):

            for item in new_data:

                # SIN self.
                if validate_person(item) is None:

                    raise ValueError(
                        "Datos inválidos"
                    )

        else:

            if validate_person(new_data) is None:

                raise ValueError(
                    "Datos inválidos"
                )

        self.__documents[name]["data"] = new_data

    
    # SAVE: Guarda los valores modificados en el disco
    def save_document(self, name: str):

        if name not in self.__documents:

            raise KeyError(
                f"No existe el documento: {name}"
            )

        path = self.__documents[name]["path"]

        data = self.__documents[name]["data"]

        yaml_stream = yaml.dump(
            data,
            allow_unicode=True,
            sort_keys=False
        )

        self.write_file(path, yaml_stream)