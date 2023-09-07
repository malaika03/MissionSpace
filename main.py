import pygame

# initialize the pygame
pygame.init()

# create the screen/window
screen = pygame.display.set_mode((800, 600))

# Name/Title
pygame.display.set_caption("Mission Space")

# Game loop
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

# RGB and update
    screen.fill((254, 235, 201))
    pygame.display.update()

    





