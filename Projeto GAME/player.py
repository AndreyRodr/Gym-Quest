import pygame

class Player:
    def __init__(self, x, y):
        # ... (seu código de inicialização)
        self.frames = [pygame.Surface((32, 32)), pygame.Surface((32, 32))]
        self.frames[0].fill((0, 200, 0)) # Frame 1: cor verde
        self.frames[1].fill((0, 150, 0)) # Frame 2: cor verde mais escura

        self.current_frame = 0 # Começa no primeiro frame da lista
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 3
        self.animation_speed = 0.2
        self.animation_timer = 0

    def update(self, keys, delta_time):
        # Lógica de movimento...
        is_moving = False
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            is_moving = True
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            is_moving = True
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            is_moving = True
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            is_moving = True

        # Lógica de animação
        if is_moving:
            self.animation_timer += delta_time
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.image = self.frames[self.current_frame]
        else:
            # Voltar para o frame parado se o jogador parar
            self.current_frame = 0
            self.image = self.frames[self.current_frame]

    def draw(self, screen):
        screen.blit(self.image, self.rect)