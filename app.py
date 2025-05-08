from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('pedidos.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    pedidos = conn.execute('SELECT * FROM pedidos ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', pedidos=pedidos)

@app.route('/agregar', methods=['POST'])
def agregar():
    numero_pedido = request.form['numero_pedido']
    numero_seguimiento = request.form['numero_seguimiento']
    cantidad_items = request.form['cantidad_items']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO pedidos (numero_pedido, numero_seguimiento, cantidad_items) VALUES (?, ?, ?)',
                 (numero_pedido, numero_seguimiento, cantidad_items))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
