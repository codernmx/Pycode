import requests
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser

def getHTMLText(url):
    try:
        kv = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53",
            "Cookie": 'UOR=,,login.sina.com.cn; ALF=1666445729; SCF=AscEHVE2sTV05zTwYj5M7tduM7Zz3ktqPi21c2dTBB0sGFGcFIldixokcQ1yN8xFwVW-ywKnUt3rugqpWgzVXsE.; SINAGLOBAL=7267933806159.166.1634959444829; SUB=_2AkMW3d0wf8NxqwJRmPERzW_nbIx0yQ7EieKggSzrJRMxHRl-yT9jqhdftRB6PV3z3z21fp5a3CkZMXy5gZcyj15_nia0; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W56DO1wnAXX89yZnIENST5-; _s_tentry=-; Apache=6131946571247.373.1639292770571; ULV=1639292770592:2:1:1:6131946571247.373.1639292770571:1634959444907'
        }
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"

def on_item_click(event):
    selected_index = listb.curselection()  # 获取当前选中的项的索引
    print(selected_index[0])
    # print(allInfo[selected_index[0]])
    webbrowser.open(allInfo[len(allInfo)-1-selected_index[0]]['href'])

url = "https://s.weibo.com/top/summary?cate=realtimehot"
html = getHTMLText(url)
soup = BeautifulSoup(html, 'html.parser')
sou = soup.find_all("td", class_='td-02')
allInfo = []
for i in range(len(sou) - 1, -1, -1):
    href = 'https://s.weibo.com' + sou[i].a['href']
    allInfo.append({
        "title":str(i + 1) + '.' + sou[i].a.string,
        "href":href
    })
root = Tk()
root.title("微博热搜排行榜")
screenWidth = root.winfo_screenwidth()  # 获取显示区域的宽度
screenHeight = root.winfo_screenheight()  # 获取显示区域的高度
width = 300  # 设定窗口宽度
height = 450  # 设定窗口高度
left = (screenWidth - width) / 2
top = (screenHeight - height) / 2
# 宽度x高度+x偏移+y偏移
# 在设定宽度和高度的基础上指定窗口相对于屏幕左上角的偏移位置
root.geometry("%dx%d+%d+%d" % (width, height, left, top))

# 创建一个列表框并添加数据
listb = Listbox(root, width=300, height=450)
for item in allInfo:
    listb.insert(0, item['title'])

listb.pack()

# 绑定点击事件处理函数到列表框
listb.bind("<ButtonRelease>", on_item_click)

root.mainloop()
