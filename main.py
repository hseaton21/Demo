# This file was created by Mikey DiIorio
# Thanks to Chris Bradfield for the "Kids Can Code" Series

import pygame as pg
import random
from settings import *
from sprites import *
import time

class Game:
    def __init__(self): 
        #-Game window
        #Init pygame and create...
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Enigma")
        self.clock = pg.time.Clock()
        self.running = True
        self.background = pg.image.load(path.join(img, "gum.gif"))
        self.background_rect = self.background.get_rect()
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.team_1 = pg.sprite.Group()
        self.team_2 = pg.sprite.Group()
        self.platforms = pg.sprite. Group()
        # Player 1
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.team_1.add(self.player)
        # Player 2
        self.player_2 = Player(self)
        self.player_2.image.fill(WHITE)
        self.player_2.startpos = (2 * WIDTH / 3, HEIGHT / 2)
        self.player_2.up = pg.K_w
        self.player_2.left = pg.K_a
        self.player_2.right = pg.K_d
        self.all_sprites.add(self.player_2)
        self.team_2.add(self.player_2)
        self.oneoff = 0
        self.ntt = 5
        self.start = time.time()
        self.tag1 = False
        self.tag2 = True
        while self.ntt > 0:
            self.ntt = self.ntt - 1
        # Platforms
        for plat in PLAT_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()  
        #Create new player
        pass
    def run(self):
        self.playing = True
        #Game loop
        while self.playing: 
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def update(self):
        while self.oneoff == 0:
            self.player_2.pos = self.player_2.startpos
            self.player_2.vel = vec(0,0)
            self.player.pos = self.player.startpos
            self.player.vel = vec(0,0)
            self.oneoff = self.oneoff + 1

        self.all_sprites.update()
        hits_1 = pg.sprite.spritecollide(self.player, self.platforms, False)
        hits_2 = pg.sprite.spritecollide(self.player_2, self.platforms, False)
        pcollide = pg.sprite.spritecollideany(self.player, self.team_2)
        if hits_1 and self.player.vel.y >= 0:
            self.player.pos.y = hits_1[0].rect.top + 1
            self.player.vel.y = 0
        if self.player.rect.bottom > HEIGHT:
            self.player.pos = self.player.startpos
            self.player.vel = vec(0,0)

        if hits_2 and self.player_2.vel.y >= 0:
            self.player_2.pos.y = hits_2[0].rect.top + 1
            self.player_2.vel.y = 0
        if self.player_2.rect.bottom > HEIGHT:
            self.player_2.pos = self.player_2.startpos
            self.player_2.vel = vec(0,0)

        if pcollide:
            if self.tag1 == True and self.tag2 == False:
                if self.ntt == 0:
                    self.tag1 = False
                    self.tag2 = True
                    if self.ntt == 0:
                        self.ntt += 5
                    print(str(self.ntt))
            elif self.tag2 == True and self.tag1 == False:
                if self.ntt == 0:
                    self.tag1 = True
                    self.tag2 = False
                    if self.ntt == 0:
                        self.ntt += 5
                    print(str(self.ntt))
        if self.tag1 == True:
            self.player.image.fill(BLACK)
            self.player.acc = 1
        if self.tag2 == True:
            self.player_2.image.fill(REDDISH)
            self.player_2.acc = 1
        if self.tag1 == False:
            self.player.image.fill(THANOS)
            self.player.acc = 0.5
        if self.tag2 == False:
            self.player_2.image.fill(WHITE)
            self.player_2.acc = 0.5
        print(str(self.ntt))
        #Update game 
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == self.player.up:
                    self.player.jump()
                if event.key == self.player_2.up:
                    self.player_2.jump()
    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, self.background_rect)
        self.all_sprites.draw(self.screen)
        #Double Buffer
        pg.display.flip()
        #Draw character (and others)
        pass
    def show_start_screen(self):
        #Show the start screen
        pass
    def show_go_screen(self):
        #Show the go screen
        pass

g = Game()
g.show_start_screen()
while g.running: 
    g.new()
    g.show_go_screen()

pg.quit()