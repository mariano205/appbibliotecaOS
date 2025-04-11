from Models.database import Base, engine

from Models.libro import Libro
from Models.reserva import Reserva
from Models.usuario import Usuario

def crear_tablas():
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Migración completada.")

if __name__ == "__main__":
    crear_tablas()
