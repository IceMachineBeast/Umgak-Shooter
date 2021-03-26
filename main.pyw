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
    collision_tolarence = 5

    sprites.update()
    for x in gravity_sprites:
        x.vely += 1

    for x in grounds:
        if player.rect.colliderect(x.rect):
            if abs(player.rect.bottom - x.rect.top) < collision_tolarence:
                player.vely = 0
                print("KEK")

#########################################
######      Engine Variables        #####
#########################################
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('Umgak Shooter')
clock = pygame.time.Clock()
running = True
sprites = pygame.sprite.Group()
gravity_sprites = pygame.sprite.Group()
grounds = pygame.sprite.Group()


################################
#####       Sprites        #####
################################

###     Player     ###
player = Entity((255, 0, 0), 50, 50)
player.rect.x = 200
player.rect.y = 300
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

for x in sprites:
    if x.gravity == True:
        gravity_sprites.add(x)

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
