#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import androidhelper

droid = androidhelper.Android()
message = droid.dialogGetInput('Falador', 'Fale alguma coisa?').result
droid.ttsSpeak(message)
