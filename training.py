import random

# 場所ごと
print("家なら1、ジムなら２を入力してください")
place = int(input())
print("=================================")

# 家：部位→各部位を関数にして呼び出す
if place == 1 :
    # 辞書でストレッチ、ヨガピラティス、上半身、下半身、体幹、インナーをランダムチョイスで出力
    choices_house_item_house= { 1:"ストレッチ", 2:"ヨガピラティス", 3:"上半身", 4:"下半身", 5:"体幹" ,6:"インナー"}
    # 回数
    print(random.choice(list(choices_house_item_house.values())))
    # 軽め、通常、追い込み、鬼、激鬼
    choices_house_strength_house= { 1:"軽め", 2:"通常", 3:"追い込み", 4:"鬼", 5:"激鬼" }
    strength = random.choice(list(choices_house_strength_house.values()))
    print(strength)
    # 各部位のトレーニングメニュー    
    if strength == "軽め":
        print("30秒+休憩10秒 : ６セット")
    elif strength == "通常":
        print("35秒+休憩10秒 : ６セット")
    elif strength == "追い込み":
        print("40秒+休憩10秒 : ６セット")
    elif strength == "鬼":
        print("45秒+休憩10秒 : ６セット")
    else:
        print("50秒+休憩10秒 : ６セット")
    # セット数
    set_number = random.randint(1,6)


# ジム：部位
elif place == 2 :
# 辞書で腕、肩、胸、背中、腹、足をランダムチョイスで出力
    choices_house_item_gym= { 1:"胸", 2:"肩", 3:"胸", 4:"背中", 5:"腹" ,6:"足"}

    # 回数
    gym = random.choice(list(choices_house_item_gym.values()))
    print(gym)

    # 軽め、通常、追い込み、鬼、激鬼
    choices_house_strength_gym= { 1:"軽め", 2:"通常", 3:"追い込み", 4:"鬼", 5:"激鬼" }
    strength = random.choice(list(choices_house_strength_gym.values()))
    print(strength)
    
    # 各部位のトレーニングメニュー 
    # ダンベル、バーベル、、ケーブル、マシンの選択
    if gym == '腕':
        # ダンベル、バーベル、、ケーブル、マシンの選択
        ude_choice_implement= {1:"ダンベル", 2:"バーベル", 3:"マシン", 4:"ケーブル"}
        ude_choice = random.choice(list(ude_choice_implement.values()))
        print(ude_choice)
        # ダンベル、バーベル、マシンのメニュー
        if ude_choice == 'ダンベル':
            print("リストカール	リバースリストカール	アームカール	捻りアームカール	ハンマーカール	コンセントレーションカール	キックバッグ	フレンチプレス	ライイングトライセプスエクステンション	テイトプレス")
        elif ude_choice == 'バーベル':
            print("リストカール	リバースリストカール	アームカール	プッシュダウン	スカルクラッシャー	JMプレス")
        else:
            print("なし")

    elif gym == '肩' :
        # ダンベル、バーベル、、ケーブル・マシン（なし）の選択
        shoulder_choice_implement= {1:"ダンベル", 2:"バーベル", 3:"マシン", 4:"ケーブル"}
        shoulder_choice = random.choice(list(shoulder_choice_implement.values()))
        print(shoulder_choice)
        # ダンベル、バーベル、マシンのメニュー
        if shoulder_choice == 'ダンベル':
            print("ショルダープレス	フロントレイズ	サイドプレス	アップライトローイング	シュラッグ")
        elif shoulder_choice == 'バーベル':
            print("ショルダープレス	アップライトローイング	シュラッグ")
        else:
            print("やり直し")

    elif gym == '背中' :
        # ダンベル、バーベル、、ケーブル、マシン(なし)の選択
        ude_choice_implement= {1:"ダンベル", 2:"バーベル", 3:"ケーブル"}
        ude_choice = random.choice(list(ude_choice_implement.values()))
        print(ude_choice)
        # ダンベル、バーベル、マシンのメニュー
        if ude_choice == 'ダンベル':
            print("ダンベルローイング")
        elif ude_choice == 'バーベル':
            print("デットリフト（スタンダード・ワイ・ナロー）ペントオーバーローイング")
        else:
            print("ラットプルダウン ケーブルローイング ")

    elif gym == '胸' :    
        # ダンベル、バーベル、、ケーブル、マシンの選択
        ude_choice_implement= {1:"ダンベル", 2:"バーベル", 3:"マシン", 4:"ケーブル"}
        ude_choice = random.choice(list(ude_choice_implement.values()))
        print(ude_choice)
        # ダンベル、バーベル、マシンのメニュー
        if ude_choice == 'ダンベル':
            print("なし")
        elif ude_choice == 'バーベル':
            print("ベンチプレス	（スタンダード・ワイド・ナロー）インクラインベンチプレス（スタンダード・ワイド・ナロー）デクラインベンチプレス（スタンダード・ワイド・ナロー）")
        else:
            print("ケーブルプレス（上・中・下）")


    elif gym == '腹' :
        # ダンベル、バーベル、、ケーブル、マシンの選択
        ude_choice_implement= {1:"ダンベル", 2:"バーベル", 3:"マシン", 4:"ケーブル"}
        ude_choice = random.choice(list(ude_choice_implement.values()))
        print(ude_choice)
        # ダンベル、バーベル、マシンのメニュー
        if ude_choice == 'ダンベル':
            print("休み")
        elif ude_choice == 'バーベル':
            print("休み")
        else:
            print("休み")

    else :
        # 足
        # ダンベル、バーベル、、ケーブル、マシンの選択
        ude_choice_implement= {1:"ダンベル", 2:"バーベル", 3:"マシン", 4:"ケーブル"}
        ude_choice = random.choice(list(ude_choice_implement.values()))
        print(ude_choice)
        # ダンベル、バーベル、マシンのメニュー
        if ude_choice == 'ダンベル':
            print("スクワット（スタンダード・片足）ランジ（フロント・バッグ・サイド）カーフレイズ（スタンディング・バッグスタンディング）")
        elif ude_choice == 'バーベル':
            print("スクワット（スタンダード・片足）ランジ（フロント・バッグ・サイド）カーフレイズ（スタンディング・バッグスタンディング）")
        else:
            print("")

    # 強度
    if strength == "軽め":
        print("60% 15回,70% 10回,80% 5回")
    elif strength == "通常":
        print("70% 10回,80% 8回,90% 5回")
    elif strength == "追い込み":
        print("80% 10回,90% 8回,100% 3回")
    elif strength == "鬼":
        print("100%,90%,80%")
        print("限界まで")
    else:
        print("100%,95%,90%,85%,80%")
        print("限界まで")
    # セット数
    set_number = random.randint(1,6)
    print(set_number , end='セット''\n')
    print("追い込めアホ") 

else:
    print("値入れ直してちょうだい")