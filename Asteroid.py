import pygame as pyg
from random import randint as R

# node
class Asteroid():
    def __init__(self, w, next = None):
        self.w = w
        self.width, self.height = self.w.get_size()

        self.image = pyg.transform.scale(pyg.image.load('assets/asteroid.png'), (40, 40))
        
        self.spd = R(5, 10)

        # data
        self.rect = self.image.get_rect(topleft=(self.width + 200, R(-25, 455)))
        
        self.next = next

    # return the 
    def get_image(self):
        return self.image

    # return the rectangle area of the asteroid
    def get_rect(self):
        return self.rect

    # update the rectangle area of the asteroid
    def set_rect(self, value):
        self.rect = value

    # return the speed of the asteroid
    def get_spd(self):
        return self.spd

# linked list
class Asteroids (object):
    def __init__ (self, w):
        self.first = None
        self.last = None

        self.w = w
        self.width, self.height = self.w.get_size()

        self.has_collided = False

    # return if any of the asteroids has collided with ship
    def get_collision (self):
        return self.has_collided
    
    # add an item at the end of the list
    def insert (self, w):
        new_link = Asteroid (w)
        if self.first == None:
            self.first = new_link
            self.last = new_link
        else:
            self.last.next = new_link
            self.last = new_link

    # Delete the first occurrence of a Asteroid containing data
    # from an unordered list
    def delete_asteroid (self, data):
        before_link = self.first
        cur_link = self.first

        if (cur_link == None):
            return None

        while (cur_link.get_rect() != data):
            if (cur_link.next == None):
                return None
            else:
                before_link = cur_link
                cur_link = cur_link.next

        if (cur_link == self.first):
            self.first = cur_link.next
        else:
            before_link.next = cur_link.next
            
    # Return True if a list is empty or False otherwise
    def is_empty (self):
        return self.first == None

    # recursively traverse through linked list of Asteroids
    # updates position of asteroids and deletes the objects when they go offscreen
    # keeps track of whether the player has collided with any asteroid
    def traversal (self, player, link = None):
        if link == None:
            return
        else:
            cur_link = link
            if cur_link.get_rect().right > 0:
                self.w.blit(cur_link.get_image(), cur_link.get_rect())
                cur_link.set_rect(cur_link.get_rect().move(-cur_link.get_spd(), 0))
                if player.colliderect(cur_link.get_rect()):
                    self.has_collided = True
                    return
            else:
                self.delete_asteroid(cur_link.get_rect())
            cur_link = cur_link.next
            self.traversal(player, cur_link)
        

