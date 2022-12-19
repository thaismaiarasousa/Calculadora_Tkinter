"""Calculadora simples feita a partir do módulo Tkinter, de Python."""

#importo o módulo tkinter e o conjunto de widgets ttk
from tkinter import *
from tkinter import ttk

# Definindo as cores
cor1="#f588fc"   #rosa bebê 
cor2="#f16bfa"   #rosa bebê escuro
cor3="#ECEFF1"   #cinza
cor4="#b8e9ff"   #azul claro
cor5="#6bcdfa"   #azul piscina

# Criando a janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x301")
janela.configure(bg=cor1)

# Criando frames
frame_tela= Frame(janela, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

# Criando o corpo da página
frame_corpo= Frame(janela, width=235, height=267)
frame_corpo.grid(row=1, column=0)

# Recebe e concatena todos os valores enviados por str(valor).
todos_valores=''   

# Criando funções
def entrar_valores(valor):
    # Esta função recebe todos os valores ingressados pelo usuário. Ao definir todos_valores como global é possível manter o valor correspondente em todas as variáveis todos_valores no código.
    global todos_valores
    todos_valores = todos_valores + str(valor)
    valor_texto.set(todos_valores) # expressão impressa.

def calcular():
    # Avalia todos os caracteres que são guardados dentro de "todos_valores".
    resultado = eval(todos_valores) # eval executa expressões que são passadas a ela como uma Str e nos dá o resultado como uma expressão matemática.
    
    valor_texto.set(str(resultado)) # Se recupera o valor de valor_texto e se imprime na tela.
    
def limpar_tela():
    # Apaga caracteres impressos.
    global todos_valores # Limpa o valor desta variável de maneira global.
    todos_valores=""
    valor_texto.set("") # Recupera o valor de valor_texto e lhe atribui uma cadeia vazia.

# Criando Label (para exibir textos/imagens na tela).
valor_texto = StringVar() 

# Se cria a variável app_label chamando à classe Label para receber os valores de usuário.
app_label = Label(frame_tela, textvariable=valor_texto, width=24, height=3, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('arturo'), bg=cor3)
app_label.place(x=0, y=0)

# Se cria as variáveis b_1 - b_18 chamando à classe Button para receber os valores de usuário.
# Criando botões 1a linha
b_1 = Button(frame_corpo,command = limpar_tela, text="C", width=11, height=2, bg=cor3, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command = lambda:entrar_valores('%'), text="%", width=6, height=2, bg=cor3, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=109, y=0)
b_3 = Button(frame_corpo, command = lambda:entrar_valores('/'), text="/", width=6, height=2, bg=cor5, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=173, y=0)

# Criando botões segunda linha 
b_4 = Button(frame_corpo, command = lambda:entrar_valores('7'), text="7", width=6, height=2, bg=cor3, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=51)
b_5 = Button(frame_corpo, command = lambda:entrar_valores('8'), text="8", width=6, height=2, bg=cor3, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=58, y=51)
b_6 = Button(frame_corpo, command = lambda:entrar_valores('9'), text="9", width=6, height=2, bg=cor3, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=51)
b_7 = Button(frame_corpo, command = lambda:entrar_valores('*'), text="*", width=6, height=2, bg=cor5, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=173, y=51)

# Criando botões terceira linha
b_8 = Button(frame_corpo,command = lambda:entrar_valores('4'), text="4", width=6, height=2, bg=cor3, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=101)
b_9 = Button(frame_corpo, command = lambda:entrar_valores('5'), text="5", width=6, height=2, bg=cor3, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=58, y=101)
b_10 = Button(frame_corpo, command = lambda:entrar_valores('6'), text="6", width=6, height=2, bg=cor3, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=101)
b_11 = Button(frame_corpo, command = lambda:entrar_valores('-'), text="-", width=6, height=2, bg=cor5, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=173, y=101)

# Criando botões quarta linha
b_12 = Button(frame_corpo, command = lambda:entrar_valores('1'), text="1", width=6, height=2, bg=cor3, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=151)
b_13 = Button(frame_corpo, command = lambda:entrar_valores('2'), text="2", width=6, height=2, bg=cor3, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=58, y=151)
b_14 = Button(frame_corpo, command = lambda:entrar_valores('3'), text="3", width=6, height=2, bg=cor3, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=151)
b_15 = Button(frame_corpo, command = lambda:entrar_valores('+'), text="+", width=6, height=2, bg=cor5, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=173, y=151)

# Criando botões quinta linha
b_16 = Button(frame_corpo, command = lambda:entrar_valores('0'), text="0", width=6, height=2, bg=cor3, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=201)
b_17 = Button(frame_corpo, command = lambda:entrar_valores('.'), text=".", width=6, height=2, bg=cor3, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=58, y=201)
b_18 = Button(frame_corpo, command = calcular, text="=", width=12, height=2, bg=cor3, font=('arturo'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=118, y=201)
    
# O método mainloop() é chamado e atribuído à variável janela, mantendo a janela aberta até que o próprio usuário a feche.
janela.mainloop()