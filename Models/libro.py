from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .database import Base

class Libro(Base):
    __tablename__ = "libro"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False, unique=True)
    descripcion = Column(String(255), nullable=False)
    autor = Column(String(100), nullable=False)
    genero = Column(String(50), nullable=False)
    publicacion = Column(Date, nullable=False)
    portada = Column(String(255), nullable=False)
    stock = Column(Integer, nullable=False)

    # Relación con Reserva
    reservas = relationship("Reserva", back_populates="libro")

    def to_dict(self):
        """Convierte el objeto Libro a un diccionario serializable."""
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'autor': self.autor,
            'genero': self.genero,
            'publicacion': str(self.publicacion),
            'portada': self.portada,
            'stock': self.stock,
        }
