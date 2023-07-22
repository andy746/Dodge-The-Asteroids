from abc import ABC, abstractmethod

import pygame as pyg
from pygameGUI import *

# abstract class
class State(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass

# title screen
class Title(State):
    def __init__(self, w):
        self.w = w
        self.wr = w.get_rect()
        self.bg = pyg.image.load('assets/spacebackground.png')

        # button
        self.start_button = Button(w, bg = "lightblue", text = "Click Here to Start", font = 0, fc = "white", size = (200, 80),
                                  pos = (320, 240), bold = True, pad = 10, bc = "white")
        # title font
        self.title_font = pyg.font.SysFont("Concord", 75, True, False)

    # run the title screen
    def run(self):  
        self.w.blit(self.bg, self.wr)

        # draw button
        self.start_button.draw()
        
        # draw title
        title = self.title_font.render("Dodge the Asteroids!", True, "lightblue")
        self.w.blit(title, title.get_rect(midtop = self.wr.midtop))
    
    # return the start button object
    def get_start_button(self):
        return self.start_button

# game over screen
class GameOver(State):
    def __init__(self, w, score):
        self.w = w
        self.wr = w.get_rect()
        self.score = score
        self.bg = pyg.image.load('assets/spacebackground.png')

        # buttons
        self.restart_button = Button(w, bg = "lightblue", text = "Click Here to Restart", font = 0, fc = "white", size = (200, 80),
                                  pos = (160, 400), bold = True, pad = 10, bc = "white")
        self.end_button = Button(w, bg = "lightblue", text = "Click Here to Exit", font = 0, fc = "white", size = (200, 80),
                                  pos = (480, 400), bold = True, pad = 10, bc = "white")

        # font
        self.final_font = pyg.font.SysFont("Concord", 50, True, False)

    # run the game over screen
    def run(self):
        self.w.blit(self.bg, self.wr)

        # draw buttons
        self.restart_button.draw()
        self.end_button.draw()

        end_text = self.final_font.render('GAME OVER', True, "white")
        self.w.blit(end_text, end_text.get_rect(midtop = self.wr.midtop))

        score_text = self.final_font.render('Score: ' + str(self.score), True, "white")
        self.w.blit(score_text, score_text.get_rect(center = self.wr.center))
    
    # return the restart button object
    def get_restart_button (self):
        return self.restart_button

    # return the end button object
    def get_end_button(self):
        return self.end_button


