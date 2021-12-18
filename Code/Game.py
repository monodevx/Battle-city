import random
import pygame

pygame.init()
BLACK = (0, 0, 0)

enemies = 2
width = 512
height = 448
clock = pygame.time.Clock()
stage = 0
FPS = 60
speed = 15
score = 0
main_tank = pygame.image.load("../Sprites/Tank/TankUp.png")
enemy_tank = pygame.image.load("../Sprites/Tank/Enemy.png")
bullet = pygame.image.load("../Sprites/Tank/Bullet.png")
tile_block = pygame.image.load("../Sprites/Tile/Default block.png")
bullet_e = pygame.image.load("../Sprites/Tank/Bullet.png")
eagle = pygame.image.load("../Sprites/Tile/Eagle.png")
eagle = pygame.image.load("../Sprites/Tile/Bush.png")
window = pygame.display.set_mode((width, height))
tank_pos = (0, 0)
enemy_tank_pos = (0, 0)
rot = 000
e_rot = 0
timer = 0
timer_s = 0
timer_r = 0
rand = 0
shoot_r = 0
tile = [
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "x", "_", "x", "_", "_", "_", "_", "_", "x", "_", "x", "_"],
    ["_", "x", "_", "x", "_", "x", "_", "x", "_", "x", "_", "x", "_"],
    ["_", "x", "_", "x", "_", "x", "_", "x", "_", "x", "_", "x", "_"],
    ["_", "x", "_", "x", "_", "x", "_", "x", "_", "x", "_", "x", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "X", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "x", "x", "x", "_", "_", "_", "_", "_"],
    ["_", "x", "_", "X", "_", "x", "_", "x", "_", "x", "_", "x", "_"],
    ["_", "x", "_", "x", "_", "_", "_", "_", "_", "x", "_", "x", "_"],
    ["_", "x", "_", "x", "_", "x", "x", "x", "_", "x", "_", "x", "_"],
    ["_", "_", "_", "_", "_", "x", "_", "x", "_", "_", "_", "_", "_"],
    ]
tile2 = [
        ["b", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "b"],
        ["_", "x", "x", "x", "_", "x", "_", "x", "_", "x", "x", "x", "_"],
        ["_", "x", "b", "x", "_", "x", "_", "x", "_", "x", "b", "x", "_"],
        ["_", "x", "b", "x", "_", "x", "_", "x", "_", "x", "b", "x", "_"],
        ["_", "x", "b", "x", "_", "x", "_", "x", "_", "x", "b", "x", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "b", "b", "b", "b", "b", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "b", "_", "b", "_", "b", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "x", "b", "x", "_", "_", "_", "_", "_"],
        ["_", "x", "_", "X", "_", "x", "_", "x", "_", "x", "_", "x", "_"],
        ["_", "x", "_", "x", "_", "_", "_", "_", "_", "x", "_", "x", "_"],
        ["_", "x", "_", "x", "_", "x", "x", "x", "_", "x", "_", "x", "_"],
        ["b", "_", "_", "_", "_", "x", "_", "x", "_", "_", "_", "_", "b"],
        ]

def stage_1():
    global stage, tank1, eagle_group, bullet_group, enemy_bullet_group, player_group, enemy_group, tile_group, x_log, y_log, keystate
    global stage, collide, enemies, player_group, eagle_group, tile_group, enemy_group, tile2
    window.fill(BLACK)
    player_group.update()
    player_group.draw(window)
    eagle_group.update()
    eagle_group.draw(window)
    enemy_group.update()
    enemy_group.draw(window)
    bullet_group.update()
    bullet_group.draw(window)
    enemy_bullet_group.update()
    enemy_bullet_group.draw(window)
    tile_group.update()
    tile_group.draw(window)
    #window.blit(pygame.image.load("../Sprites/GUI/Border.png"), (0, 0))

    target = pygame.sprite.groupcollide(player_group, enemy_bullet_group, True, True)
    target_e = pygame.sprite.groupcollide(enemy_group, bullet_group, True, True)
    collide = pygame.sprite.groupcollide(tile_group, player_group, False, False)
    bullet_bullet = pygame.sprite.groupcollide(bullet_group, enemy_bullet_group, True, True)
    bullet_wall = pygame.sprite.groupcollide(bullet_group, tile_group, True, True)
    e_bullet_wall = pygame.sprite.groupcollide(enemy_bullet_group, tile_group, True, True)
    eagle_bullet = pygame.sprite.groupcollide(enemy_bullet_group, eagle_group, True, True)
    if target_e:
        enemies -= 1
    if enemies == 0:


        player = Player()
        player_group = pygame.sprite.Group()
        player_group.add(player)
        eagle = Eagle()
        eagle_group = pygame.sprite.Group()
        eagle_group.add(eagle)
        enemy = Enemy()
        enemy1 = Enemy()
        enemy2 = Enemy()
        enemy_group = pygame.sprite.Group()
        enemy_group.add(enemy,enemy1,enemy2)


        tile_group = pygame.sprite.Group()


        bullet_group = pygame.sprite.Group()
        enemy_bullet_group = pygame.sprite.Group()
        for i in range(0,13):
            y_log = i*32
            for j in range(0,13):
                if tile2[i][j] == "x":
                    x_log = j*32
                    unit = Tile()
                    tile_group.add(unit)
        stage = 2
    elif target:
        stage = 0
    if eagle_bullet:
        stage = 0
    pygame.display.update()

def stage_2():
    global stage, collide, enemies, player_group, enemy_group, eagle_group, bullet_group, enemy_bullet_group, tile2_group
    window.fill(BLACK)
    player_group.update()
    player_group.draw(window)
    eagle_group.update()
    eagle_group.draw(window)
    enemy_group.update()
    enemy_group.draw(window)
    bullet_group.update()
    bullet_group.draw(window)
    enemy_bullet_group.update()
    enemy_bullet_group.draw(window)
    tile_group.update()
    tile_group.draw(window)
    #window.blit(pygame.image.load("../Sprites/GUI/Border.png"), (0, 0))
    target = pygame.sprite.groupcollide(player_group, enemy_bullet_group, True, True)
    target_e = pygame.sprite.groupcollide(enemy_group, bullet_group, True, True)
    collide = pygame.sprite.groupcollide(tile_group, player_group, False, False)
    bullet_bullet = pygame.sprite.groupcollide(bullet_group, enemy_bullet_group, True, True)
    bullet_wall = pygame.sprite.groupcollide(bullet_group, tile_group, True, True)
    e_bullet_wall = pygame.sprite.groupcollide(enemy_bullet_group, tile_group, True, True)
    eagle_bullet = pygame.sprite.groupcollide(enemy_bullet_group, eagle_group, True, True)
    if target_e:
        enemies -= 1
    if enemies == 0:
        stage = 0
    elif target:
        stage = 0
    if eagle_bullet:
        stage = 0
    pygame.display.update()

def menu():
    global stage, tank1, eagle_group, bullet_group, enemy_bullet_group, player_group, enemy_group, tile_group, x_log, y_log, keystate
    window.fill(BLACK)
    keystate = pygame.key.get_pressed()
    #window.blit(pygame.image.load("../Sprites/GUI/Interface.png"), (45, 0))
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] > 205 and mouse_pos[0] < 340 or keystate[pygame.K_SPACE]:
        if mouse_pos[1] > 240 and mouse_pos[1] < 260 or keystate[pygame.K_SPACE]:
            #window.blit(pygame.image.load("../Sprites/GUI/Interface2.png"), (45, 0))
            if event.type == pygame.MOUSEBUTTONDOWN or keystate[pygame.K_SPACE]:
                player = Player()
                player_group = pygame.sprite.Group()
                player_group.add(player)
                eagle = Eagle()
                eagle_group = pygame.sprite.Group()
                eagle_group.add(eagle)
                enemy = Enemy()
                enemy1 = Enemy()
                enemy_group = pygame.sprite.Group()
                enemy_group.add(enemy,enemy1)


                tile_group = pygame.sprite.Group()


                bullet_group = pygame.sprite.Group()
                enemy_bullet_group = pygame.sprite.Group()
                for i in range(0,13):
                    y_log = i*32
                    for j in range(0,13):
                        if tile[i][j] == "x":
                            x_log = j*32
                            unit = Tile()
                            tile_group.add(unit)
                stage = 1
    pygame.display.update()

class Eagle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =eagle
        self.rect = self.image.get_rect()
        self.rect.x = 224
        self.rect.y  = 403

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_tank
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(13, 435)
        self.rect.y = 13
        self.rand = random.randint(1, 4)
        self.enemy_tank_pos = self.rect.center
        self.timer_r = 0
        self.timer_s = 0
    def update(self):
        global enemy_tank_pos, e_rot, rand, shoot_r, bull_e
        self.enemy_tank_pos = self.rect.center
        if pygame.sprite.spritecollide(self, tile_group, False):
            if self.rand == 1:
                self.rand = 2
            elif self.rand == 2:
                self.rand = 1
            elif self.rand == 3:
                self.rand = 4
            elif self.rand == 4:
                self.rand = 3

        if self.rand == 1:
            self.rect.x -= 1
            e_rot = -90
            self.image = pygame.transform.rotate(enemy_tank, 90)
        if self.rand == 2:
            self.rect.x += 1
            e_rot = 90
            self.image = pygame.transform.rotate(enemy_tank, -90)
        if self.rand == 3:
            self.rect.y -= 1
            e_rot = 0
            self.image = pygame.transform.rotate(enemy_tank, 0)
        if self.rand == 4:
            self.rect.y += 1
            e_rot = 180
            self.image = pygame.transform.rotate(enemy_tank, 180)

        if self.enemy_tank_pos[0] < 77:
            self.rand = 2
        if self.enemy_tank_pos[0] > width - 77:
            self.rand = 1
        if self.enemy_tank_pos[1] > height - 29:
            self.rand = 3
        if self.enemy_tank_pos[1] < 29:
            self.rand = 4

        if self.timer_r//FPS > 0.1:
            self.rand = random.randint(1, 4)
            self.timer_r = 0
        if self.timer_s//FPS > 0.2:
            shoot_r = random.randint(1, 2)
            self.timer_s = 0
        if shoot_r == 1:
            bull_e = EnemyBulet(e_rot, self.enemy_tank_pos)
            enemy_bullet_group.add(bull_e)
            shoot_r = 0
        self.timer_r += 1
        self.timer_s += 1

class Tile(pygame.sprite.Sprite):
    global Tile
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = tile_block
        self.rect = self.image.get_rect()
        self.rect.x = x_log + 32
        self.rect.y = y_log + 16

class Bush(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bush
        self.rect = self.image.get_rect()
        self.rect.x = x_log + 32
        self.rect.y = y_log + 16

class Player(pygame.sprite.Sprite):
    global Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = main_tank
        self.rect = self.image.get_rect()
        self.rect.x = 163
        self.rect.y = 403

    def update(self):
        global tank_pos, rot, timer, rand
        tank_pos = self.rect.center
        keystate = pygame.key.get_pressed()
        if pygame.sprite.spritecollide(self, tile_group, False):
            if keystate[pygame.K_a] and rot == -90:
                self.rect.x += 2
                self.image = pygame.transform.rotate(main_tank, 90)
            elif keystate[pygame.K_d] and rot == 90:
                self.rect.x -= 2
                self.image = pygame.transform.rotate(main_tank, -90)
            elif keystate[pygame.K_w] and rot == 0:
                self.rect.y += 2
                self.image = pygame.transform.rotate(main_tank, 0)
            elif keystate[pygame.K_s] and rot == 180:
                self.rect.y -= 2
                self.image = pygame.transform.rotate(main_tank, 180)
        else:
            if keystate[pygame.K_a] and tank_pos[0] > 45:
                self.rect.x -= 1
                rot = -90
                self.image = pygame.transform.rotate(main_tank, 90)
            elif keystate[pygame.K_d] and tank_pos[0] < width - 77:
                self.rect.x += 1
                rot = 90
                self.image = pygame.transform.rotate(main_tank, -90)
            elif keystate[pygame.K_w] and tank_pos[1] > 29:
                self.rect.y -= 1
                rot = 0
                self.image = pygame.transform.rotate(main_tank, 0)
            elif keystate[pygame.K_s] and tank_pos[1] < height - 29:
                self.rect.y += 1
                rot = 180
                self.image = pygame.transform.rotate(main_tank, 180)

        if keystate[pygame.K_SPACE] and timer//FPS > 1:
            bull = Bullet(rot)
            bullet_group.add(bull)
            timer = 0

class Bullet(pygame.sprite.Sprite):
    def __init__(self, rot):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet
        self.rect = self.image.get_rect()
        self.rect.x = tank_pos[0]
        self.rect.y = tank_pos[1]

        if rot == 0:
            self.speedy = -4
            self.speedx = 0
            self.image = pygame.transform.rotate(bullet, 0)
        if rot == 90:
            self.speedy = 0
            self.speedx = 4
            self.image = pygame.transform.rotate(bullet, -90)
        if rot == 180:
            self.speedy = 4
            self.speedx = 0
            self.image = pygame.transform.rotate(bullet, 180)
        if rot == -90:
            self.speedy = 0
            self.speedx = -4
            self.image = pygame.transform.rotate(bullet, 90)

    def update(self):
       self.rect.x += self.speedx
       self.rect.y += self.speedy

class EnemyBulet(pygame.sprite.Sprite):
    global e_rot, bullet_e
    def __init__(self, e_rot, tank_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_e
        self.rect = self.image.get_rect()
        self.rect.x = tank_pos[0]
        self.rect.y = tank_pos[1]

        if e_rot == 0:
            self.speedy = -4
            self.speedx = 0
            self.image = pygame.transform.rotate(bullet_e, 0)
        if e_rot == 90:
            self.speedy = 0
            self.speedx = 4
            self.image = pygame.transform.rotate(bullet_e, -90)
        if e_rot == 180:
            self.speedy = 4
            self.speedx = 0
            self.image = pygame.transform.rotate(bullet_e, 180)
        if e_rot == -90:
            self.speedy = 0
            self.speedx = -4
            self.image = pygame.transform.rotate(bullet_e, 90)

    def update(self):
       self.rect.x += self.speedx
       self.rect.y += self.speedy

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if stage == 1:
        stage_1()
        timer += 1
        timer_s += 1
        timer_r += 1
    if stage == 2:
        stage_2()
        timer += 1
        timer_s += 1
        timer_r += 1
        enemies = 4
    if stage == 0:
        menu()
        enemies = 2

    clock.tick(FPS)
