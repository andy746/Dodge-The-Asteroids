import pygame as pyg
import math
import time
from pygame import mixer
from Asteroid import *
from States import State

# gameplay
class Game(State):
    def __init__(self, w):
        self.w = w
        
        # load fonts
        fonts = pyg.font.get_fonts()
        self.score_font = pyg.font.SysFont("assets/minecraft.ttf", 35, False, False)
        
        # load music
        mixer.init()
        mixer.music.load("assets/8bit-spaceshooter.mp3")
        mixer.music.play(-1)
        mixer.music.set_volume(0.1)

        # load images
        self.bg = pyg.image.load('assets/spacebackground.png')
        self.ship = pyg.transform.scale(pyg.image.load('assets/ship.png'), (80, 80))

        # define rects
        self.wr = w.get_rect()
        self.player = pyg.Rect(0, 0, 30, 50)
        self.player.midleft = self.wr.midleft

        # get sizes
        self.wx , self.wy = w.get_size()
        self.bx, self.by = self.bg.get_size()

        # linked list of Asteroids
        self.asteroids = Asteroids(self.w)

        # to scroll background
        self.scroll = 0
        self.tiles = math.ceil(self.wx / self.bx) + 1

        # start timer
        self.start_time = time.time()

        # score
        self.dist = 0

        # how much the player can move
        self.spd = 5

    # background scroll
    def scroll_bg(self):
        for i in range(0, self.tiles):
            self.w.blit(self.bg, (i * self.bx + self.scroll, 0))

        # scroll background
        self.scroll -= 5

        # reset scroll
        if abs(self.scroll) > self.bx:
            self.scroll = 0

    # draws score
    def draw_text(self):
        text = self.score_font.render('LIGHT-YEARS TRAVELLED: ' + str(self.dist), True, "white")
        self.w.blit(text, text.get_rect(topleft = self.wr.topleft))

    # returns distance travelled
    def get_dist(self):
        return self.dist

    def get_collision(self):
        return not self.asteroids.get_collision()
        
    # run the level
    # returns if player has not collided with any of the asteroids
    def run(self):
        self.scroll_bg()
        self.w.blit(self.ship, self.player)
        self.draw_text()

        # what controls the generation rate of asteroids
        if R(0, 35) == 1:
            self.asteroids.insert(self.w)

        # update asteroids
        if not self.asteroids.is_empty():
            self.asteroids.traversal(self.player, self.asteroids.first)

        # key controls
        kpr = pyg.key.get_pressed()
        if kpr[pyg.K_UP] and self.wr.contains(self.player.move(0, -self.spd)):
            self.player = self.player.move(0, -self.spd)
        if kpr[pyg.K_DOWN] and self.wr.contains(self.player.move(0, self.spd)):
            self.player = self.player.move(0, self.spd)

        # score calculations
        self.dist = int(time.time() - self.start_time)
    

