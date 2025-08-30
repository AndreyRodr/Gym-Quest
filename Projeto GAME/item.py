import pygame

class Item:
    def __init__(self, x, y):
        self.image = pygame.image.load('img/halter.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(x=x, y=y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)