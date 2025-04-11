from Repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()

    def crear(self, usuario_data):
        """Valida y crea un usuario."""
        # Lógica adicional, por ejemplo, validar datos antes de crear
        return self.repository.crear(usuario_data)

    def obtener_todos(self):
        """Obtiene todos los usuarios."""
        return self.repository.obtener_todos()

    def obtener_por_id(self, usuario_id):
        """Obtiene un usuario por su ID."""
        return self.repository.obtener_por_id(usuario_id)

    def actualizar(self, usuario_id, usuario_data):
        """Actualiza un usuario."""
        return self.repository.actualizar(usuario_id, usuario_data)

    def eliminar(self, usuario_id):
        """Elimina un usuario."""
        return self.repository.eliminar(usuario_id)
