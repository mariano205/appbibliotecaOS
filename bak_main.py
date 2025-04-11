from flask import Flask
from Controllers import usuario_controller, libro_controller, reserva_controller

app = Flask(__name__)

app.register_blueprint(usuario_controller.usuario_bp)
app.register_blueprint(libro_controller.libro_bp)
app.register_blueprint(reserva_controller.reserva_bp)


@app.route("/")
def home():
    return "¡Prueba API REST!"


if __name__ == '__main__':
    app.run(debug=True)
