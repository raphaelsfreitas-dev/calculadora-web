from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Conectar ao banco de dados SQLite
def get_db_connection():
    conn = sqlite3.connect('calculos.db')
    conn.row_factory = sqlite3.Row
    return conn

# Criar tabela de cálculos (se não existir)
def criar_tabela():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS calculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expressao TEXT NOT NULL,
            resultado TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Rota para calcular e salvar no banco de dados
@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    expressao = data['expressao']

    try:
        resultado = str(eval(expressao))  # Avalia a expressão matemática
        # Salva no banco de dados
        conn = get_db_connection()
        conn.execute('INSERT INTO calculos (expressao, resultado) VALUES (?, ?)',
                     (expressao, resultado))
        conn.commit()
        conn.close()
        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'resultado': 'Erro'}), 400

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)
