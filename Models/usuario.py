from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    apellidos = Column(String(100), nullable=False)
    usuario = Column(String(50), unique=True, nullable=False)
    contra = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    movil = Column(String(15), nullable=False)

    # Relación con Reserva
    reservas = relationship("Reserva", back_populates="usuario")

    def to_dict(self):
        """Convierte el objeto Usuario a un diccionario serializable."""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellidos': self.apellidos,
            'usuario': self.usuario,
            'contra': self.contra,
            'correo': self.correo,
            'movil': self.movil,
        }
