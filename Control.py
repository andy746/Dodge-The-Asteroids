import pygame as pyg
import sys
from pygame import mixer
from Game import *
from States import *

class Control:
    def __init__(self, w):
        self.state_name = "title"
        self.w = w
        self.state = Title (self.w)

    # event_loop
    def event_loop(self):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                # exit game
                pyg.quit()
                sys.exit()
    
            if event.type == pyg.MOUSEBUTTONDOWN:
                if self.state_name == "title":
                    # transition to game screen
                    if self.state.get_start_button().click():
                        self.state_name = "game"
                        self.state = Game (self.w)
                elif self.state_name == "over":
                    # exit game
                    if self.state.get_end_button().click():
                        pyg.quit()
                        sys.exit()
                    # transition to game screen
                    if self.state.get_restart_button().click():
                        self.state_name = "game"
                        self.state = Game (self.w)

    # checks if game over conditions have been met
    # and if so, transitions from game screen to game over screen
    def check_game_con(self):
        # transition to game over screen
        if not self.state.get_collision():
            self.state_name = "over"
            mixer.music.stop()
            self.state = GameOver(self.w, self.state.get_dist())

    # run current state
    def state_run(self):
        self.event_loop()
        self.state.run()
        if self.state_name == "game":
            self.check_game_con()
            

def main():
    pyg.init()
    w = pyg.display.set_mode((640, 480))
    pyg.display.set_caption("Dodge The Asteroids")
    
    app = Control(w)

    # game loop
    while True:
        w.fill("white")

        app.state_run()

        pyg.display.update()
        pyg.time.delay(17)
        pyg.event.pump()


if __name__ == "__main__":
    main()
