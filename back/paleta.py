from flask import Flask, jsonify, request
import colorsys
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Rota para gerar paleta de cores
@app.route('/gerar_paleta', methods=['GET'])
def gerar_paleta():
    # Obtém a quantidade de cores da query string
    quantidade = int(request.args.get('quantidade'))

    # Lista vazia para armazenar as cores
    cores = []

    # Gera as cores aleatórias
    for i in range(quantidade):
        # Gera valores aleatórios de matiz, saturação e luminosidade
        h = random.random()
        s = random.random() * 0.5 + 0.4
        l = random.random() * 0.5 + 0.4

        # Converte a cor de HSL para RGB
        r, g, b = colorsys.hls_to_rgb(h, l, s)

        # Converte a cor de RGB para hexadecimal
        cor_hex = "#{:02x}{:02x}{:02x}".format(
            int(r * 255),
            int(g * 255),
            int(b * 255)
        )

        # Adiciona a cor à lista de cores
        cores.append(cor_hex)

    # Retorna a lista de cores como JSON
    return jsonify(cores)

if __name__ == '__main__':
    app.run()