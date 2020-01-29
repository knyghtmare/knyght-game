import pygame
import random
from inc.player import Player
from inc.monster import Monster
from pygame import mixer


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
mixer.music.load('sounds/background.wav')
mixer.music.play(-1)

num_monsters = 5

blast_x_shift = 5
blaster_img = pygame.image.load('images/blast.png')


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
        player1.activate_laser(screen)

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
