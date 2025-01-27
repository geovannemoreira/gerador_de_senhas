from tkinter import *
from tkinter import ttk, messagebox
import random
import string
from PIL import Image, ImageTk

# Cores
cor_1 = "#0a0a0a"  
cor_2 = "#1f8f1f"   
cor_3 = "#21c25c" 
cor_4 = "#bb9" 

# Configuração da janela principal
janela = Tk()
janela.title("SENHA ALEATORIA")
janela.geometry("280x280")
janela.configure(bg=cor_2)
janela.resizable(False, False)

# Estilo
estilo = ttk.Style(janela)
estilo.theme_use("clam")

# Divisão da janela em dois frames
header = Frame(janela, height=40, bg=cor_2, pady=5, padx=9, relief="flat")
header.grid(row=0, column=0, sticky=NSEW)

# Corpo da tela fundo
main = Frame(janela, width=295, height=310, bg=cor_2, pady=0, padx=0, relief="flat")
main.grid(row=1, column=0, sticky=NSEW)

# Configuração da imagem e do nome do aplicativo 
try:
  img = Image.open('gerador_de_senhas/logo.png')
  img = img.resize((25, 25), Image.Resampling.LANCZOS)
  img = ImageTk.PhotoImage(img)
  logo = Label(header,  image=img, compound=CENTER, bg=cor_2, relief='flat')
  logo.grid(row=0, column=0, sticky=NSEW)
except Exception:
  pass

app_nome = Label(header, text='GERADOR DE SENHAS', font='Ivy 16 bold', bg=cor_2, fg=cor_1)
app_nome.grid(row=0, column=1, sticky=NSEW)

app_linha = Label(header,text='',width=200, height=1, padx=0, relief='sunken', anchor='nw', font='Ivy 1', bg=cor_3, fg=cor_1)
app_linha.grid(row=1, column=0, columnspan=2, sticky=NSEW)

# Função para copiar a senha
def copiar_senha():
  senha = app_senha['text']
  if senha and senha != '- - - -':
    janela.clipboard_clear()
    janela.clipboard_append(senha)
    messagebox.showinfo('Senha copiada', 'A senha foi copiada com sucesso!')
  else:
    messagebox.showwarning('Aviso', 'Nenhuma senha para copiar!')

# Função para gerar a senha
def criar_senha():
  comprimento = int(spin.get())

  # Combinar os caracteres com base nos checkboxes
  caracteres = ""
  if estado_1.get():
    caracteres += string.ascii_uppercase
  if estado_2.get():
    caracteres += string.ascii_lowercase
  if estado_3.get():
    caracteres += string.digits
  if estado_4.get():
    caracteres += "!@#$%&*"

  if not caracteres:
    messagebox.showwarning('Aviso', 'Selecione pelo menos um tipo de caractere!')
    return

  senha = ''.join(random.choices(caracteres, k=comprimento))
 # Se a senha tiver mais de 9 caracteres, colocar até 9 caracteres e adicionar "..." de cor diferente
  if len(senha) > 7:
    app_senha['text'] = f'{senha[:6]}...'
  else:
    app_senha['text'] = senha

# Configuração do frame main
## Tela onde exibe a senha
app_senha = Label(main, text='- - - -',width=18, height=1, relief='solid', font='Ivy 12 bold', bg=cor_4, fg=cor_1)
app_senha.grid(row=0, column=0, columnspan=1, padx=10, pady=0)

# Botão para copiar a senha 
botao_copiar = Button(main, text='Copiar', command=copiar_senha, width=6, height=1, font='Ivy 10 bold', bg=cor_4, fg=cor_1, relief='raised')
botao_copiar.grid(row=0, column=1, padx=8, sticky=E)

# Spinbox para o comprimento da senha 4 - 20
spin = Spinbox(main, from_=4, to=20, width=3, font='Ivy 10')
spin.grid(row=1, sticky=W, column=0, pady=8, padx=5)

# Texto e Spinbox para o comprimento da senha
total_de_caracteres = Label(main, text='Total de caracter (4 - 20)', font='Ivy 10 bold', bg=cor_2, fg=cor_1)
total_de_caracteres.grid(row=1, column=0, sticky=E, padx=5)


# faixa verde main 
faixa_verde = Label(main, text='', width=200, height=1, padx=0, relief='flat', anchor='nw', font='Ivy 1', bg=cor_3, fg=cor_1)
faixa_verde.grid(row=3, column=0, columnspan=2, sticky=NSEW, padx=0, pady=1)

frame_caracteres = Frame(main, bg=cor_2)
frame_caracteres.grid(row=4, sticky=W, column=0, columnspan=2, pady=5)


# Configuração dos checkboxes
estado_1 = BooleanVar()
check_1 = Checkbutton(frame_caracteres, text='ABC Letras maiúsculas', var=estado_1, bg=cor_2, font='Ivy 10 bold', relief='flat')
check_1.grid(row=0, column=0, sticky=W)

estado_2 = BooleanVar()
check_2 = Checkbutton(frame_caracteres, text='abc Letras minúsculas', var=estado_2, bg=cor_2, font='Ivy 10 bold', relief='flat')
check_2.grid(row=1, column=0, sticky=W)

estado_3 = BooleanVar()
check_3 = Checkbutton(frame_caracteres, text='123 Números', var=estado_3, bg=cor_2, font='Ivy 10 bold', relief='flat')
check_3.grid(row=2, column=0, sticky=W)

estado_4 = BooleanVar()
check_4 = Checkbutton(frame_caracteres, text='!@# Símbolos', var=estado_4, bg=cor_2, font='Ivy 10 bold', relief='flat')
check_4.grid(row=3, column=0, sticky=W)

# Botão para gerar a senha
botao_gerar = Button(main, text='Gerar Senha', command=criar_senha, width=20, height=1, font='Ivy 10 bold', bg=cor_4, fg=cor_2, relief='sunken', overrelief='solid')
botao_gerar.grid(row=5, column=0, columnspan=2, pady=10)


janela.mainloop()
