###############################
#####       Imports       #####
###############################
import pygame

#########################################
#####       Utility Functions       #####
#########################################
def draw():
    pass

def logic():
    pass

def events():
    for event in pygame.event.get():    # This will deal with all of the events such as keypresses.
        if event.type == pygame.QUIT:
            running = False

#########################################
######      Engine Variables        #####
#########################################
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('Umgak Shooter')
clock = pygame.time.Clock()
running = True

#################################
#####       Main Loop       #####
#################################
while running:
    clock.tick(60)  # The fps is locked at 60!
    screen.fill((255,255,255))  # Erase everything of the screen.

    events()
    logic()
    draw()

    pygame.display.flip()   # Updates the screen
