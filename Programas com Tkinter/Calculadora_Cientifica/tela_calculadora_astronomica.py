import math
from tkinter import *

# constantes globais
lum_sol = 3.828e+26 # luminosidade solar
rad_sol = 695500000 # raio solar em metro
temp_sol = 5778 # temperatura solar em Kelvin
mass_sol = 1.98855e+30 # massa solar em kg
sig = 5.670367e-8 # Stefan-Boltzmann constant
AU = 149597870691 # unidade astronômica em metro
c = 299792458 # velociade da luz em m/s
hbar = 1.0545718e-34 # constante de Planck reduzida
G = 6.67408e-11 # Constante gravitacional
k = 1.38066e-23 # Boltzmann constant

# tela calculadora_astronomica
def calculadora_astronomica():
    janela = Tk()
    janela.title("Calculadora Astronômica")
    janela.geometry("325x25")
        
    # funcoes da calculadora_astronomica
    # funcao black_hole()
    def black_hole():
        janela = Tk()
        janela.title("Parâmetros do Buraco negro")
        janela.geometry("420x250")

        def limpar():
            radius_AU["text"] = ""
            diameter_AU["text"] = ""
            radius["text"] = ""
            diameter["text"] = ""
            surface_area["text"] = ""
            surface_gravity["text"] = ""
            surface_tides["text"] = ""
            entropia["text"] = ""
            temp["text"] = ""
            luminosidade["text"] = ""
            life_time["text"] = ""

        def blackhole():
            mass = float(massa.get())
            bhmass = mass*mass_sol
            radius["text"] = (2*G*bhmass)/(pow(c,2))
            radius_AU["text"] = radius["text"]/AU
            diameter_AU["text"] = 2*radius_AU["text"]
            diameter["text"] = 2*radius["text"]
            surface_area["text"] = ((16*math.pi*pow(G,2)*pow(bhmass,2)))/(pow(c,4))
            surface_gravity["text"] = (pow(c,4))/(bhmass*4*G)
            surface_tides["text"] = (pow(c,6))/(pow(bhmass,2)*pow(G,2)*4)
            entropia["text"] = (4*math.pi*G*pow(bhmass,2))/(hbar*c*math.log(10))
            temp["text"] = (hbar*pow(c,3))/(bhmass*8*k*math.pi*G)
            luminosidade["text"] = (hbar*pow(c,6))/(pow(bhmass,2)*15360*math.pi*pow(G,2))
            life_time["text"] = (pow(bhmass,3)*5120*math.pi*pow(G,2))/(hbar*pow(c,4))

        lb = Label(janela, text="Digite a massa do buraco negro em unidade de massa solar: ")
        lb.grid(row=0, column=0)

        massa = Entry(janela)
        massa.grid(row=0, column=1)

        lb = Label(janela, text="Raio:")
        lb.grid(row=2, column=0, stick=W)
        radius_AU = Label(janela, text="")
        radius_AU.grid(row=2, column=0)
        au = Label(janela, text="AU")
        au.grid(row=2, column=1, stick=W)

        lb = Label(janela, text="Diâmetro:")
        lb.grid(row=3, column=0, stick=W)
        diameter_AU = Label(janela, text="")
        diameter_AU.grid(row=3, column=0)
        lb = Label(janela, text="AU")
        lb.grid(row=3, column=1, stick=W)

        lb = Label(janela, text="Raio:")
        lb.grid(row=4, column=0, stick=W)
        radius = Label(janela, text="")
        radius.grid(row=4, column=0)
        lb = Label(janela, text="m")
        lb.grid(row=4, column=1, stick=W)

        lb = Label(janela, text="Diâmetro:")
        lb.grid(row=5, column=0, stick=W)
        diameter = Label(janela, text="")
        diameter.grid(row=5, column=0)
        lb = Label(janela, text="m")
        lb.grid(row=5, column=1, stick=W)

        lb = Label(janela, text="Área superfície:")
        lb.grid(row=6, column=0, stick=W)
        surface_area = Label(janela, text="")
        surface_area.grid(row=6, column=0)
        lb = Label(janela, text="m²")
        lb.grid(row=6, column=1, stick=W)

        lb = Label(janela, text="Aceleração gravitacional:")
        lb.grid(row=7, column=0, stick=W)
        surface_gravity = Label(janela, text="")
        surface_gravity.grid(row=7, column=0, stick=E)
        lb = Label(janela, text="m²")
        lb.grid(row=7, column=1, stick=W)

        lb = Label(janela, text="Força de maré:")
        lb.grid(row=8, column=0, stick=W)
        surface_tides = Label(janela, text="")
        surface_tides.grid(row=8, column=0)
        lb = Label(janela, text="m/s²/m")
        lb.grid(row=8, column=1, stick=W)

        lb = Label(janela, text="Entropia:")
        lb.grid(row=9, column=0, stick=W)
        entropia = Label(janela, text="")
        entropia.grid(row=9, column=0)

        lb = Label(janela, text="Temperatura:")
        lb.grid(row=10, column=0, stick=W)
        temp = Label(janela, text="")
        temp.grid(row=10, column=0)
        lb = Label(janela, text="K")
        lb.grid(row=10, column=1, stick=W)

        lb = Label(janela, text="Luminosidade:")
        lb.grid(row=11, column=0, stick=W)
        luminosidade = Label(janela, text="")
        luminosidade.grid(row=11, column=0)
        lb = Label(janela, text="W")
        lb.grid(row=11, column=1, stick=W)

        lb = Label(janela, text="Tempo de vida:")
        lb.grid(row=12, column=0, stick=W)
        life_time = Label(janela, text="")
        life_time.grid(row=12, column=0)
        lb = Label(janela, text="s")
        lb.grid(row=12, column=1, stick=W)

        calculo = Button(janela, text="CALCULAR", command=blackhole)
        calculo.grid(row=13, column=0, stick=W)

        limpar = Button(janela, text="LIMPAR", command=limpar)
        limpar.grid(row=13, column=1, stick=E)

        janela.mainloop()
        
    # funcao zh()
    def zh():
        janela = Tk()
        janela.title("Luminosidade e Zona Habitavel da estrela")
        janela.geometry("420x250")
            
        bt = Button(janela, text="test")
        bt.grid(row=0, column=0)
            
        janela.mainloop()

    # botoes tela calculadora_astronomica
    bh = Button(janela, text="calcular parametros do BH", command=black_hole)
    bh.grid(row=0, column=0, stick=W)

    zh = Button(janela, text="calcular luminosidade e ZH da estrela", command=zh)
    zh.grid(row=0, column=1, stick=E)

    janela.mainloop()