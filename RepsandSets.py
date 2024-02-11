import random
import tkinter as tk

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

logic()