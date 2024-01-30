import tkinter as tk

def clique_do_botao():
    txt.config(text='Botão Pressionado')

home = tk.Tk()
home.title('Login')

txt = tk.Label(home, text='Olá, Mundo!')

botao = tk.Button(home, text='Clique Aqui', command=clique_do_botao)

txt.pack()
botao.pack()

home.mainloop()