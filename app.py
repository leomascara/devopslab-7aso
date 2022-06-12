from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Olá Mundo, por Leonardo Martins Scaramel da FIAP 7ASO"


if __name__ == '__main__':
    app.run()