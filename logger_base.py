import logging as log

# --> Configuración básica para el registro de mensajes
log.basicConfig(
    level=log.DEBUG,                                                            # Nivel de los mensajes que se van a mostrar
    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',  # Formato de los mensajes
    datefmt='%I:%M:%S %p',                                                      # Formato de la fecha y la hora
    handlers=[                                                                  # Manejadores de los mensajes
        log.FileHandler('capa_datos.log'),                                      # Archivo donde se almacenan los mensajes
        log.StreamHandler()                                                     # Consola donde se muestran los mensajes
    ]
)


if __name__ == "__main__":
    print("Mensaje a nivel de consola".center(50, '-'))
    log.debug("Mensaje a nivel debug")
    log.info("Mensaje a nivel info")
    log.warning("Mensaje a nivel warning")
    log.error("Mensaje a nivel error")
    log.critical("Mensaje a nivel critical")