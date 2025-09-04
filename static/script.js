function excluirUsuario(cpf, id) {
    if (!confirm(`Tem certeza que deseja excluir o usuário com CPF: ${cpf}?`)) {
        return;
    }

    fetch(`/usuarios/${id}`, {
        method: 'DELETE'
    })
        .then(response => {
            return response.json().then(data => {
                if (!response.ok) {
                    throw new Error(data.erro || "Erro desconhecido");
                }
                return data;
            });
        })
        .then(data => {
            alert(data.mensagem);
            // Se for o usuário logado, redireciona para logout
            window.location.href = "/logout";
        })
        .catch(error => {
            console.error("Erro na requisição", error);
            alert("Erro ao excluir usuário: " + error.message);
        });
}


function preencherFormulario(button) {
    var container = document.querySelector(".container")
    var usuario = JSON.parse(button.getAttribute('data-usuario'))
    container.style.display = "grid";
    document.getElementById('id').value = usuario.id
    document.getElementById('nome').value = usuario.nome
    document.getElementById('email').value = usuario.email
    document.getElementById('idade').value = usuario.idade
    document.getElementById('cpf').value = usuario.cpf
    document.getElementById('perfil').value = usuario.perfil
}

document.getElementById('form-atualizar-usuario').addEventListener('submit', atualizarUsuario);

function atualizarUsuario(event) {
    event.preventDefault();

    if (!confirm("Tem certeza que deseja alterar os dados do usuário?")) {
        return;
    }

    const id = document.getElementById('id').value;
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const idade = document.getElementById('idade').value;
    const cpf = document.getElementById('cpf').value;
    const perfil = document.getElementById('perfil').value;

    const usuario = { id, nome, email, idade, cpf, perfil };
    console.log("Dados do usuário enviados:", usuario); // Log para depuração

    fetch(`/usuarios/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(usuario)
    })
        .then(response => {
            console.log("Resposta do servidor:", response); // Log para depuração
            if (!response.ok) {
                throw new Error(`Erro HTTP: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("Dados recebidos:", data); // Log para depuração
            alert("Usuário atualizado com sucesso!");
            location.reload();
        })
        .catch(error => {
            console.error("Erro ao atualizar:", error);
            alert("Erro ao atualizar usuário: " + error.message);
        });
}
