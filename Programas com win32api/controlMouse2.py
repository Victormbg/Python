import pyautogui
''''
pyautogui.moveTo(100, 150)
pyautogui.moveRel(0, 10)
pyautogui.dragTo(100, 150)
pyautogui.dragRel(0, 10)
'''

pyautogui.hotkey('browserhome', interval=0.25)
pyautogui.write('w', interval=0.25)
pyautogui.press(['enter'])
pyautogui.moveTo(100, 300, duration=20)
pyautogui.click()
pyautogui.write('RUANNNN  TU VAI SE DA MAL NAO SOU EU QUE TO ESCREVENDO E ESSA BIBLIOTECA AQUI KKKK ', interval=0.5)
pyautogui.press(['enter'])

#pyautogui.press(['alt''tab'])
#wpyautogui.write('RUANNNN  TU VAI SE DA MAL NAO SOU EU QUE TO ESCREVENDO E ESSA BIBLIOTECA AQUI KKKK ', interval=0.25)
