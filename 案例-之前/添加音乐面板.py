from tkinter import *
import pathlib
import sqlite3
import tkinter.messagebox as tm

music = ['here with you', '500 hundreds miles']

root = Tk()  # 创建窗口对象的背景色
root.geometry('800x500')
root.title('音乐')
Label(root, text='Add Music:', font=('Arial', 12), width=50, height=2).place(x=0, y=0)
Label(root, text='Music Library:', font=('Arial', 12), width=50, height=2).place(x=400, y=0)
Label(root, text='Song Name:', font=('Arial', 12), width=10, height=2).place(x=0, y=50)
musicName = Entry(root, show=None, font=('Arial', 14)).place(x=100, y=60)
Label(root, text='Length:', font=('Arial', 12), width=10, height=2).place(x=0, y=100)
musicLength = Entry(root, show=None, font=('Arial', 14)).place(x=100, y=110)

music_id = 0


def submit():
    # name = musicName.get(),
    # length = musicLength.get()
    conn = sqlite3.connect("test.db")  # 打开或创建数据库
    c = conn.cursor()  # 获取游标
    sql1 = '''
       insert into music (id, SongName, SongLength) 
       values(,music_id,name,length)
    '''
    c.execute(sql1)  # 执行sql语句
    conn.commit()  # 提交数据库操作

    getLength = '''
       select songName,SongLength from music
    '''
    lengthList = c.execute(getLength)  # 执行sql语句，有返回值
    total = 0.0
    k = 0
    for row in lengthList:
        music[k] = row[0] + "     " + row[1]
        total += row[1]
        k = k + 1

    averAge = total / k

    conn.commit()  # 提交数据库操作
    conn.close()


Button(root, text='Submit', font=('Arial', 12), width=10, height=1, command=submit).place(x=10, y=150)
musicList = Listbox(root, width=40, height=10)
musicList.place(x=400, y=50)
for item in music:  # 第二个小部件插入数据
    musicList.insert(0, item)
averLength = Label(root, text='Average Length:', font=('Arial', 12), width=15, height=2)
averLength.place(x=400, y=250)
averLength = Label(root, text=20, font=('Arial', 12), width=15, height=2)
averLength.place(x=600, y=250)
root.mainloop()  # 进入消
