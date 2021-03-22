import pygame

screen = pygame.display.set_mode(800, 600)
pygame.display.set_caption('Grubhub Offical Game')
white = (255,255,255)

screen.fill(white)
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
