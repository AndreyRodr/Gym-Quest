import pygame
from pgzero.screen import Screen
from player import Player
from enemy import Enemy

pygame.font.init()
font_title = pygame.font.Font(None, 80)
font_text = pygame.font.Font(None, 30)

# Configurações do jogo
WIDTH = 800
HEIGHT = 600
TITLE = "Gym Quest"

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Variáveis do jogo
game_state = 'menu'
music_on = True

start_button = pygame.Rect((300, 280), (200, 40))
music_button = pygame.Rect((275, 330), (250, 40))
quit_button = pygame.Rect((350, 380), (100, 40))

# Funções de desenho
def draw_menu():
    # Limpa a tela com uma cor de fundo (preto)
    screen.fill((0, 0, 0))

    # Desenha o título
    title_surface = font_title.render("Gym Quest", True, (255, 255, 255))
    title_rect = title_surface.get_rect(center=(WIDTH // 2, 200))
    screen.blit(title_surface, title_rect)
    
    # Desenha os botões (retângulos)
    pygame.draw.rect(screen, (100, 100, 100), start_button)
    pygame.draw.rect(screen, (100, 100, 100), music_button)
    pygame.draw.rect(screen, (100, 100, 100), quit_button)

    # Desenha o texto dos botões
    start_text = font_text.render("Começar Jogo", True, (255, 255, 255))
    start_rect = start_text.get_rect(center=start_button.center)
    screen.blit(start_text, start_rect)
    
    music_text = font_text.render("Música: ON/OFF", True, (255, 255, 255))
    music_rect = music_text.get_rect(center=music_button.center)
    screen.blit(music_text, music_rect)
    
    quit_text = font_text.render("Sair", True, (255, 255, 255))
    quit_rect = quit_text.get_rect(center=quit_button.center)
    screen.blit(quit_text, quit_rect)


# Crie o jogador
player = Player(100, 100)
# Crie um inimigo
enemy = Enemy(400, 300)

clock = pygame.time.Clock()
# Laço principal do jogo (game loop)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Lógica de clique do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == 'menu':
                if start_button.collidepoint(event.pos):
                    # AGORA MUDA O ESTADO DO JOGO
                    game_state = 'game' 
                elif music_button.collidepoint(event.pos):
                    music_on = not music_on
                    print(f"Música está: {'Ligada' if music_on else 'Desligada'}")
                elif quit_button.collidepoint(event.pos):
                    running = False 
    
    delta_time = clock.tick(60) / 1000.0  # Tempo em segundos desde o último frame
    # MUDE ESTAS DUAS LINHAS DE LUGAR, ELAS DEVEM ESTAR AQUI
    keys = pygame.key.get_pressed()
    player.update(keys, delta_time)

    enemy.update()

    if game_state == 'game':
        if player.rect.colliderect(enemy.rect):
            print("Colisão! O jogo acabou.")
            running = False  # Para o jogo
    # Chama a função de desenho
    if game_state == 'menu':
        draw_menu()
    else:
        player.draw(screen)
        enemy.draw(screen)

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()