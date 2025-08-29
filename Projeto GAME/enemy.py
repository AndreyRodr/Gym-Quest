import pygame

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.image = pygame.Surface((32, 32))
        self.image.fill((200, 0, 0))  # Um quadrado vermelho para o inimigo
        self.speed = 2
        self.direction = 1  # 1 para direita, -1 para esquerda

    def update(self):
        self.rect.x += self.speed * self.direction
        # Mude a direção ao atingir as bordas
        if self.rect.left < 0 or self.rect.right > 800:
            self.direction *= -1

    def draw(self, screen):
        screen.blit(self.image, self.rect)