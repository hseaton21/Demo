#This Post Was made By Harrison Seaton
#Thanks to Chris and Priya Bradfield\Heavely Inspired by KidsCanCode.
import pygame as pg
from settings import *
import random
from sprites import *

class Game:
    def __init__(self):
         #init game window, try:
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Oingo Boingo Bros")
        self.clock = pg.time.Clock()
        self.running = True
        #init pygame and create...
    def new(self):
        #Create new player object
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLAT_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
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
        #Temp, Scrolling the screen up.
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
        if self.player.rect.bottom > HEIGHT:
            self.playing = False
    def events(self):
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def draw(self):
        self.screen.fill(BLACK)
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
 