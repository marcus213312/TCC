from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sports_hub_chave_super_secreta_2026'
socketio = SocketIO(app, cors_allowed_origins="*")

# ==================== DADOS DE PRODUTOS (pode vir do banco depois) ====================
PRODUTOS = [
    {"nome": "Chuteira Campo Pro", "preco": "299,90", "imagem": "https://picsum.photos/id/160/300/200"},
    {"nome": "Camisa Oficial 24/25", "preco": "159,90", "imagem": "https://picsum.photos/id/201/300/200"},
    {"nome": "Tênis Running X", "preco": "499,90", "imagem": "https://picsum.photos/id/29/300/200"},
    {"nome": "Bola de Futebol Profissional", "preco": "89,90", "imagem": "https://picsum.photos/id/180/300/200"},
    {"nome": "Raquete de Tênis Elite", "preco": "349,90", "imagem": "https://picsum.photos/id/251/300/200"},
]

# ==================== ROTAS ====================
@app.route('/')
def home():
    usuario = session.get('usuario')
    return render_template('index.html', produtos=PRODUTOS, usuario=usuario)

@app.route('/login', methods=['POST'])
def login():
    nome = request.form.get('nome_usuario', '').strip()
    if nome:
        session['usuario'] = nome
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('home'))

# ==================== CHAT SOCKETIO ====================
@socketio.on('message')
def handle_message(dados):
    print(f"📨 Mensagem de {dados.get('usuario')}: {dados.get('texto')}")
    send(dados, broadcast=True)   # envia para TODOS os conectados

if __name__ == '__main__':
    print("🚀 SportsHub rodando em http://127.0.0.1:5000")
    socketio.run(app, debug=True, port=5000)