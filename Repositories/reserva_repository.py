from Models.database import SessionLocal
from Models.reserva import Reserva
from Models.libro import Libro

class ReservaRepository:
    def crear(self, reserva_data):
        """
        Crea una nueva reserva si el libro tiene stock disponible.
        """
        db = SessionLocal()
        libro = db.query(Libro).filter(Libro.id == reserva_data['libro_id']).first()
        if libro and libro.stock > 0:
            libro.stock -= 1  # Reducir el stock del libro
            db.add(libro)
            nueva_reserva = Reserva(**reserva_data)
            db.add(nueva_reserva)
            db.commit()
            db.refresh(nueva_reserva)  # Refresca para obtener datos actualizados
            db.close()
            return nueva_reserva
        db.close()
        raise ValueError("El libro no tiene stock disponible.")

    def obtener_todos(self):
        """
        Obtiene todas las reservas.
        """
        db = SessionLocal()
        reservas = db.query(Reserva).all()
        db.close()
        return reservas

    def obtener_por_id(self, reserva_id):
        """
        Obtiene una reserva por su ID.
        """
        db = SessionLocal()
        reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
        db.close()
        return reserva

    def actualizar(self, reserva_id, reserva_data):
        """
        Actualiza una reserva existente.
        """
        db = SessionLocal()
        reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
        if reserva:
            for key, value in reserva_data.items():
                setattr(reserva, key, value)  # Actualiza los atributos del objeto
            db.commit()
            db.refresh(reserva)  # Refresca para obtener los datos actualizados
        db.close()
        return reserva

    def eliminar(self, reserva_id):
        """
        Elimina una reserva y actualiza el stock del libro.
        """
        db = SessionLocal()
        reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
        if reserva:
            libro = reserva.libro
            libro.stock += 1  # Incrementar el stock al eliminar la reserva
            db.add(libro)
            db.delete(reserva)
            db.commit()
            db.close()
            return reserva
        db.close()
        return None

    def obtener_por_usuario(self, usuario_id):
        """
        Obtiene las reservas de un usuario por su ID.
        """
        db = SessionLocal()
        reservas = db.query(Reserva).filter(Reserva.usuario_id == usuario_id).all()
        db.close()
        return reservas
