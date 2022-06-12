from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Olá Mundo, por Leonardo Martins Scaramel da FIAP 7ASO"

if __name__ == '__main__':
    app.run()