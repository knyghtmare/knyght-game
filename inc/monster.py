import pygame
import random


# monster class
class Monster:
    """Monster class"""
    def __init__(self, monster_x, monster_y, monster_image):
        self.shift_ver = 5
        self.shift_hor = -50
        self.x = monster_x
        self.y = monster_y
        self.image = monster_image

    def draw_screen(self, window):
        window.blit(self.image, (self.x, self.y))

    def monster_movement(self):
        # move to the left when
        # monster reaches a boundary
        self.y += self.shift_ver

        if self.y <= 60:
            self.shift_ver = random.randint(3,5)
            self.x += self.shift_hor
        elif self.y >= 640:
            self.shift_ver = random.randint(-5, -3)
            self.x += self.shift_hor

    def got_hit():
        pass
