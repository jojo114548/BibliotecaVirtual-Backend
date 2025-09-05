from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from service.usuario_service import UsuarioService

usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/")
def home():
    return render_template("index.html")

@usuario_bp.route("/login")
def login_get():
    return render_template("login.html")

@usuario_bp.route("/cadastro-usuario", methods=["POST"])
def cadastrar_usuario():
    dados = {
        "nome": request.form.get("nome"),
        "cpf": request.form.get("cpf"),
        "email": request.form.get("email"),
        "idade": request.form.get("idade"),
        "senha": request.form.get("senha"),
        "perfil": request.form.get("perfil", "user")
    }
    usuario = UsuarioService.cadastrar(dados)
    return render_template("index.html", usuario=usuario)

@usuario_bp.route("/cadastro-usuario", methods=["GET"])
def cadastro_get():
    return render_template("cadastro-usuario.html")

# ---------- LOGIN / LOGOUT ---------- #
@usuario_bp.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    senha = request.form.get("senha")

    usuario = UsuarioService.autenticar(email, senha)
    if usuario:
        session["id_usuario"] = usuario["id"]
        session["perfil"] = usuario["perfil"]
        session["nome"] = usuario["nome"]
        session["email"] = usuario["email"]
        session["cpf"] = usuario["cpf"]
        session["idade"] = usuario["idade"]
        return render_template("pagina_principal.html", usuario=usuario)
    return "Email ou senha inválidos", 401

@usuario_bp.route("/logout")
def logout():
    session.clear()
    return render_template("index.html")

# ---------- ROTAS PROTEGIDAS ---------- #
@usuario_bp.route("/usuarios/json")
def buscar_usuarios_json():
    if "id_usuario" not in session:
        return "Acesso negado. Faça login.", 401
    if session["perfil"] != "admin":
        return "Acesso negado. Área de administração.", 401
    return jsonify(UsuarioService.listar())

@usuario_bp.route("/usuarios")
def dados_usuarios():
    if "id_usuario" not in session:
        return "Acesso negado. Faça login.", 401
    usuarios = UsuarioService.listar()    
    if session["perfil"] == "admin":
        return render_template("area-admin.html", usuarios=usuarios)
    else:
        return render_template("editar-perfil.html", usuarios=usuarios)
    

@usuario_bp.route("/editar-perfil")
def editar_perfil():
    usuarios = UsuarioService.listar()    
    return render_template("editar-perfil.html", usuarios=usuarios)
    

@usuario_bp.route("/usuarios/<id>", methods=["DELETE"])
def excluir_usuario(id):
    usuario_logado_id = session.get("id_usuario")
    perfil_logado = session.get("perfil")
    
    if UsuarioService.deletar(id):
        if usuario_logado_id == id:
            session.clear()
            return jsonify({"mensagem": "Usuário deletado com sucesso. Você foi deslogado."}), 200
        return jsonify({"mensagem": "Usuário deletado com sucesso."}), 200
    return jsonify({"erro": "Usuário não encontrado."}), 404

@usuario_bp.route("/pagina-principal")
def pag_principal():
    return render_template("pagina_principal.html")

@usuario_bp.route("/usuarios/<id>", methods=["PUT"])
def atualizar_usuario(id):
    if "id_usuario" not in session:
        return "Acesso negado. Faça login.", 401

    usuario_edit = request.get_json()
    # Adicione o ID ao objeto recebido, se necessário
    usuario_edit["id"] = id
    if UsuarioService.atualizar(usuario_edit):
        return jsonify({"mensagem": "Usuário atualizado com sucesso"}), 200
    return jsonify({"erro": "Não foi possível salvar as modificações"}), 404


