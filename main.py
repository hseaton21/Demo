#This Post Was made By Harrison Seaton
#Thanks to Chris and Priya Bradfield\Heavely Inspired by KidsCanCode.
import pygame as pg
from settings import *
import random
from sprites import *
from os import path

class Game:
    def __init__(self):
         #init game window,try:
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Oingo Boingo Bros")
        self.clock = pg.time.Clock()
        self.running = True
        self.background = pg.image.load(path.join(img, "bazonk.jpg")).convert()
        self.background_rect = self.background.get_rect()
        self.p1lives = 3
        self.p2lives = 3
        #init pygame and create...
    def new(self):
        #Create new player object
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.player2 = Player2(self)
        self.all_sprites.add(self.player2)
        self.all_sprites.add(self.player)
        self.stage_select = input("Gimme a stage, choose 1, 2, or 3: ")
        if self.stage_select == "1":
            for plat in STAGE_1:
                p = Platform(*plat)
                self.all_sprites.add(p)
                self.platforms.add(p)
        if self.stage_select == "2":
            for plat in STAGE_2:
                p = Platform(*plat)
                self.all_sprites.add(p)
                self.platforms.add(p)
        if self.stage_select == "3":
            for plat in STAGE_3:
                p2 = Platform2(*plat)
                self.all_sprites.add(p2)
                self.platforms.add(p2)
        self.run()
    def run(self):
        #game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def update(self): 
        #update things
        self.all_sprites.update()
        #Collisions
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits: 
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
        if self.player2.vel.y > 0:
            hits2 = pg.sprite.spritecollide(self.player2, self.platforms, False)
            if hits2: 
                self.player2.pos.y = hits2[0].rect.top + 1
                self.player2.vel.y = 0
        #Temp, Scrolling the screen up.
        if self.player.rect.bottom >= 825:
            self.player.pos.x = WIDTH / 2
            self.player.pos.y = HEIGHT / 2
            self.p1lives = self.p1lives - 1
            print(str(self.p1lives))
        if self.player2.rect.bottom >= 825:
            self.player2.pos.x = WIDTH / 2
            self.player2.pos.y = HEIGHT / 2
            self.p2lives = self.p2lives - 1
            print(str(self.p2lives))
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.player2.jump()
            self.player.dash()
            self.player2.dash()
    def draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, self.background_rect)
        self.all_sprites.draw(self.screen)
        #double buffer
        pg.display.flip()

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen
 