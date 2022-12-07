import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Minha primeira API dezembro 2022'

@app.route('/pegarvendas')
def pegarvendas():
    tabela = pd.read_csv('advertising.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total vendas': total_vendas}
    return jsonify(resposta)

app.run(host='0.0.0.0')

