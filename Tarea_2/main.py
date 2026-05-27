from yaml_manager import YAMLManager            # Importa la clase YAMLManager (Clase Hija de FileManager)


def main():

    manager = YAMLManager()                     # Crea el objeto

    # Cargamos el YAML

    manager.load_yaml("personas", "personas.yaml")

    # Obtiene el documento
    document = manager.get_document("personas")

    print("\nDocumento original:\n")
    print(document)

    # Modificamos el documento
    document["data"][0]["nombre"] = "Oscar"
    document["data"][0]["altura"] = 1.74
    document["data"][0]["peso"] = 70.0
    document["data"][0]["edad"] = 25
    document["data"][0]["habilidades"][0] = "tocar guitarra"
    document["data"][0]["habilidades"][1] = "entender circuitos"
    document["data"][0]["habilidades"][2] = "conocimientos de matematicas"
    document["data"][0]["descripcion"] = "Estudiante de Electronica"

    # Actualiza el documento interno
    manager.update_document("personas", document["data"])

    # Guardamos cambios

    manager.save_document("personas")

    print("\nCambios guardados.\n")
    print(document)

if __name__ == "__main__":
    main()