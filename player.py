import pygame

WHITE = (255, 255, 255)
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Variables
        self.velx = 0
        self.vely = 0

        # Draw the car (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
