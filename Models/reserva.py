from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base

class Reserva(Base):
    __tablename__ = "reserva"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer,
                        ForeignKey("usuario.id", ondelete="CASCADE"),
                        nullable=False)
    libro_id = Column(Integer,
                      ForeignKey("libro.id", ondelete="CASCADE"),
                      nullable=False)
    estado = Column(String(50), nullable=False)
    reservado = Column(Date, nullable=False)
    devolucion = Column(Date, nullable=True)

    # Relaciones
    usuario = relationship("Usuario", back_populates="reservas")
    libro = relationship("Libro", back_populates="reservas")

    def to_dict(self):
        """Convierte el objeto Reserva a un diccionario serializable."""
        return {
            'id': self.id,
            'usuario_id': self.usuario_id,
            'libro_id': self.libro_id,
            'estado': self.estado,
            'reservado': str(self.reservado),
            'devolucion': str(self.devolucion) if self.devolucion else None,
        }
