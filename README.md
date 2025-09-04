A seguir, um `README.md` detalhado para o projeto, com base nos arquivos fornecidos:

# Biblioteca Virtual

Este projeto é uma aplicação web simples para uma "Biblioteca Virtual", desenvolvida em Python usando o framework Flask. A aplicação permite o cadastro, autenticação e gerenciamento básico de usuários, com diferentes níveis de acesso (usuário e administrador).

-----

## Estrutura do Projeto

O projeto é organizado com base no padrão MVC (Model-View-Controller) e no conceito de Blueprints do Flask para modularização.

```
.
├── app.py
├── controller/
│   └── usuario_controller.py
├── model/
│   └── usuario.py
├── repository/
│   └── usuario_repository.py
├── service/
│   └── usuario_service.py
├── static/
│   ├── css/
│   │   ├── index.css
│   │   ├── logado.css
│   │   └── login.css
│   ├── imgs/
│   │   ├── ... (imagens do site)
│   └── script.js
└── templates/
    ├── area-admin.html
    ├── cadastro-usuario.html
    ├── editar-perfil.html
    ├── index.html
    ├── login.html
    └── pagina_principal.html
└── usuarios.json
```

-----

## Funcionalidades

### 1\. Sistema de Usuários

  * **Cadastro de Usuários**: A aplicação permite que novos usuários se registrem fornecendo nome, CPF, e-mail, idade e senha. A senha é armazenada com hash usando a biblioteca `bcrypt` para segurança. O usuário pode selecionar seu perfil (`user` ou `admin`) durante o cadastro.
  * **Autenticação**: O login é feito com e-mail e senha. O sistema valida a senha digitada com a senha armazenada (com hash) usando `bcrypt.checkpw()`.
  * **Controle de Sessão**: Após o login, a sessão do usuário é gerenciada pelo Flask, armazenando informações como `id`, `perfil` e `nome` para controle de acesso.
  * **Logout**: O usuário pode encerrar sua sessão a qualquer momento, o que limpa os dados da sessão e o redireciona para a página inicial.

### 2\. Gerenciamento de Dados

  * **Armazenamento de Dados**: Os dados dos usuários são persistidos em um arquivo JSON chamado `usuarios.json`.
  * **Ações CRUD (Create, Read, Update, Delete)**:
      * **Adicionar (Create)**: Adiciona um novo usuário ao arquivo JSON.
      * **Buscar (Read)**: Permite buscar usuários por e-mail. A lista completa de usuários também pode ser carregada.
      * **Atualizar (Update)**: Permite a atualização dos dados de um usuário. Essa funcionalidade é usada tanto pelo administrador para editar perfis quanto pelo próprio usuário para gerenciar suas informações.
      * **Deletar (Delete)**: Exclui um usuário do arquivo JSON com base em seu ID.

### 3\. Rotas e Páginas

  * **`/`**: Página inicial (home) do site com informações sobre a "Biblioteca Virtual".
  * **`/login`**: Página para autenticação de usuários.
  * **`/cadastro-usuario`**: Página para registro de novos usuários.
  * **`/pagina-principal`**: Página principal do usuário logado, exibindo sugestões de leitura e um menu lateral.
  * **`/usuarios`**: Rota que exibe a tabela de usuários. O acesso é controlado pelo perfil da sessão:
      * `admin`: Exibe a tabela de todos os usuários para gerenciamento.
      * `user`: Exibe apenas os dados do usuário logado para edição de seu próprio perfil.
  * **`/editar-perfil`**: Rota específica para o usuário comum editar seu perfil, visualizando somente seus dados.
  * **`/logout`**: Encerra a sessão do usuário.

-----

## Tecnologias Utilizadas

  * **Backend**: Python, Flask
  * **Segurança**: `bcrypt` (para hashing de senhas)
  * **Frontend**: HTML, CSS, JavaScript
  * **Bibliotecas de Estilo**: Bootstrap 5.3.8 (para a página inicial) e ícones Bootstrap (`bootstrap-icons`)
  * **Armazenamento**: JSON

-----

## Como Executar

1.  **Pré-requisitos**: Certifique-se de ter o Python 3.x instalado.
2.  **Instalar dependências**:
    ```bash
    pip install Flask bcrypt
    ```
3.  **Executar a aplicação**:
    ```bash
    python app.py
    ```
4.  Abra seu navegador e acesse `http://127.0.0.1:5000/`.

-----
