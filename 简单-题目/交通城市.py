import numpy as np
import copy
from datetime import datetime
#定位元素0的位置
def local(S0):
    a = np.array(S0)
    i,j = np.where(a == 0)
    return i[0],j[0]
def right_(S0):
    i,j =  local(S0)
    arr = copy.deepcopy(S0)
    if j in (0,len(S0)-2):
        arr[i][j], arr[i][j+1] = arr[i][j+1],arr[i][j]
        return arr
def left_(S0):
    i,j =  local(S0)
    arr = copy.deepcopy(S0)
    if j in (1,len(S0)-1):
        arr[i][j],arr[i][j-1] = arr[i][j-1],arr[i][j]
    return arr
def up_(S0):
    i,j =  local(S0)
    arr = copy.deepcopy(S0)
    if i in (1,len(S0)-1):
        arr[i][j],arr[i-1][j] = arr[i-1][j],arr[i][j]
        return arr
def down_(S0):
    i,j =  local(S0)
    arr = copy.deepcopy(S0)
    if i in (0,len(S0)-2):
        arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j]
        return arr
class Node:
    def __init__(self,data,level,parent,score):
        self.data=data
        self.level=level
        self.parent = parent
        self.score = score
def Atest_g(S0,Sg):
    S1 = np.reshape(S0,(3,3))
    Sg = np.reshape(Sg,(3,3))
    g = 0
    for i in range(len(S1)):
        for j in range(len(S1[i])):
            if S1[i][j] != Sg[i][j] and S1[i][j] != 0:
                g += 1
    return g
def Asort(open_):
    for i in range(len(open_)):
        for j in range(len(open_)-1):
#             print(open_[i])
            if open_[i].score<open_[j].score:
                open_[i],open_[j] = open_[j],open_[i]
    return open_
if __name__ ==  "__main__":

    # S0 = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    # Sg = [[4,1,2,3],[0,5,6,7],[8,9,10,11],[12,13,14,15]]

    # S0 = [[0,1],[2,3]]
    # Sg = [[3,1],[2,0]]

    S0=[[2,8,3],[1,6,4],[7,0,5]]
    Sg=[[1,2,3],[8,0,4],[7,6,5]]

    Node0 = Node(S0,0,"None",0)
    # print(Node0.data)

    deep_level = 5

    open_ = [Node0]
    close = []

    # level = 1

    step = 0

    start = datetime.now()
    while len(open_) > 0:
        step = step + 1
        n = open_.pop(0)
    #     print("1111",Node0.data)
        close.append(n)
        # 如果找到目标结果，则输出其最优路径。
        if n.data == Sg:
            print( n.data,'true','搜索完毕！')
            result = []
            result.append(n)
            while n.parent!="None":
                result.append(n.parent)
                n = n.parent
            for j in range(len(result)):
                print(str(j)+"->")
                result_0 = result.pop(-1)
                print(result_0.data)
            print("------------结束搜索-----------")
            break
        else:
    #         if n.level<=int(deep_level):
                local(n.data)
                Up = up_(n.data)
                if Up not in [open_[i].data for i in range(len(open_))] and Up not in [close[i].data for i in range(len(close))] and Up is not None:
                    Node0 = Node(Up,n.level+1,n,(Atest_g(Up,Sg)+n.level+1))
                    open_.append(Node0)

                Down = down_(n.data)
                if Down not in [open_[i].data for i in range(len(open_))] and Down not in [close[i].data for i in range(len(close))] and Down is not None:
                    Node0 = Node(Down,n.level+1,n,(Atest_g(Down,Sg)+n.level+1))
                    open_.append(Node0)

                Left = left_(n.data)
                if Left not in [open_[i].data for i in range(len(open_))] and Left not in [close[i].data for i in range(len(close))] and Left is not None:
                    Node0 = Node(Left,n.level+1,n,(Atest_g(Left,Sg)+n.level+1))
                    open_.append(Node0)

                Right = right_(n.data)
                if Right not in [open_[i].data for i in range(len(open_))] and Right not in [close[i].data for i in range(len(close))] and Right is not None:
                    Node0 = Node(Right,n.level+1,n,(Atest_g(Right,Sg)+n.level+1))
                    open_.append(Node0)
        Asort(open_)
        print("第"+ str(step)+"次查找,中间项为：",Node0.data,"深度为:",Node0.level,"估价值为：",Node0.score)
    end = datetime.now()

    print('共耗时:', end - start)