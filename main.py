import pygame
import random

# initialize the pygame
pygame.init()

# create the screen/window
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('galaxy.png')

# Name/Title
pygame.display.set_caption("Mission Space")
icon = pygame.image.load('planet-ringed.png')
pygame.display.set_icon(icon)

# Player
PlayerImg = pygame.image.load('ufo.png')
PlayerX = 370
PlayerY = 480
PlayerX_change = 0

# Enemy
EnemyImg = pygame.image.load('enemy.png')
EnemyX = random.randint(0, 800)
EnemyY = random.randint(50, 150)
EnemyX_change = 0.2
EnemyY_change = 30

# Bullet
# Ready - state is that you cannot see the bullet
# Fire - is that the bullet is still currently moving
BulletImg = pygame.image.load('bullet.png')
BulletX = 0
BulletY = 480
BulletX_change = 0
BulletY_change = 10
Bullet_state = "ready"


def player(x, y):
    screen.blit(PlayerImg, (x, y))


def Enemy(x, y):
    screen.blit(EnemyImg, (x, y))


def fire_bullet(x, y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(BulletImg, (x + 16, y + 10))


# Game loop
Running = True
while Running:

    # RGB and update
    screen.fill((0, 0, 0))

    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    # if keystroke is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            PlayerX_change = -0.3
        if event.key == pygame.K_RIGHT:
            PlayerX_change = 0.3
        if event.key == pygame.K_SPACE:
            fire_bullet(PlayerX, BulletY)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            PlayerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    # checking for boundaries so that the character don't exceed the frame.
    PlayerX += PlayerX_change

    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >= 736:
        PlayerX = 736

    # Enemy movement
    EnemyX += EnemyX_change

    if EnemyX <= 0:
        EnemyX_change = 0.2
        EnemyY += EnemyY_change
    elif EnemyX >= 736:
        EnemyX_change = -0.2
        EnemyY += EnemyY_change

    # Bullet movement
    if Bullet_state == "fire":
        fire_bullet(PlayerX, BulletY)
        BulletY -= BulletY_change

    player(PlayerX, PlayerY)
    Enemy(EnemyX, EnemyY)
    pygame.display.update()
