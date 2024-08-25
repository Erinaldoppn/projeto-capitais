from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
     return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/cadastro')
def cadastro():
	return render_template('cadastro.html')

@app.route('/cadastrarcapital')
def cadastrarcapital():
	return render_template('cadastrarcapital.html')

@app.route('/exibircapital')
def exibircapital():
	return render_template('exibircapital.html')

