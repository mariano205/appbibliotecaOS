from Models.database import SessionLocal
from Models.usuario import Usuario

class UsuarioRepository:
    def crear(self, usuario_data):
        """
        Crea un nuevo usuario en la base de datos.
        """
        db = SessionLocal()
        nuevo_usuario = Usuario(**usuario_data)
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)  # Actualiza el objeto con el ID generado
        db.close()
        return nuevo_usuario

    def obtener_todos(self):
        """
        Obtiene todos los usuarios de la base de datos.
        """
        db = SessionLocal()
        usuarios = db.query(Usuario).all()
        db.close()
        return usuarios

    def obtener_por_id(self, usuario_id):
        """
        Obtiene un usuario por su ID.
        """
        db = SessionLocal()
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        db.close()
        return usuario

    def actualizar(self, usuario_id, usuario_data):
        """
        Actualiza un usuario existente.
        """
        db = SessionLocal()
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if usuario:
            for key, value in usuario_data.items():
                setattr(usuario, key, value)  # Actualiza los atributos del objeto
            db.commit()
        db.close()
        return usuario

    def eliminar(self, usuario_id):
        """
        Elimina un usuario por su ID.
        """
        db = SessionLocal()
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if usuario:
            db.delete(usuario)
            db.commit()
        db.close()
        return usuario
