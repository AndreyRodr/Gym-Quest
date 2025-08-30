import pygame
import pgzrun

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load('img/stickman.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 3
        
    def grow(self):
        new_width = int(self.rect.width * 1.3)
        new_height = int(self.rect.height * 1.3)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

        self.rect = self.image.get_rect(center=self.rect.center)
    
    def update(self, delta_time, keyboard):
        is_moving = False
        if keyboard.left:
            self.rect.x -= self.speed
            is_moving = True
        if keyboard.right:
            self.rect.x += self.speed
            is_moving = True
        if keyboard.up:
            self.rect.y -= self.speed
            is_moving = True
        if keyboard.down:
            self.rect.y += self.speed
            is_moving = True

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1280:
            self.rect.right = 1280
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 720:
            self.rect.bottom = 720
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)