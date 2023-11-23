from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from byteburguer.models import Usuario

class FormCriarConta(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired(), Length(11)])
    telefone = StringField('Telefone', validators=[DataRequired(), Length(11)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
    cep = StringField('CEP', id='inputCep', validators=[DataRequired(), Length(5, 8)])
    estado = StringField('Estado', id='inputEstado', validators=[DataRequired()])
    cidade = StringField('Cidade', id='inputCidade', validators=[DataRequired()])
    endereco = StringField('Endereço', id='inputEndereco', validators=[DataRequired()])
    bairro = StringField('Bairro', id='inputBairro', validators=[DataRequired()])
    complemento = StringField('Complemento', id='inputComplemento', validators=[DataRequired()])
    botao_submit_criarconta = SubmitField('Criar Conta')
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    botao_submit_login = SubmitField('Fazer Login')
