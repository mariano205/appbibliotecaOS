from flask import Blueprint, jsonify, request
from Services.reserva_service import ReservaService

# Crear el Blueprint
reserva_bp = Blueprint('reserva', __name__, url_prefix='/reservas')

# Instancia del servicio
reserva_service = ReservaService()

@reserva_bp.route('/', methods=['GET'])
def listar_reservas():
    """Lista todas las reservas."""
    reservas = reserva_service.obtener_todos()
    return jsonify([reserva.to_dict() for reserva in reservas]), 200

@reserva_bp.route('/', methods=['POST'])
def crear_reserva():
    """Crea una nueva reserva."""
    data = request.get_json()
    try:
        reserva = reserva_service.crear(data)
        return jsonify(reserva.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@reserva_bp.route('/<int:reserva_id>', methods=['GET'])
def obtener_reserva(reserva_id):
    """Obtiene una reserva por su ID."""
    reserva = reserva_service.obtener_por_id(reserva_id)
    if reserva:
        return jsonify(reserva.to_dict()), 200
    return jsonify({'mensaje': 'Reserva no encontrada'}), 404

@reserva_bp.route('/<int:reserva_id>', methods=['PUT'])
def actualizar_reserva(reserva_id):
    """Actualiza una reserva existente."""
    data = request.get_json()
    resultado = reserva_service.actualizar(reserva_id, data)
    if resultado:
        return jsonify({'mensaje': 'Reserva actualizada'}), 200
    return jsonify({'mensaje': 'Reserva no encontrada'}), 404

@reserva_bp.route('/<int:reserva_id>', methods=['DELETE'])
def eliminar_reserva(reserva_id):
    """Elimina una reserva existente."""
    resultado = reserva_service.eliminar(reserva_id)
    if resultado:
        return jsonify({'mensaje': 'Reserva eliminada'}), 200
    return jsonify({'mensaje': 'Reserva no encontrada'}), 404

@reserva_bp.route('/usuario/<int:usuario_id>', methods=['GET'])
def listar_reservas_por_usuario(usuario_id):
    """Lista todas las reservas de un usuario específico."""
    reservas = reserva_service.obtener_por_usuario(usuario_id)
    return jsonify([reserva.to_dict() for reserva in reservas]), 200
