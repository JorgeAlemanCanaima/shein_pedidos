from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('pedidos.db')
    c = conn.cursor()
    c.execute('SELECT * FROM pedidos ORDER BY id DESC')
    pedidos = c.fetchall()
    conn.close()
    return render_template('index.html', pedidos=pedidos)

@app.route('/agregar', methods=['POST'])
def agregar_pedido():
    numero_pedido = request.form['numero_pedido']
    numero_seguimiento = request.form['numero_seguimiento']
    
    conn = sqlite3.connect('pedidos.db')
    c = conn.cursor()
    c.execute('INSERT INTO pedidos (numero_pedido, numero_seguimiento) VALUES (?, ?)',
              (numero_pedido, numero_seguimiento))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

@app.route('/actualizar_estado/<int:id>', methods=['POST'])
def actualizar_estado(id):
    nuevo_estado = request.form['estado']
    
    conn = sqlite3.connect('pedidos.db')
    c = conn.cursor()
    c.execute('UPDATE pedidos SET estado = ? WHERE id = ?',
              (nuevo_estado, id))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
