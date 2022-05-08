from flask import Flask , render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Seja bem vindo! <br> navegue por /sobre, /contato, /endereco</h1>'

@app.route('/sobre')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/endereco')
def endereco():
    return render_template('endereco.html')