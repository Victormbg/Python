from gtts import gTTS
import os
voz = gTTS('''Olá, tudo bem?
           Em que posso ajuda-lo
           eu sou legal''', lang ="pt")
voz.save("voz.mp3")
