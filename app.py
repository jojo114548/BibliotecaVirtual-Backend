from flask import Flask
from controller.usuario_controller import usuario_bp

app = Flask(__name__)
app.secret_key = "sua_chave_super_secreta"

# 🔹 O Blueprint funciona como um "módulo de rotas"
# Em vez de definir todas as rotas direto aqui no app,
# nós criamos o usuario_bp no arquivo usuario_controller.py
# e registramos ele aqui para que faça parte da aplicação.

app.register_blueprint(usuario_bp)

if __name__ == "__main__":
 app.run(host='0.0.0.0',debug=False)