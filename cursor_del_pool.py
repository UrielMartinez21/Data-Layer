from conexion import Conexion
from logger_base import log

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug("Inicio de with método __enter__")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug("Se ejecuta método __exit__")
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f"Ocurrió una excepción: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}")
        else:
            self._conexion.commit()
            log.debug("Commit de la transacción")
        # Cerramos el cursor
        self._cursor.close()
        # Regresamos la conexión al pool
        Conexion.liberarConexion(self._conexion)

if __name__ == "__main__":
    with CursorDelPool() as cursor:
        print("Dentro del bloque with".center(50, '-'))
        cursor.execute('SELECT * FROM persona')
        log.debug("Listado de personas")
        log.debug(cursor.fetchall())