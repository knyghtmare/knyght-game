import pygame
import random


# define the screen dimensions
width = 1200
height = 800

pygame.init()

screen = pygame.display.set_mode((width,height))

# add title and icon
pygame.display.set_caption("Tahsin Jahin's 2D shooter Game")
icon = pygame.image.load('images/game-icon.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('images/background.jpg')

# define the player
class Player:
    def __init__(self, player_x, player_y, image):
        self.x = player_x
        self.y = player_y
        self.image = image
        self.mov_val = 5

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

    # def update(self):
    #       self.rect = (self.x, self.y, 100, 100)

num_monsters = 5

# monster class
class Monster:
    """Monster class"""
    def __init__(self, monster_x, monster_y, monster_image):
        self.shift_ver = 3
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


def refresh_screen():
    screen.fill((0, 0, 0))
    # background here
    screen.blit(background, (0, 0))

def update_display(window, player):
    player.draw_on_screen(window)
    pygame.display.update()


player_img = pygame.image.load('images/player/player.png')
you_x = 60
you_y = random.randint(60, 640)
monster_img1 = pygame.image.load('images/monsters/monster1.png')
monster_img2 = pygame.image.load('images/monsters/monster2.png')
monster_img3 = pygame.image.load('images/monsters/monster3.png')
monster_img4 = pygame.image.load('images/monsters/monster4.png')
monster_img5 = pygame.image.load('images/monsters/monster5.png')
mon_x = 1010
mon_y1 = random.randint(60, 640)
mon_y2 = random.randint(60, 640)
mon_y3 = random.randint(60, 640)
mon_y4 = random.randint(60, 640)
mon_y5 = random.randint(60, 640)

def main():
    is_running = True
    clock = pygame.time.Clock()

    player1 = Player(you_x, you_y, player_img)
    monster1 = Monster(mon_x, mon_y1, monster_img1)
    monster2 = Monster(mon_x, mon_y2, monster_img2)
    monster3 = Monster(mon_x, mon_y3, monster_img3)
    monster4 = Monster(mon_x, mon_y4, monster_img4)
    monster5 = Monster(mon_x, mon_y5, monster_img5)

    while is_running:
        clock.tick(60)

        refresh_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()

        player1.movement()

        monster1.monster_movement()
        monster1.draw_screen(screen)
        monster2.monster_movement()
        monster2.draw_screen(screen)
        monster3.monster_movement()
        monster3.draw_screen(screen)
        monster4.monster_movement()
        monster4.draw_screen(screen)
        monster5.monster_movement()
        monster5.draw_screen(screen)

        update_display(screen, player1)

# start the game by calling the main
# function

main()
