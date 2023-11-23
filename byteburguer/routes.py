from flask import Flask, render_template, url_for, request, flash, redirect
from byteburguer import app, database, bcrypt
from byteburguer.forms import FormLogin, FormCriarConta
from byteburguer.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            return redirect('/')
        else:
            flash(f'Falha no Login. E-mail ou Senha Incorretos', 'alert-danger')
    return render_template('login.html', form_login=form_login)


@app.route('/cadastrocliente', methods=['GET', 'POST'])
def cadastrocliente():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(nome=form_criarconta.nome.data, email=form_criarconta.email.data, senha=senha_cript, cpf=form_criarconta.cpf.data, 
                          telefone=form_criarconta.telefone.data, cep=form_criarconta.cep.data, estado=form_criarconta.estado.data, 
                          cidade=form_criarconta.cidade.data, endereco=form_criarconta.endereco.data, bairro=form_criarconta.bairro.data, complemento=form_criarconta.complemento.data)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect('/')
    return render_template('cadastrocliente.html', form_criarconta=form_criarconta)


@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash(f'Logout Feito com Sucesso', 'alert-success')
    return redirect('/')


@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html')

@app.route('/pedido/criar')
@login_required
def criar_pedido():
    return render_template('criar_pedido.html')