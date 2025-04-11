from flask import Blueprint, jsonify, request
from Services.libro_service import LibroService

# Crear el Blueprint
libro_bp = Blueprint('libro', __name__, url_prefix='/libros')

# Instancia del servicio
libro_service = LibroService()

@libro_bp.route('/', methods=['GET'])
def listar_libros():
    """Lista todos los libros."""
    libros = libro_service.obtener_todos()
    return jsonify([libro.to_dict() for libro in libros]), 200

@libro_bp.route('/', methods=['POST'])
def crear_libro():
    """Crea un nuevo libro."""
    data = request.get_json()
    libro = libro_service.crear(data)
    return jsonify(libro.to_dict()), 201

@libro_bp.route('/<int:libro_id>', methods=['GET'])
def obtener_libro(libro_id):
    """Obtiene un libro por su ID."""
    libro = libro_service.obtener_por_id(libro_id)
    if libro:
        return jsonify(libro.to_dict()), 200
    return jsonify({'mensaje': 'Libro no encontrado'}), 404

@libro_bp.route('/<int:libro_id>', methods=['PUT'])
def actualizar_libro(libro_id):
    """Actualiza un libro existente."""
    data = request.get_json()
    resultado = libro_service.actualizar(libro_id, data)
    if resultado:
        return jsonify({'mensaje': 'Libro actualizado'}), 200
    return jsonify({'mensaje': 'Libro no encontrado'}), 404

@libro_bp.route('/<int:libro_id>', methods=['DELETE'])
def eliminar_libro(libro_id):
    """Elimina un libro existente."""
    resultado = libro_service.eliminar(libro_id)
    if resultado:
        return jsonify({'mensaje': 'Libro eliminado'}), 200
    return jsonify({'mensaje': 'Libro no encontrado'}), 404
