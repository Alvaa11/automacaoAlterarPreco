from tkinter import *
from tkinter import Tk, ttk
from controller import bot as b

co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters
co5 = "#0d00a4"


class View():
    def __init__(self):

        return
            
    def window(self):
        win = Tk()
        win.title('Rodar altera')
        win.geometry('310x330')
        win.configure(background=co1)
        win.resizable(height=FALSE, width=FALSE)

        def comecar():
            user = ent_user.get()
            senha = ent_pass.get()
            b.Bot(user, senha).rodar_altera()
            return 

        # Dividindo a janela ----------------
        frm_up = Frame(win, width=310, height=50, bg=co1, relief='flat').grid(column=0, row=0, padx=1, pady=0, sticky=NSEW)
        frm_down = Frame(win, width=310, height=250, bg=co1, relief='flat').grid(column=0, row=1, padx=1, pady=0, sticky=NSEW)


        # Configurando o fram de cima---------
        lbl_nome = Label(frm_up, text='RODAR ALTERA', anchor=NE, font=('Ivy 19'), bg=co1, fg=co4).place(x=5, y=7)
        lbl_linha = Label(frm_up, text='', width=140, height=1, anchor=NW, font=('Ivy 2'), bg=co3, fg=co4).place(x=10, y=46)
        
        # configurando a frame de baixo --------
        lbl_user = Label(frm_down, text='Usuário *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4).place(x=10, y=65)
        ent_user = Entry(frm_down, width=25, justify='left', font=('', 15), highlightthickness=1)
        ent_user.place(x=10, y=88)

        lbl_pass = Label(frm_down, text='Senha *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4).place(x=10, y=128)
        ent_pass = Entry(frm_down, width=25, justify='left', font=('', 15), highlightthickness=1,show='*')
        ent_pass.place(x=10, y=150)


        bttn = Button(frm_down, text='Começar!', relief='raised', font=('Ivy 8'), bg=co4, fg=co1, height=3, width=35, command=comecar).place(x=35, y=250)

        
        win.mainloop()




