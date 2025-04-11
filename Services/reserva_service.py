from Repositories.reserva_repository import ReservaRepository

class ReservaService:
    def __init__(self):
        self.repository = ReservaRepository()

    def crear(self, reserva_data):
        """Valida y crea una reserva."""
        return self.repository.crear(reserva_data)

    def obtener_todos(self):
        """Obtiene todas las reservas."""
        return self.repository.obtener_todos()

    def obtener_por_id(self, reserva_id):
        """Obtiene una reserva por su ID."""
        return self.repository.obtener_por_id(reserva_id)

    def actualizar(self, reserva_id, reserva_data):
        """Actualiza una reserva."""
        return self.repository.actualizar(reserva_id, reserva_data)

    def eliminar(self, reserva_id):
        """Elimina una reserva."""
        return self.repository.eliminar(reserva_id)

    def obtener_por_usuario(self, usuario_id):
        """Obtiene todas las reservas de un usuario."""
        return self.repository.obtener_por_usuario(usuario_id)



