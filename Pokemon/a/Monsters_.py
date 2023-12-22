import os
import pygame as pg
#技威力
破壊光線 = 150
十万ボルト = 90
逆鱗 = 120
かめはめ波 = 300

skill = [破壊光線,十万ボルト,逆鱗,かめはめ波]

class Monsters:
    #ステータス
    def __init__(self, name, hp, ap, cp, bp, dp, sp, skl_1, skl_2, skl_3, skl_4):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.cp = cp
        self.bp = bp
        self.dp = dp
        self.sp = sp
        self.skl_1 = skill[skl_1]
        self.skl_2 = skill[skl_2]
        self.skl_3 = skill[skl_3]
        self.skl_4 = skill[skl_4]
        
# ポケモンフォルダのパス//////////////////////////////////////////////////////////////////////////////////
image_folder = os.path.join(os.getcwd(), "images","Pokemon")

# キャラクターの画像を読み込む
Pikatyu_image = pg.image.load(os.path.join(image_folder, "Pikatyu.png"))
Ibui_image = pg.image.load(os.path.join(image_folder, "Ev.png"))

# キャラクター情報
Pikatyu_info = Monsters('Pika', 100, 50, 30, 20, 40, 25, 0, 1, 2, 3)
Ibui_info = Monsters('Ev', 120, 60, 35, 25, 50, 30, 0, 1, 2, 3)

# それぞれの情報をペアで持つ
Pikatyu = (Pikatyu_info, Pikatyu_image)
Ibui = (Ibui_info, Ibui_image)