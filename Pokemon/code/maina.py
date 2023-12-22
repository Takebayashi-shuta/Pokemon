import pygame as pg
import sys
import random
import time
import Layout as lo
import Monsters as ms

# 初期化
pg.init()

# 画面サイズ
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pokemon")

# 色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# ゲームステートの基底クラス
class GameState:
    def __init__(self):
        self.player_x = WIDTH // 2
        self.player_y = HEIGHT // 2
        self.last_transition_time = time.time()
        self.transition_interval = random.uniform(1, 50)  # ランダムな時間で遷移

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def update(self):
        pass

    def draw(self, screen):
        pass

# ゲーム画面
class GameScreen(GameState):
    def __init__(self):
        super().__init__()
        self.transition_probability = 0.01  # 1%の確率で遷移

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.player_y -= 5
        if keys[pg.K_s]:
            self.player_y += 5
        if keys[pg.K_a]:
            self.player_x -= 5
        if keys[pg.K_d]:
            self.player_x += 5

        # 画面外にプレイヤーが出ないように制御
        self.player_x = max(0, min(self.player_x, WIDTH))
        self.player_y = max(0, min(self.player_y, HEIGHT))

        # ランダムに戦闘画面に遷移
        if random.random() < self.transition_probability:
            return FightScreen()

    def draw(self, screen):
        screen.fill(WHITE)
        pg.draw.circle(screen, GREEN, (int(self.player_x), int(self.player_y)), 20)

# 戦闘画面
class FightScreen(GameState):
    def __init__(self):
        super().__init__()

    def update(self):
        
       # 戦闘画面の更新処理をここに追加
        pass
        
    def draw(self, screen):
        # 戦闘画面の描画処理をここに追加
        # 背景の描画
        screen.blit(lo.background_image, (0, 0))

        # キャラクターの描画
        screen.blit(lo.Pikatyu_image, (lo.Ally_x, lo.Ally_y))
        screen.blit(lo.Ibui_image, (lo.Enemy_x,lo.Enemy_y))

        #TextPの描画
        pg.draw.rect(screen, (0,0,0), (50,420,700,150))
        screen.blit(lo.text, (lo.textp))

        #キャラクターの名前の描画
        screen.blit(lo.Ally_name, (lo.Ally_name_posx, lo.Ally_name_posy))
        screen.blit(lo.Enemy_name, (lo.Enemy_name_posx, lo.Enemy_name_posy))
        screen.blit(lo.Allytext_name,(500,330))
        # キャラクターのHPバーの描画
        lo.Ally_HpB.draw_hp_bar(screen, 500, 380, 200, 20)
        pass

# ゲームのメインループ
current_state = GameScreen()

while True:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    current_state.handle_events(events)
    new_state = current_state.update()

    if new_state is not None:
        current_state = new_state

    screen.fill(WHITE)
    current_state.draw(screen)

    pg.display.flip()
    pg.time.Clock().tick(60)
