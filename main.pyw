###############################
#####       Imports       #####
###############################
import pygame
from entity import Entity

#########################################
#####       Utility Functions       #####
#########################################
def draw():
    sprites.draw(screen)

def logic():

    # Update all sprites.
    sprites.update()

    # Apply gravity to those sprites that need it.
    for x in sprites:
        if x.gravity == True:
            x.vely += 1

    # Check collision for player.
    if abs(ground.rect.top - player.rect.bottom) < 5:
        player.vely = 0

    # Getting user input.
    keys = pygame.key.get_pressed()

    # Using user inputs.
    if keys[pygame.K_LEFT] and player.velx > -15:
        player.velx -= 2
    if keys[pygame.K_RIGHT] and player.velx < 15:
        player.velx += 2
    if keys[pygame.K_UP] and abs(ground.rect.top - player.rect.bottom) < 5:
        player.vely -= 20

    # Applying friction
    if player.velx > 0:
        player.velx -= 1
    elif player.velx < 0:
        player.velx += 1


#########################################
######      Engine Variables        #####
#########################################
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('Umgak Shooter')
clock = pygame.time.Clock()
running = True
sprites = pygame.sprite.Group()
grounds = pygame.sprite.Group()


################################
#####       Sprites        #####
################################

###     Player     ###
player = Entity((255, 0, 0), 50, 50)
player.rect.x = 200
player.rect.y = 600
sprites.add(player)

###     Ground     ###
ground = Entity((0, 255, 0), 1200, 100)
ground.rect.x = 0
ground.rect.y = 800
ground.gravity = False
sprites.add(ground)
grounds.add(ground)

#######################################
#####       Initialization       ######
#######################################

# Nothing here yet.

#################################
#####       Main Loop       #####
#################################
while running:
    clock.tick(60)  # The fps is locked at 60!
    screen.fill((255,255,255))  # Erase everything of the screen.

    #########################################
    #####       Handeling Events        #####
    #########################################

    for event in pygame.event.get():    # This will deal with all of the events such as keypresses.
        if event.type == pygame.QUIT:
            running = False

    logic()
    draw()

    pygame.display.flip()   # Updates the screen
