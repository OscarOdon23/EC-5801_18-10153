import logging

# Configuración del módulo logging para mostrar todos los niveles: DEBUG, INFO, WARNING y ERROR.
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")

# Nivel DEBUG
logging.debug("DEBUG: Información para debug >:c")

# Nivel INFO
logging.info("INFO: Operacion Exitosa:D")

# Nivel WARNING
logging.warning("WARNING: Ojo pelao, algo no esta muy bien")

# Nivel ERROR:
logging.error("ERROR: ocurrió un error durante la ejecución x_X")