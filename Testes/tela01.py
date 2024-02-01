import tkinter as tk
from tkinter import ttk

def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    x = (largura_tela - largura) //2
    y = (altura_tela - altura) //2
    
    janela.geometry(f'{largura}x{altura}+{x}+{y}')
    
# Função para formulario
def fazer_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
    print(f'Usuário: {usuario}\nSenha: {senha}')

# Criando a janela principal
janela = tk.Tk()
janela.title('Home')

# Cria nova janela
janela2 = tk.Tk()
janela2.title('Pedidos')

janela.destroy()

# Definindo o tamanho padrão da tela
largura = 1000
altura = 600
janela.geometry(f'{largura}x{altura}')

# Criando um frame
frame_login = ttk.Frame(janela, padding="10")
frame_login.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Adicionando rotulos e entradas para usuario e senha
rotulo_usuario = ttk.Label(frame_login, text='Usuário:')
rotulo_usuario.grid(column=0, row=0,sticky=tk.W)

entrada_usuario = ttk.Entry(frame_login)
entrada_usuario.grid(column=1 , row=0, sticky=(tk.W, tk.E))

rotulo_senha = ttk.Label(frame_login, text='Senha:')
rotulo_senha.grid(column=0, row=1,sticky=tk.W)

entrada_senha = ttk.Entry(frame_login, show='*')
entrada_senha.grid(column=1, row=1, sticky=(tk.W, tk.E))

# Adicionando um botão ao frame
botao_login = ttk.Button(frame_login, text='Login', command=fazer_login)
botao_login.grid(column=1, row=2, sticky=tk.E)

# Centralizando janela
centralizar_janela(janela, largura, altura)

# Iniciando o loop da aplicação
janela.mainloop()