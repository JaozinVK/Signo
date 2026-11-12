from flask import Flask, render_template, request
from datetime import datetime, date
from database import conectar, criar_tabelas
from signos import identificar_signo, INFO_SIGNOS

# 1. Cria o aplicativo Flask PRIMEIRO
app = Flask(__name__)

# 2. Cria as tabelas do banco de dados
criar_tabelas()

# ============================================================
# ROTAS DO SISTEMA
# ============================================================

@app.route('/')
def index():
    # Tela inicial apenas com o formulário
    return render_template('index.html', resultado=None, erro=None)

@app.route('/admin')
def admin():
    # Busca todos os dados salvos no banco para mostrar na tela de admin
    with conectar() as con:
        cur = con.cursor()
        cur.execute("SELECT id, nome, data_nascimento, signo, data_hora_cadastro FROM pessoas ORDER BY id DESC")
        pessoas = cur.fetchall()
    
    # Organiza os dados para enviar ao HTML
    lista = []
    for p in pessoas:
        lista.append({
            'id': p[0], 'nome': p[1], 'nascimento': p[2], 
            'signo': p[3], 'cadastro': p[4]
        })
    
    return render_template('admin.html', pessoas=lista)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome', '').strip()
    data_str = request.form.get('data_nascimento', '').strip()
    
    # Validação do nome
    if not nome:
        return render_template('index.html', resultado=None, erro="O nome não pode ficar vazio.")

    # Validação da data (recebida do calendário no formato AAAA-MM-DD)
    try:
        dt = datetime.strptime(data_str, "%Y-%m-%d").date()
        if dt.year < 1900 or dt > date.today():
            raise ValueError()
    except ValueError:
        return render_template('index.html', resultado=None, erro="A data informada é inválida, não existe ou está no futuro. Por favor, use o calendário.")

    # Calcula o signo com base no dia e mês
    signo = identificar_signo(dt.day, dt.month)
    
    # Pega a data e hora exata do cadastro
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    # Formata a data de nascimento para o padrão brasileiro antes de salvar
    data_formatada_br = dt.strftime("%d/%m/%Y")

    # Salva no banco de dados
    with conectar() as con:
        cur = con.cursor()
        cur.execute("INSERT INTO pessoas (nome, data_nascimento, signo, data_hora_cadastro) VALUES (?, ?, ?, ?)",
                    (nome, data_formatada_br, signo, agora))
        con.commit()

    # Busca as informações e curiosidades do signo
    info = INFO_SIGNOS.get(signo, {})
    resultado = {
        'nome': nome,
        'signo': signo,
        'palavras': info.get('palavras', ''),
        'texto': info.get('texto', ''),
        'curiosidade': info.get('curiosidade', '')
    }

    # Retorna o HTML mostrando o resultado do signo
    return render_template('index.html', resultado=resultado, erro=None)

# ============================================================
# INICIALIZAÇÃO DO SERVIDOR
# ============================================================
if __name__ == '__main__':
    app.run(debug=True)