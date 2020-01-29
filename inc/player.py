import pygame




# define the player
class Player:
    def __init__(self, player_x, player_y, image):
        self.x = player_x
        self.y = player_y
        self.image = image
        self.mov_val = 10

        # dummy rectangle for player
        # self.rect = (player_x, player_y, 100, 100)

    def draw_on_screen(self, window):
        # pygame.draw.rect(window, (255, 0, 0), self.rect)
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

       # self.update()

    def activate_laser(self):
        pass
