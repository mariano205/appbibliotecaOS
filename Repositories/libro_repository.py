from Models.database import SessionLocal
from Models.libro import Libro

class LibroRepository:
    def crear(self, libro_data):
        """
        Crea un nuevo libro en la base de datos.
        """
        db = SessionLocal()
        nuevo_libro = Libro(**libro_data)
        db.add(nuevo_libro)
        db.commit()
        db.refresh(nuevo_libro)  # Refresca el objeto para obtener el ID generado
        db.close()
        return nuevo_libro

    def obtener_todos(self):
        """
        Obtiene todos los libros de la base de datos.
        """
        db = SessionLocal()
        libros = db.query(Libro).all()
        db.close()
        return libros

    def obtener_por_id(self, libro_id):
        """
        Obtiene un libro por su ID.
        """
        db = SessionLocal()
        libro = db.query(Libro).filter(Libro.id == libro_id).first()
        db.close()
        return libro

    def actualizar(self, libro_id, libro_data):
        """
        Actualiza un libro existente.
        """
        db = SessionLocal()
        libro = db.query(Libro).filter(Libro.id == libro_id).first()
        if libro:
            for key, value in libro_data.items():
                setattr(libro, key, value)  # Actualiza los atributos del objeto
            db.commit()
            db.refresh(libro)  # Refresca para obtener los datos actualizados
        db.close()
        return libro

    def eliminar(self, libro_id):
        """
        Elimina un libro por su ID.
        """
        db = SessionLocal()
        libro = db.query(Libro).filter(Libro.id == libro_id).first()
        if libro:
            db.delete(libro)
            db.commit()
        db.close()
        return libro
