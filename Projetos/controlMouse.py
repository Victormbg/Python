import win32api, win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,100,100)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,100,100)

click(100,100)