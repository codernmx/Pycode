# @Time : 2021/10/27 22:19
# @Author : VX:Until_Day_Break
# @SoftWare : PyCharm
from tkinter import *
# import tkMessageBox
# import tkinter.messagebox

def getInput(title, message):
    def return_callback(event):
        print('quit...')
        root.quit()
    def close_callback():
        messagebox.showinfo('message', 'no click...')
    root = Tk(className=title)
    root.wm_attributes('-topmost', 1)
    screenwidth, screenheight = root.maxsize()
    width = 300
    height = 100
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)
    root.resizable(0, 0)
    lable = Label(root, height=2)
    lable['text'] = message
    lable.pack()
    entry = Entry(root)
    entry.bind('<Return>', return_callback)
    entry.pack()
    entry.focus_set()
    root.protocol("WM_DELETE_WINDOW", close_callback)
    root.mainloop()
    str = entry.get()
    root.destroy()
    return str
print(getInput('5555','55'))