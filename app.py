# de flask importar Flask, renderizar_template, requisição, redirecionar, para_url
from flask import Flask, render_template, request, redirect, url_for
# importar conexão.mysql
import mysql.connector

"""
* @author : Sandun Induranga
* @since : 0.1.0
"""
# app ligando a = Flask(__name__)
app = Flask(__name__)
# cnx (conexão?) ligando a = conectar.conexão.mysql(usuário='', senha='', banco de dados='')
cnx = mysql.connector.connect(user='sandu', password='1234', database='POS')
# cursor ligando a = cnx.cursor() (conexão de cursor?)
cursor = cnx.cursor()

# rota do.@app na('raíz da aplicação')
@app.route('/')
# definir no index():
def index():
    # consultar ligando a = 'SELECIONAR * DE Cliente'
    query = 'SELECT * FROM Customer'
    # executar no.cursor(consulta)
    cursor.execute(query)
    # retornar renderizando_template em('index.html', cliente=cursor)
    return render_template('index.html', customers=cursor)

# rota do.@app na('/clientesalvar', métodos=['pegar','criar']
@app.route('/savecustomer', methods=['get', 'post'])
# definir no clientesalvar():
def savecustomer():
    # id = requisição no.formulário['cusId']
    id = request.form['cusId']
    # nome = requisição no.formulário['cusNome']
    name = request.form['cusName']
    # endereço = requisição no.formulário['endereço']
    address = request.form['address']
    # salário = requisição no.formulário['salário']
    salary = request.form['salary']

    # consultar ligando a = 'INSERIR DENTRO de Cliente os Valores (%s, %s, %s, %s)'
    query = 'INSERT INTO Customer VALUES (%s, %s, %s, %s)'
    # valores ligando a = (id, nome, endereço, salário)
    values = (id, name, address, salary)
    # executar.cursor(consulta, valores)
    cursor.execute(query, values)
    # retornar redirecionando(para_url('index'))
    return redirect(url_for('index'))

# rota do.@app na('/atualizar_cliente', métodos=['pegar','criar']
@app.route('/update_customer', methods=['get', 'post'])
# definir no atualizar_cliente():
def update_customer():
    # id = requisição no.formulário['cusId']
    id = request.form['cusId']
    # nome = requisição no.formulário['cusNome']
    name = request.form['cusName']
    # endereço = requisição no.formulário['endereço']
    address = request.form['address']
    # salário = requisição no.formulário['salário']
    salary = request.form['salary']

    # consultar ligando a = 'ATUALIZAR Cliente DEFININDO Nome cliente=%s, address=%s, salary=%s WHERE customerId=%s'
    query = 'UPDATE Customer SET customerName=%s, address=%s, salary=%s WHERE customerId=%s'
    # valores ligando a = (nome, endereço, salário, id)
    values = (name, address, salary, id)
    # executar.cursor(consulta, valores)
    cursor.execute(query, values)
    # retornar redirecionando(para_url('index'))
    return redirect(url_for('index'))

# rota do.@app na('/deletar_cliente', métodos=['pegar','criar']
@app.route('/delete_customer', methods=['get', 'post'])
# definir no deletar_cliente():
def delete_customer():
    # id = requisição no.formulário['cusId']
    id = request.form['cusId']
    # consultar ligando a = 'DELETAR DE Cliente ONDE Id cliente=\''+id+'\''
    query = 'DELETE FROM Customer WHERE customerId=\''+id+'\''
    # executar.cursor(consulta, valores)
    cursor.execute(query)
    # retornar redirecionando(para_url('index'))
    return redirect(url_for('index'))

# se __name__ for == '__main__':
if __name__ == '__main__':
    # iniciar.aplicativo()
    app.run()
