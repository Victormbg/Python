# Author: Crystian Fernandes <crystian.fr@gmail.com>
# -*- coding: utf-8 -*-
# 20180511T0620Z

from tela_calculadora_astronomica import *
from tkinter import *

# tela principal
janela = Tk()
janela.title("Calculadora Astronômica e Científica")
janela.geometry("300x25")

astronomica = Button(janela, text="calculadora astronomica", command=calculadora_astronomica)
astronomica.grid(row=0, column=0, stick=W)

cientifica = Button(janela, text="calculadora cientifica")
cientifica.grid(row=0, column=1)

janela.mainloop()