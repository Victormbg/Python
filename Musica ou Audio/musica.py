from pygame  import mixer # Load the required library
from tkinter.filedialog import askopenfilename
from tkinter import *

musicas = []

class Reprodutor :
    def __init__ (self):
       pass

    def escolher ():
        selecionar = askopenfilename(initialdir="C:/Users/",
                           filetypes =(("Arquivo de audio", "*.mp3"),("All Files","*.*")),
                           title = "Selecione as musicas"
                           )
        musicas.append(selecionar)
        return musicas

    def reproduzir ():
        """ 
        mixer.init()
        mixer.music.load('C:/Users/Andreza/Music/Jeff The Killer Theme Song Piano Version Sweet Dreams Are Made Of Screams.mp3')
        mixer.music.play()
        """

        mixer.init()

        for item in musicas:
            musica_atual = mixer.music.load(item)
            musica_atual = mixer.music.play()

    def parar ():
        musica_atual = mixer.music.stop()

    def pausar ():
        musica_atual = mixer.music.pause()

    def retomar ():
        musica_atual = mixer.music.unpause() #Continua da local pausado


    def proxima ():
        for item in range(len(musicas)):
            musica_atual = mixer.music.load(musicas[item])
            musica_atual = mixer.music.play()
            item += 1


    def anterior ():
        for item in range(len(musicas)):
            musica_atual = mixer.music.load(musicas[item])
            musica_atual = mixer.music.play()
            item -= 1 



player = Reprodutor

janela =Tk()

janela.title("REPRODUTOR - FÉLIX LICHT") #Titulo

#Esta parte é que está com problemas
bt_escolher = Button(janela, width=20, text="ADICIONAR MUSICAS", command=player.escolher)
bt_proxima  = Button(janela, width=10, text="PROXIMA",            command=player.proxima)
bt_anterior = Button(janela, width=10, text="ANTERIOR",          command=player.anterior)

bt_escolher.place (x=10,  y=50 )
bt_proxima.place  (x=170, y=50)
bt_anterior.place (x=270, y=50)



bt_play    = Button(janela, width=10, text="PLAY",    command=player.reproduzir)
bt_pause   = Button(janela, width=10, text="PAUSAR",  command=player.pausar)
bt_stop    = Button(janela, width=10, text="PARAR",   command=player.parar)
bt_return  = Button(janela, width=10, text="RETOMAR", command=player.retomar)

bt_play.place   (x=10,  y=0)
bt_pause.place  (x=110, y=0)
bt_stop.place   (x=210, y=0)
bt_return.place (x=310, y=0)

janela.geometry("1280x720+450+350")
janela.mainloop()
