
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from flask_cors import CORS
import hashlib

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world(Test):
    return 'FilmChase Cripto bc no full db :)'

@app.route('/gerar-hash', methods=['POST'])
def gerar_hash():
    data = request.get_json()
    text = data.get('password', '')
    # Cria um objeto de hash SHA256
    sha256 = hashlib.sha256()

    # Atualiza o hash com o texto
    sha256.update(text.encode())

    # Obtém o valor hash em formato hexadecimal
    hash_value = sha256.hexdigest()

    return hash_value


if __name__ == '__main__':
    app.run()