from conexion import Conexion
from persona import Persona
from logger_base import log

class PersonaDAO:
    """
    DAO (Data Access Object)
    Va a contener todos los métodos CRUD
    """
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        # --> Conexión
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)

                # --> Recuperar los registros
                registros = cursor.fetchall()
                personas = [Persona(registro[0], registro[1], registro[2], registro[3]) for registro in registros]

                return personas
    
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f"Persona insertada: {persona}")
                return cursor.rowcount
            
    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f"Persona actualizada: {persona}")
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f"Persona eliminada: {persona}")
                return cursor.rowcount


if __name__ == "__main__":
    # Insertar un registro
    # persona = Persona(nombre='Pedro', apellido='Alva', email='pedro@gmail.com')
    # personas_insertadas = PersonaDAO.insertar(persona)
    # log.debug(f"Personas insertadas: {personas_insertadas}")

    # Actualizar un registro
    # persona = Persona(id_persona=1, nombre='Uriel edit', apellido='Martinez edit', email='uriel@gmail.com')
    # personas_actualizadas = PersonaDAO.actualizar(persona)
    # log.debug(f"Personas actualizadas: {personas_actualizadas}")

    # Eliminar un registro
    persona = Persona(id_persona=14)
    personas_eliminadas = PersonaDAO.eliminar(persona)

    # Consultar registros
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        print(persona)