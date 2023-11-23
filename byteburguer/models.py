from byteburguer import database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    cpf = database.Column(database.String, nullable=False, unique=True)
    telefone = database.Column(database.String, nullable=False, unique=True)
    cep = database.Column(database.String, nullable=False)
    estado = database.Column(database.String, nullable=False)
    cidade = database.Column(database.String, nullable=False)
    endereco = database.Column(database.String, nullable=False)
    bairro = database.Column(database.String, nullable=False)
    complemento = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    pedidos = database.relationship('Pedido', backref='criador', lazy=True)

class Pedido(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)