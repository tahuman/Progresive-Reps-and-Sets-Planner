#randomで生成
import random
import tkinter as tk
#list[random.randint(1,7)]
#print(list[0])
def logic():
    print("バーベルなら1、ダンベルなら２、マシンなら3を入力してください")
    trainingEquipment = int(input())

    if trainingEquipment == 1:
        weight = random.randint(50,90)
        print("バーベルの重さは" + str(weight))
    elif trainingEquipment == 2:
        weight = random.randint(8,24)
        print("ダンベルの重さは" + str(weight))
    elif trainingEquipment == 3:
        weight = random.randint(50,90)
        print("マシンの重さは" + str(weight))
    else:
        print("入力値間違ってるよ。")

    number = [random.randint(1,6) for i in range(2)]
    print('回数：' + str(number[0]))
    print('セット数' + str(number[1]))

"""
root = tk.Tk()
root.title("トレーニング回数ルーレット")
root.geometry("400x400")

# ラベル
lbl = tk.Label(text='トレーニング器具 ※ バーベル or ダンベル or マシン')
lbl.place(x=30, y=70)

# テキストボックス、入力
txt = tk.Entry(width=20)
txt.place(x=90, y=70)

#テキストボックスの値が入力されたら回数とセット数を表示

#テキストボックスの値を消す

root.mainloop()
"""
