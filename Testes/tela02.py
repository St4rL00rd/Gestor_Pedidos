import tkinter as tk
from tkinter import ttk
import pyodbc

def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2
    
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

# Função para o formulário
def fazer_login():
    # Conectar ao banco  de dados  Access
    conn_str = r'DRIVER={Microsoft Access Drive (*.mdb, *.accdb)};DBQ=C:\caminho\DB.accdb;'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # Obter usuário e senha do formulário
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
    # Consulta SQL para verificar se o usuário e senha estão corretos
    query = f"SELECT * FROM TabelaUsuarios WHERE NomeUsuarios = '{usuario}' AND Senha ='{senha}'"
    cursor.execute(query)
    
    # Verificar se há algum resultado
    if cursor.fetchone():
        print('Login bem-sucedido!')
    else:
        print('Usuário ou senha incorretos')
        
    cursor.close()
    conn.close()
    
    print(f'Usuário: {usuario}\nSenha: {senha}')

    # Destroi a janela atual
    janela.destroy()

    # Criar e exibir a nova janela (janela2)
    janela2 = tk.Tk()
    janela2.title('Pedidos')

    # Define que a tela inicie maximizada
    janela2.state('zoomed')
    
    # Define o tamanho padrão da janela
    largura = 1000
    altura = 600
    janela2.geometry(f'{largura}x{altura}')
    
    centralizar_janela(janela2, largura, altura)

    # Iniciando o loop da aplicação da janela2
    janela2.mainloop()

# Criando a janela principal
janela = tk.Tk()
janela.title('Home')

# Definindo o tamanho padrão da tela
largura = 1000
altura = 600
janela.geometry(f'{largura}x{altura}')

# Criando um frame
frame_login = ttk.Frame(janela, padding="10")
frame_login.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Adicionando rótulos e entradas para usuário e senha
rotulo_usuario = ttk.Label(frame_login, text='Usuário:')
rotulo_usuario.grid(column=0, row=0, sticky=tk.W)

entrada_usuario = ttk.Entry(frame_login)
entrada_usuario.grid(column=1, row=0, sticky=(tk.W, tk.E))

rotulo_senha = ttk.Label(frame_login, text='Senha:')
rotulo_senha.grid(column=0, row=1, sticky=tk.W)

entrada_senha = ttk.Entry(frame_login, show='*')
entrada_senha.grid(column=1, row=1, sticky=(tk.W, tk.E))

# Adicionando um botão ao frame
botao_login = ttk.Button(frame_login, text='Login', command=fazer_login)
botao_login.grid(column=1, row=2, sticky=tk.E)

# Centralizando janela
centralizar_janela(janela, largura, altura)

# Iniciando o loop da aplicação
janela.mainloop()