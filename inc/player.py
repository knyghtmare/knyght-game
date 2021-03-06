import pygame
from pygame import mixer


# define the player
class Player:
    def __init__(self, player_x, player_y, image):
        self.x = player_x
        self.y = player_y
        self.image = image
        self.mov_val = 10
        self.blaster_img = pygame.image.load('images/blast.png')

    def draw_on_screen(self, window):
        window.blit(self.image, (self.x, self.y))

    def movement(self):
        keys = pygame.key.get_pressed()
        # keys for movement
        # you're probably wondering why I did
        # this part with just if's and no elifs
        # Reason: this enables diagonal movement
        if keys[pygame.K_LEFT]:
            self.x -= self.mov_val
        if keys[pygame.K_RIGHT]:
            self.x += self.mov_val
        if keys[pygame.K_UP]:
            self.y -= self.mov_val
        if keys[pygame.K_DOWN]:
            self.y += self.mov_val
        # movement restrictions
        if self.x <= 40:
            self.x = 40
        elif self.x >= 1020:
            self.x = 1020
        if self.y <= 40:
            self.y = 40
        elif self.y >= 660:
            self.y = 660

    def activate_laser(self, window):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            blaster_sound = mixer.Sound('sounds/laser.wav')
            blaster_sound.play()
            self.blast_x = self.x
            self.blast_y = self.y
            try:
                window.blit(self.blaster_img, (self.blast_x + 104, self.blast_y + 22))
            except NameError as e:
                print(e)
