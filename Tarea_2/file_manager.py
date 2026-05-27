from pathlib import Path


class FileManager:

    def validate_path(self, path: str) -> Path:
        """
        Verifica que la ruta exista.
        """

        file_path = Path(path)

        if not file_path.exists():
            raise FileNotFoundError(
                f"La ruta no existe: {path}"
            )

        return file_path

    def read_file(self, path: str, binary: bool = False):
        """
        Lee archivos de texto o binarios.
        """

        file_path = self.validate_path(path)

        mode = "rb" if binary else "r"

        with open(
            file_path,
            mode,
            encoding=None if binary else "utf-8"
        ) as file:

            return file.read()

    def write_file(
        self,
        path: str,
        data,
        binary: bool = False
    ):
        """
        Escribe archivos de texto o binarios.
        """

        file_path = Path(path)

        mode = "wb" if binary else "w"

        with open(
            file_path,
            mode,
            encoding=None if binary else "utf-8"
        ) as file:

            file.write(data)