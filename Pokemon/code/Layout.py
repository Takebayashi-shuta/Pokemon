import os
import pygame
import Monsters as ms

pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 50)

# ポケモンフォルダのパス//////////////////////////////////////////////////////////////////////////////////
image_folder = os.path.join(os.getcwd(), "images","Pokemon")

# キャラクターの画像を読み込む
Pikatyu_image = pygame.image.load(os.path.join(image_folder, "Pikatyu.png"))
Ibui_image = pygame.image.load(os.path.join(image_folder, "Ev.png"))

# キャラクターの画像の大きさを調整する
Pikatyu_image = pygame.transform.scale(Pikatyu_image, (500, 500))
Ibui_image = pygame.transform.scale(Ibui_image, (300, 300))

# キャラクターの初期位置
Ally_x, Ally_y = 80, 50
Enemy_x,Enemy_y = 450,50

# Backgroundフォルダのパス////////////////////////////////////////////////////////////////////////////////////
image_folder = os.path.join(os.getcwd(), "images","Background")

# 背景の画像を読み込む
background_image = pygame.image.load(os.path.join(image_folder, "Background.jpg"))

#背景の画像の大きさを調整する
background_image = pygame.transform.scale(background_image, (800, 600))

#名前とテキストフォルダのパス
image_folder = os.path.join(os.getcwd(), "images","name")
Ally_name = pygame.image.load(os.path.join(image_folder, "Ally_name.png"))
Enemy_name = pygame.image.load(os.path.join(image_folder, "Enemy_name.png"))

Ally_name = pygame.transform.scale(Ally_name, (770, 500))
Enemy_name = pygame.transform.scale(Enemy_name, (750, 600))

Ally_name_posx =30
Ally_name_posy = 70
Enemy_name_posx = 0
Enemy_name_posy = 50
#HPBarの表示/////////////////////////////////////////////////////////////////////////////////
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp

    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0

    def heal(self, amount):
        self.current_hp += amount
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

    def draw_hp_bar(self, screen, x, y, width, height):
        hp_percentage = self.current_hp / self.max_hp
        bar_fill_width = int(width * hp_percentage)
        pygame.draw.rect(screen, (0, 255, 0), (x, y, bar_fill_width, height))  # 緑色のバー
        pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height), 2)  # 枠線

# キャラクターの作成
Ally_HpB = Character(name=ms.Pikatyu.name, hp=ms.Pikatyu.hp)
Allytext_name = font.render(ms.Pikatyu.name, True, (0, 0, 0))  # 白色のテキスト

#Text

text = font.render("あうるがあうるが", True,(250,250,250))
textp = (80,450)


