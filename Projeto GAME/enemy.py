import pygame
import pgzrun
import random

class Enemy:
    def __init__(self, x, y):
        self.image = pygame.image.load('img/batata.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(x=x, y=y)
        
        # Define uma velocidade aleatória para x e y
        self.speed_x = random.choice([-2, 2])
        self.speed_y = random.choice([-2, 2])
        
        # Contador para mudar a direção de vez em quando
        self.change_direction_timer = 0
        
    def update(self):
        # Move o inimigo
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Aumenta o contador de tempo
        self.change_direction_timer += 1
        
        if self.change_direction_timer >= 120:  # Muda de direção a cada 2 segundos
            self.change_direction_timer = 0
            self.speed_x = random.choice([-2, 2])
            self.speed_y = random.choice([-2, 2])

        # O inimigo não sai da tela
        if self.rect.left < 0 or self.rect.right > 1280:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > 720:
            self.speed_y *= -1

    def draw(self, screen):
        screen.blit(self.image, self.rect)