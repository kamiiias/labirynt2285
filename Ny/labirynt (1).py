import pygame
w = 700
h = 500
pygame.mixer.init()
sound = pygame.mixer.Sound("music.ogg")
pygame.mixer.music.load("music.ogg")
wiin = pygame.mixer.Sound("twise.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
window = pygame.display.set_mode((w,h))
pygame.display.set_caption("Лабіринт")
background = pygame.transform.scale(pygame.image.load("bg.jpg"),(w,h))
won = pygame.transform.scale(pygame.image.load("won.png"),(w,h))
pygame.font.init()
font1 = pygame.font.Font(None, 60)
win = font1.render("You win!", True, (0, 0, 0))
class Player(pygame.sprite.Sprite):
    def __init__ (self, width, height, player_image,player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image),(width,height))
        self.speed = player_speed
        self.width = width
        self.height = height
        self.rect = self.image.get_rect() # Створити рамку навколо картинки спрайта
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self): # Функція для того щоб намалювати спрайт на екрані
        window.blit(self.image, (self.rect.x, self.rect.y))


class Enemy (Player):
    direction = "right"
    def update(self):
        if self.rect.x <= 230:
            self.direction = "right"
        if self.rect.x >= 600:
            self.direction  = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed
class Hero (Player):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y <= 500:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x <= 700:
            self.rect.x += self.speed

class Wall(pygame.sprite.Sprite): #клас стіни
    def __init__(self,width,height,color,wall_x, wall_y):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((color))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self): #метод малювання стіни
        window.blit(self.image, (self.rect.x, self.rect.y)) #оновлюємо вікно і 

w1 = Wall(20,200,(250, 250, 250),100,300)
w2 = Wall(200,20,(250, 250, 250),100, 300)
w3 = Wall(20,200,(250, 250, 250),300,120)
w4 = Wall(200,20,(250, 250, 250),300, 110)
w5 = Wall(20,200,(250, 250, 250),480, 1)
w6 = Wall(20,200,(250, 250, 250),480, 120)
w7 = Wall(20,70,(250, 250, 250),480, 320)
w8 = Wall(200,20,(250, 250, 250),0, 120)
w9 = Wall(20,140,(250, 250, 250),200, 0)

#20 ширина стіни, 200 - висота стіни, (130, 183, 254) - колір, 100 - координати стіни по x, 300 - координати по y




hero = Hero(42,93,"hero.png", 20, 320, 5)
enemy = Enemy(100,100,"enemy.png", 500, 300, 4)
skarb = Player(150,150,"skarb.png", 500, 30, 0)
zaec = Player(80,80,"zaec.png", 330, 10, 0)
game = True
finish = False
clock = pygame.time.Clock()
FPS = 60
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    if finish != True: 
        window.blit(background, (0,0))    
        hero.update() #змушує рухатись головного героя 
        enemy.update()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        hero.reset() #оновлюємо головного героя на сцені   
        enemy.reset()
        skarb.reset()
        zaec.reset()
        if pygame.sprite.collide_rect(hero, w1) or pygame.sprite.collide_rect(hero, w2) or pygame.sprite.collide_rect(hero, w3) or pygame.sprite.collide_rect(hero, w4) or pygame.sprite.collide_rect(hero, w5) or pygame.sprite.collide_rect(hero, w6) or pygame.sprite.collide_rect(hero, w7) or pygame.sprite.collide_rect(hero, w8) or pygame.sprite.collide_rect(hero, w9):
            hero.rect.x = 20
            hero.rect.y = 320
        if pygame.sprite.collide_rect(hero, enemy) or pygame.sprite.collide_rect(hero, enemy) or pygame.sprite.collide_rect(hero, enemy) or pygame.sprite.collide_rect(hero, enemy) or pygame.sprite.collide_rect(hero, enemy) or pygame.sprite.collide_rect(hero, enemy) or pygame.sprite.collide_rect(hero, enemy) or pygame.sprite.collide_rect(hero, enemy) or pygame.sprite.collide_rect(hero, enemy):
            hero.rect.x = 20
            hero.rect.y = 320
        if pygame.sprite.collide_rect(hero, zaec):
            w4.rect.x = 1000
            w4.rect.y = 1000
            zaec.rect.x = 1000
            zaec.rect.y = 1000
        if pygame.sprite.collide_rect(hero, skarb):
            FPS = 1
            window.blit(won, (0,0))
            window.blit(win, (50, 50))
            finish = True
            pygame.mixer.music.load("twise.ogg")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
            

    pygame.display.update()
    clock.tick(FPS)
