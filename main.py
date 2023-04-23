from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    width = 50
    height =50
    def __init__(self, plair_imege, plair_x ,plair_y ,plair_speed):
        super().__init__()
        self.image = transform.scale(image.load(plair_imege), (self.width , self.height))
        self.speed = plair_speed
        self.rect = self.image.get_rect()
        self.rect.x = plair_x
        self.rect.y = plair_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player1(GameSprite):
    width = 100
    height =50
    def __init__(self, plair_imege, plair_x ,plair_y ,plair_speed):
       super().__init__(plair_imege, plair_x ,plair_y ,plair_speed)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -= 5
        if keys_pressed[K_s]:
            self.rect.y += 5


class Player2(GameSprite):
    width = 100
    height =50
    def __init__(self, plair_imege, plair_x ,plair_y ,plair_speed):
       super().__init__(plair_imege, plair_x ,plair_y ,plair_speed)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT]:
            self.rect.y -= 5
        if keys_pressed[K_DOWN]:
            self.rect.y += 5

#создай окно игры
window = display.set_mode((700 ,500))
display.set_caption("пингпонг")
background = transform.scale(image.load('background.png'), (1000 , 500))
sprite1 = Player1('ufo.png', 1 , 75 ,5)
sprite2 = Player2('ufo.png', 500 , 75, 5)
ball = GameSprite('pngwing.com.png', 250 , 100, 3)
FPS = 60

x1 = 100
y1 = 300
x2 = 300
y2 = 300
events = event.get()
events[0].type


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            # if ball.speed.y = -500 or ball.speed.y = 0
            #     speed.y * -1
            # if sprite.collide_rect(sprite1 , ball)
            #     sprite.collide_rect(sprite2 , ball)
            #     s
        window.blit(background, (0 ,0))

        sprite1.reset()
        sprite1.update()
        sprite2.reset()
        sprite2.update()
        ball.reset()
        ball.update()

    clock = time.Clock()
    clock.tick(FPS)

    clock = time.Clock()
    clock.tick(FPS)
    display.update()