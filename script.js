// Lógica de Interatividade e WebSockets

// Alternar abas
function mudarAba(abaId) {
    document.querySelectorAll('.tab-content').forEach(aba => aba.classList.remove('active-tab'));
    document.getElementById(abaId).classList.add('active-tab');
}

// Conecta ao servidor Python via WebSocket
const socket = io();

// Cria um ID aleatório para sabermos quem é "Você" e quem são os "Outros"
const meuId = Math.random().toString(36).substring(7);

// Função que ESCUTA as mensagens chegando do servidor
socket.on('message', function(dados) {
    const boxMensagens = document.getElementById('box-mensagens');
    const divMsg = document.createElement('div');

    // Verifica se a mensagem foi enviada por você ou por outro usuário
    if(dados.id === meuId) {
        divMsg.className = 'msg user';
        divMsg.innerHTML = `<strong>Você:</strong> ${dados.texto}`;
    } else {
        divMsg.className = 'msg bot';
        divMsg.innerHTML = `<strong>Visitante:</strong> ${dados.texto}`;
    }

    boxMensagens.appendChild(divMsg);
    boxMensagens.scrollTop = boxMensagens.scrollHeight; // Rola para baixo
});

// Função que ENVIA a mensagem para o servidor
function enviarMensagem() {
    const input = document.getElementById('input-msg');
    const texto = input.value.trim();

    if (texto !== '') {
        // Envia um objeto com seu ID e o texto para o Python
        socket.send({ id: meuId, texto: texto });
        input.value = ''; // Limpa o campo
    }
}

// Enviar com a tecla Enter
function handleEnter(event) {
    if (event.key === 'Enter') enviarMensagem();
}