import pygame

# initialize the pygame
pygame.init()

# create the screen/window
screen = pygame.display.set_mode((800, 600))

# Name/Title
pygame.display.set_caption("Mission Space")
icon = pygame.image.load('planet-ringed.png')
pygame.display.set_icon(icon)

# Player
PlayerImg = pygame.image. load('ufo.png')
PlayerX = 370
PlayerY = 480
PlayerX_change = 0

# Enemy
EnemyImg = pygame.image. load('enemy.png')
EnemyX = 370
EnemyY = 50
EnemyX_change = 0

def player(x, y):
    screen.blit(PlayerImg, (x, y))

def Enemy(x, y):
    screen.blit(EnemyImg, (x, y))


# Game loop
Running = True
while Running:

    # RGB and update
    screen.fill((254, 235, 201))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    # if keystroke is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            PlayerX_change = -0.3
        if event.key == pygame.K_RIGHT:
            PlayerX_change = 0.3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            PlayerX_change = 0


    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    PlayerX += PlayerX_change

    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >= 736:
        PlayerX = 736

    player(PlayerX, PlayerY)
    Enemy(EnemyX, EnemyY)
    pygame.display.update()



    





