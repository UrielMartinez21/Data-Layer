from logger_base import log
import psycopg2 as db
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        """
        Establece la conexión con la base de datos
        return: psycopg2.connection
        """

        if cls._conexion == None or cls._conexion.closed:
            try:
                cls._conexion = db.connect(
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f"Conexión exitosa: {cls._conexion}")
                return cls._conexion
            except Exception as e:
                log.error(f"Error al conectar a la BD: {e}")
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        """
        Obtiene el cursor de la conexión
        return: psycopg2.cursor
        """

        if cls._cursor == None or cls._cursor.closed:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f"Se abrió el cursor exitosamente: {cls._cursor}")
                return cls._cursor
            except Exception as e:
                log.error(f"Error al obtener el cursor: {e}")
                sys.exit()
        else:
            return cls._cursor


if __name__ == "__main__":
    # Obtener conexión
    Conexion.obtenerConexion()

    # Obtener cursor
    Conexion.obtenerCursor()