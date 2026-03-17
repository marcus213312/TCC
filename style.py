 User 23:24

eu gostaria que você melhorasse essas linhas de código para a criação do meu site esportivo, com chats, login e catálogo de vendas.

HTML
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SportsHub - Loja & Chat</title>
    <style>
        /* Estilos Globais (CSS) */
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4; }
        header { background-color: #E2001A; color: white; padding: 15px 30px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 24px; font-weight: bold; cursor: pointer; }
        .nav-links button { background: none; border: none; color: white; font-size: 16px; margin: 0 10px; cursor: pointer; font-weight: bold; }
        .nav-links button:hover { text-decoration: underline; }
code
Code

/* Área de Login (Canto superior direito) */
    .login-area button { background-color: white; color: #E2001A; padding: 8px 15px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }
    
    /* Layout Principal */
    main { padding: 20px; max-width: 1200px; margin: 0 auto; }
    .tab-content { display: none; }
    .active-tab { display: block; }

    /* Estilos da Loja */
    .grid-produtos { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; }
    .produto-card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); text-align: center; }
    .produto-card img { max-width: 100%; height: 150px; object-fit: cover; border-radius: 5px; }
    .btn-comprar { background-color: #28a745; color: white; border: none; padding: 10px; width: 100%; border-radius: 5px; cursor: pointer; margin-top: 10px; }

    /* Estilos do Chat */
    .chat-container { background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); display: flex; flex-direction: column; height: 500px; }
    .mensagens { flex-grow: 1; padding: 20px; overflow-y: auto; border-bottom: 1px solid #ddd; }
    .msg { margin-bottom: 10px; padding: 10px; border-radius: 5px; max-width: 70%; }
    .msg.bot { background-color: #f1f1f1; align-self: flex-start; }
    .msg.user { background-color: #E2001A; color: white; align-self: flex-end; margin-left: auto; }
    .input-area { display: flex; padding: 10px; }
    .input-area input { flex-grow: 1; padding: 10px; border: 1px solid #ccc; border-radius: 5px; margin-right: 10px; }
    .input-area button { background-color: #E2001A; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }
</style>

</head>
<body>
code
Code

<header>
    <div class="logo">SportsHub</div>
    <div class="nav-links">
        <button onclick="mudarAba('loja')">Loja</button>
        <button onclick="mudarAba('chat')">Chat Global</button>
    </div>
    <div class="login-area">
        <button onclick="alert('Área de Login em construção pelo Back-end (Python)!')">Entrar / Cadastrar</button>
    </div>
</header>

<main>
    <section id="loja" class="tab-content active-tab">
        <h2>Lançamentos Esportivos</h2>
        <div class="grid-produtos">
            <div class="produto-card">
                <img src="https://via.placeholder.com/250x150/eee?text=Chuteira+Pro" alt="Chuteira">
                <h3>Chuteira Campo Pro</h3>
                <p>R$ 299,90</p>
                <button class="btn-comprar">Comprar</button>
            </div>
            <div class="produto-card">
                <img src="https://via.placeholder.com/250x150/eee?text=Camisa+Time" alt="Camisa">
                <h3>Camisa Oficial 24/25</h3>
                <p>R$ 159,90</p>
                <button class="btn-comprar">Comprar</button>
            </div>
            <div class="produto-card">
                <img src="https://via.placeholder.com/250x150/eee?text=Tenis+Corrida" alt="Tênis">
                <h3>Tênis Running X</h3>
                <p>R$ 499,90</p>
                <button class="btn-comprar">Comprar</button>
            </div>
        </div>
    </section>

    <section id="chat" class="tab-content">
        <h2>Chat da Comunidade</h2>
        <div class="chat-container">
            <div class="mensagens" id="box-mensagens">
                <div class="msg bot"><strong>Sistema:</strong> Bem-vindo ao chat da SportsHub! Compartilhe suas dicas esportivas.</div>
            </div>
            <div class="input-area">
                <input type="text" id="input-msg" placeholder="Digite sua mensagem..." onkeypress="handleEnter(event)">
                <button onclick="enviarMensagem()">Enviar</button>
            </div>
        </div>
    </section>
</main>

<script>
    // Lógica de Interatividade (JavaScript)

    // Função para alternar entre as abas Loja e Chat
    function mudarAba(abaId) {
        document.querySelectorAll('.tab-content').forEach(aba => {
            aba.classList.remove('active-tab');
        });
        document.getElementById(abaId).classList.add('active-tab');
    }

    // Função para enviar mensagem no chat
    function enviarMensagem() {
        const input = document.getElementById('input-msg');
        const texto = input.value.trim();
        const boxMensagens = document.getElementById('box-mensagens');

        if (texto !== '') {
            // Cria a div da mensagem do usuário
            const divMsg = document.createElement('div');
            divMsg.className = 'msg user';
            divMsg.innerHTML = `<strong>Você:</strong> ${texto}`;
            
            // Adiciona na tela
            boxMensagens.appendChild(divMsg);
            input.value = '';
            
            // Rola o chat para o final
            boxMensagens.scrollTop = boxMensagens.scrollHeight;

            // Simula uma resposta do sistema (ou outro usuário) após 1 segundo
            setTimeout(() => {
                const divResposta = document.createElement('div');
                divResposta.className = 'msg bot';
                divResposta.innerHTML = `<strong>Atendimento:</strong> Recebemos sua mensagem: "${texto}". Como podemos ajudar com seus equipamentos esportivos?`;
                boxMensagens.appendChild(divResposta);
                boxMensagens.scrollTop = boxMensagens.scrollHeight;
            }, 1000);
        }
    }

    // Permite enviar mensagem apertando a tecla "Enter"
    function handleEnter(event) {
        if (event.key === 'Enter') {
            enviarMensagem();
        }
    }
</script>

</body>
</html>

PYTHON

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(name)
app.config['SECRET_KEY'] = 'chave_secreta_aqui'
socketio = SocketIO(app)

app.route('/')
def home():
# Aqui o Python buscaria os produtos no banco de dados
produtos = [{"nome": "Chuteira", "preco": 299.90}, {"nome": "Camisa", "preco": 159.90}]
return render_template('index.html', produtos=produtos)

@socketio.on('message')
def handleMessage(msg):
print('Mensagem recebida: ' + msg)
# Reenvia a mensagem para todos os usuários conectados
send(msg, broadcast=True)

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(name)
app.config['SECRET_KEY'] = 'chave_super_secreta_sports_hub'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def home():
return render_template('index.html')

@socketio.on('message')
def handle_message(dados):
# Quando recebe uma mensagem de um usuário, reenvia para TODOS conectados
send(dados, broadcast=True)