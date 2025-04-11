from Repositories.libro_repository import LibroRepository

class LibroService:
    def __init__(self):
        self.repository = LibroRepository()

    def crear(self, libro_data):
        return self.repository.crear(libro_data)

    def obtener_todos(self):
        return self.repository.obtener_todos()

    def obtener_por_id(self, libro_id):
        return self.repository.obtener_por_id(libro_id)

    def actualizar(self, libro_id, libro_data):
        return self.repository.actualizar(libro_id, libro_data)

    def eliminar(self, libro_id):
        return self.repository.eliminar(libro_id)
