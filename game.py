# imports for run the Game
import pygame
import random
# run the Game and init
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption('humans VS aliens')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('human.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = 20
enemyX_change = 0.7
enemyY_change = 40

def enemy (x, y):
    screen.blit(enemyImg, (x, y))

# bullet
# ready - you ca'nt see the bullet on the screen
# fire - the bullet is currnetly moving !
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 1
bullet_state = 'ready'

def fire_bullet (x, y):
    global bullet_state
    bulet_state = 'fire'
    screen.blit(bulletImg, (x, y))
    return bullet_state

# Game Loop
running = True


while running :

    # set the color screen
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running == False

        # what happend when keystroke is precced
        if (event.type == pygame.KEYDOWN):

            if (event.key == pygame.K_LEFT):
                playerX_change = -0.7

            elif (event.key == pygame.K_RIGHT):
                playerX_change = +0.7

            elif (event.key == pygame.K_SPACE):
                if (bullet_state == 'ready'):
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        elif (event.type == pygame.KEYUP):
             if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                playerX_change = 0


    if (playerX <= 0):
        playerX = 0
    elif (playerX >= 736):
            playerX = 736

    if (enemyX <= 0):
        enemyX = 0
        enemyX_change = 0.7
        enemyY += enemyY_change
    elif (enemyX >= 730):
        enemyX = 730
        enemyX_change = -0.7
        enemyY += enemyY_change
    else :
        pass

    # bullet movment

    if (bullet_state is 'fire'):
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        if (bulletY <= 0):
            bulletY = 480
            bullet_state = 'ready'

    playerX += playerX_change
    enemyX += enemyX_change
    bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
