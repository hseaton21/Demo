#Sprite Classes for game
#Thanks to Chris and Priya Bradfield\Heavely Inspired by KidsCanCode.
import pygame as pg
from settings import *
from pygame.sprite import Sprite
import random
from os import path
vec = pg.math.Vector2
img = path.join(path.dirname(__file__), 'images')
class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.game = game
        self.player_img = pg.image.load(path.join(img, "Player1Standing.gif")).convert()
        self.image = self.player_img
        self.rect = self.image.get_rect()
        # self.image.set_colorkey(BLACK)
        self.rect.center = (WIDTH /2, HEIGHT /2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.charge = True
        self.left =self.acc.x = -PLAYER_ACC
        self.right =self.acc.x = PLAYER_ACC
        
        
#defining jumping
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -24
#dash variable
    def dash(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and keys[pg.K_LEFT] and keys[pg.K_LCTRL]:
            if hits:
                pass
            else:
                if self.charge == True:
                    self.vel.x = -30
                    self.vel.y = -30
                    self.charge = False
        if keys[pg.K_DOWN] and keys[pg.K_LEFT] and keys[pg.K_LCTRL]:
            if hits:
                pass
            else:    
                if self.charge == True:
                    self.vel.x = -30
                    self.vel.y = 30
                    self.charge = False
        if keys[pg.K_UP] and keys[pg.K_RIGHT] and keys[pg.K_LCTRL]:
            if hits:
                pass
            else:        
                if self.charge == True:
                    self.vel.x = 30
                    self.vel.y = -30
                    self.charge = False
        if keys[pg.K_DOWN] and keys[pg.K_LCTRL] and keys[pg.K_RIGHT]:
            if hits:
                pass
            else:        
                if self.charge == True:
                    self.vel.x = 30
                    self.vel.y = 30
                    self.charge = False
        if keys[pg.K_RIGHT] and keys[pg.K_LCTRL]:
            if hits:
                pass
            else:    
                if self.charge == True:
                    self.vel.x = 30
                    self.charge = False
        if keys[pg.K_LEFT] and keys[pg.K_LCTRL]:
            if hits:
                pass
            else:    
                if self.charge == True:
                    self.vel.x = -30
                    self.charge = False
        if keys[pg.K_DOWN] and keys[pg.K_LCTRL]:
            if hits:
                pass
            else:    
                if self.charge == True:
                    self.vel.y = 30
                    self.charge = False
        if keys[pg.K_UP] and keys[pg.K_LCTRL]:
            if hits:
                pass
            else:    
                if self.charge == True:
                    self.vel.y = -30
                    self.charge = False
    
    def update(self):
        #Controls
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.charge = True
        self.acc = vec(0,PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
            self.player_img = pg.image.load(path.join(img, "Player1Left.gif")).convert()
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
            self.player_img = pg.image.load(path.join(img, "Player1Left.gif")).convert()
        #Acceleration
        self.acc.x += self.vel.x * PLAYER_FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH / 2
            self.pos.y = HEIGHT / 2
        if self.pos.x < 0:
            self.pos.x = WIDTH / 2
            self.pos.y = HEIGHT / 2
        self.rect.midbottom = self.pos
class Player2(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30,40))
        self.image.fill(GREENISH)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH /2, HEIGHT /2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.charge = True
        self.left =self.acc.x = -PLAYER_ACC
        self.right =self.acc.x = PLAYER_ACC
        
#defining jumping
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -24
#dash variable
    def dash(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and keys[pg.K_a] and keys[pg.K_q]:
            if hits:
                pass
            else:
                if self.charge == True:
                    self.vel.x = -30
                    self.vel.y = -30
                    self.charge = False
        if keys[pg.K_s] and keys[pg.K_a] and keys[pg.K_q]:
            if hits:
                pass
            else:    
                if self.charge == True:
                    self.vel.x = -30
                    self.vel.y = 30
                    self.charge = False
        if keys[pg.K_w] and keys[pg.K_d] and keys[pg.K_q]:
            if hits:
                pass
            else:        
                if self.charge == True:
                    self.vel.x = 30
                    self.vel.y = -30
                    self.charge = False
        if keys[pg.K_s] and keys[pg.K_q] and keys[pg.K_d]:
            if hits:
                pass
            else:        
                if self.charge == True:
                    self.vel.x = 30
                    self.vel.y = 30
                    self.charge = False
        if keys[pg.K_d] and keys[pg.K_q]:
            if hits:
                pass
            else:    
                if self.charge == True:
                    self.vel.x = 30
                    self.charge = False
        if keys[pg.K_a] and keys[pg.K_q]:
            if hits:
                pass
            else:    
                if self.charge == True:
                    self.vel.x = -30
                    self.charge = False
        if keys[pg.K_s] and keys[pg.K_q]:
            if hits:
                pass
            else:    
                if self.charge == True:
                    self.vel.y = 30
                    self.charge = False
        if keys[pg.K_w] and keys[pg.K_q]:
            if hits:
                pass
            else:    
                if self.charge == True:
                    self.vel.y = -30
                    self.charge = False
    
    def update(self):
        #Controls
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.charge = True
        self.acc = vec(0,PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_d]:
            self.acc.x = PLAYER_ACC
        #Acceleration
        self.acc.x += self.vel.x * PLAYER_FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH / 2
            self.pos.y = HEIGHT / 2
        if self.pos.x < 0:
            self.pos.x = WIDTH / 2
            self.pos.y = HEIGHT / 2

        self.rect.midbottom = self.pos

#Creating a Pkatform to stand on.
class Platform(Sprite):
    def __init__(self,x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.plat_img = pg.image.load(path.join(img, "yeetform.gif")).convert()
        self.image = self.plat_img
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Platform2(Sprite):
    def __init__(self,x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y