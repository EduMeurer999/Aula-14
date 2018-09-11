from tkinter import *
import tkinter as tk

def bt_click():

    

def bt_az():
   

janela.title("Banco do Edu")
janela["bg"] = "green"
#L=Largura A=Altura E=Distancia da borda Esqueda da tela T=Distancia do Topo da Tela
#L*A+E+T
L= "1200"
A= "800"
E= "100"
T= "100"
tamanho = str(L+"x"+A+"+"+E+"+"+T)
janela.geometry(tamanho)
lb= Label(janela, text="Banco do Edu", bg = janela['bg'], font = "Arial 16")
lb.place(x=50, y=10)
global lbNulo
lbNulo= Label(janela, bg=janela["bg"], text="")
lb= Label(janela, text="Titulo", bg = janela['bg'], font = "Arial 12")
lb.place(x=60, y=50)
edtTitulo = Entry(janela, width=20)
edtTitulo.place(x=200, y=50)

lb= Label(janela, text="Autor", bg = janela['bg'], font = "Arial 12")
lb.place(x=60, y=80)
edtAutor = Entry(janela, width=20)
edtAutor.place(x=200, y=80)

lb= Label(janela, text="Ano de edição", bg = janela['bg'], font = "Arial 12")
lb.place(x=60, y=110)
edtAnoEdicao = Entry(janela, width=20)
edtAnoEdicao.place(x=200, y=110)

lb= Label(janela, text="Editora", bg = janela['bg'], font = "Arial 12")
lb.place(x=60, y=140)
edtEditora = Entry(janela, width=20)
edtEditora.place(x=200, y=140)

MODES = [
    "Literatura",
    "Técnico",
    "Periódico",
    "Didáticos"
]

v = StringVar()
v.set("Literatura")  # initialize
cont=0
for text in MODES:
    cont = cont + 30
    b = Radiobutton(janela, text=text, bg=janela["bg"],
                    variable=v, value=text.lower())
    b.place(x= 70, y= 170+cont)

lb= Label(janela, text="Categoria do livro", bg = janela['bg'], font = "Arial 12")
lb.place(x=60, y=170)

bt = Button(janela, width=20, text="Cadastrar Livro", command=lambda: bt_click())
bt.place(x=100, y=350)

btListarAZ = Button(janela, width=20, text="Listar por Ordem Alfabética", command=lambda: bt_az())
btListarAZ.place(x=200, y=400)


btListarAZ = Button(janela, width=20, text="Listar por Categoria", command=lambda: bt_cat())
btListarAZ.place(x=200, y=450)
variable = StringVar(janela)
variable.set("Literatura") # default value
w = OptionMenu(janela, variable, "Literatura", "Técnico", "Periódico", "Didáticos")
w.place(x= 400, y=450)

list = Listbox(janela, bg="white", width= "100", height = "15")
list.place(x= 300, y= 500)

list.insert("1", "A")



janela.mainloop()