from flask import Blueprint, jsonify, request
from Services.usuario_service import UsuarioService

# Crear el blueprint para las rutas del controlador
usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuarios')

# Instancia del servicio
usuario_service = UsuarioService()

@usuario_bp.route('/', methods=['GET'])
def listar_usuarios():
    """Lista todos los usuarios."""
    usuarios = usuario_service.obtener_todos()
    return jsonify([usuario.to_dict() for usuario in usuarios]), 200

@usuario_bp.route('/', methods=['POST'])
def crear_usuario():
    """Crea un nuevo usuario."""
    data = request.get_json()
    usuario = usuario_service.crear(data)
    return jsonify(usuario.to_dict()), 201

@usuario_bp.route('/<int:usuario_id>', methods=['GET'])
def obtener_usuario(usuario_id):
    """Obtiene un usuario por su ID."""
    usuario = usuario_service.obtener_por_id(usuario_id)
    if usuario:
        return jsonify(usuario.to_dict()), 200
    return jsonify({'mensaje': 'Usuario no encontrado'}), 404

@usuario_bp.route('/<int:usuario_id>', methods=['PUT'])
def actualizar_usuario(usuario_id):
    """Actualiza un usuario existente."""
    data = request.get_json()
    resultado = usuario_service.actualizar(usuario_id, data)
    if resultado:
        return jsonify({'mensaje': 'Usuario actualizado'}), 200
    return jsonify({'mensaje': 'Usuario no encontrado'}), 404

@usuario_bp.route('/<int:usuario_id>', methods=['DELETE'])
def eliminar_usuario(usuario_id):
    """Elimina un usuario existente."""
    resultado = usuario_service.eliminar(usuario_id)
    if resultado:
        return jsonify({'mensaje': 'Usuario eliminado'}), 200
    return jsonify({'mensaje': 'Usuario no encontrado'}), 404