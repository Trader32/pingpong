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
            self.rect.y -= self.speed
        if keys_pressed[K_s]:
            self.rect.y += self.speed


class Player2(GameSprite):
    width = 100
    height =50
    def __init__(self, plair_imege, plair_x ,plair_y ,plair_speed):
       super().__init__(plair_imege, plair_x ,plair_y ,plair_speed)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]:
            self.rect.y += self.speed

#создай окно игры
window = display.set_mode((1000 ,700))
display.set_caption("пингпонг")
background = transform.scale(image.load('background.png'), (1000 , 700))
sprite1 = Player1('ufo.png', 1 , 75 ,10)
sprite2 = Player2('ufo.png', 900 , 75, 10)
ball = GameSprite('pngwing.com.png', 500 , 100, 3)
FPS = 60

x1 = 100
y1 = 300
x2 = 300
y2 = 300
events = event.get()
events[0].type

font.init()
font1 = font.Font(None, 100)

ball.speed_x = 4
ball.speed_y = 6
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:

        ball.rect.y += ball.speed_y
        ball.rect.x += ball.speed_x
    if ball.rect.y >= 655 or ball.rect.y <= 0:
        ball.speed_y *= -1
    if sprite.collide_rect(sprite1 , ball) or sprite.collide_rect(sprite2 , ball):
        ball.speed_x *= -1
            
    window.blit(background, (0 ,0))
    sprite1.reset()
    sprite1.update()
    sprite2.reset()
    sprite2.update()
    ball.reset()
    ball.update()

    display.update()
    if ball.rect.x >= 1000:
        Text1 = font1.render('1 игрок выйграл', True ,(255 ,10, 0))
        finish = True
        window.blit(Text1, (100, 200))
        display.update()
    if ball.rect.x <= 0:
        Text2 = font1.render('2 игрок выйграл', True ,(200 ,100, 0))
        finish = True
        window.blit(Text2, (100, 200))
        display.update()


    # if finish = True
    #     ball.rect.y = 300 
    #     ball.rect.x = 300 

    clock = time.Clock()
    clock.tick(FPS)
    display.update()



    