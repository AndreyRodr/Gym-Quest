import pgzrun
from pygame import Rect
from player import Player
from enemy import Enemy
from item import Item

# Configurações do jogo
WIDTH = 1280
HEIGHT = 720
TITLE = "Gym Quest"

game_state = 'menu'
music_on = True
collision_delay = 0 # Tempo de espera antes de detectar colisão

# Botões do menu
start_button = Rect((WIDTH // 2 - 100, 350), (200, 40))
music_button = Rect((WIDTH // 2 - 125, 420), (250, 40))
quit_button = Rect((WIDTH // 2 - 100, 490), (200, 40))

# Botões para o final do jogo
play_again_button = Rect((WIDTH // 2 - 150, 350), (300, 50))
exit_button = Rect((WIDTH // 2 - 100, 430), (200, 50))


qtd_enemies = 5
qtd_items = 5

# Inicialização
def reset_game():
    global player, enemies, items, game_state, collision_delay
    
    player = Player(100, 100)
    
    enemies = []
    for i in range(qtd_enemies):
        enemy_x = 400 + i * 150
        enemy_y = 150 + (i % 2) * 300 
        enemies.append(Enemy(enemy_x, enemy_y))
    
    items = []
    for i in range(qtd_items):
        item_x = 50 + i * 250
        item_y = 150 + (i % 2) * 300
        items.append(Item(item_x, item_y))
    
    collision_delay = 60 # 60 frames de imunidade (aproximadamente 1 segundo)
    game_state = 'menu'

# Chamada inicial
reset_game()

def draw():
    screen.fill((255, 255, 255))
    
    if game_state == 'menu':
        screen.draw.text("Gym Quest", center=(WIDTH // 2, 250), color="black", fontsize=100)
        screen.draw.rect(start_button, (100, 100, 100))
        screen.draw.rect(music_button, (100, 100, 100))
        screen.draw.rect(quit_button, (100, 100, 100))
        
        screen.draw.text("Comecar Jogo", center=start_button.center, color="black", fontsize=40)
        screen.draw.text("Musica: ON/OFF", center=music_button.center, color="black", fontsize=40)
        screen.draw.text("Sair", center=quit_button.center, color="black", fontsize=40)

    elif game_state == 'game':
        for enemy in enemies:
            enemy.draw(screen)
        for item in items:
            item.draw(screen)
        player.draw(screen)

    elif game_state == 'win':
        screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT), (0, 100, 0))
        screen.draw.text("Voce Venceu!", center=(WIDTH // 2, 250), color="white", fontsize=80)
        screen.draw.rect(play_again_button, (100, 100, 100))
        screen.draw.text("Jogar Novamente", center=play_again_button.center, color="white", fontsize=40)
        screen.draw.rect(exit_button, (100, 100, 100))
        screen.draw.text("Sair", center=exit_button.center, color="white", fontsize=40)
    
    elif game_state == 'game_over':
        screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT), (150, 0, 0))
        screen.draw.text("Game Over!", center=(WIDTH // 2, 250), color="white", fontsize=80)
        screen.draw.rect(play_again_button, (100, 100, 100))
        screen.draw.text("Jogar Novamente", center=play_again_button.center, color="white", fontsize=40)
        screen.draw.rect(exit_button, (100, 100, 100))
        screen.draw.text("Sair", center=exit_button.center, color="white", fontsize=40)

def update():
    global game_state, music_on, collision_delay
    if game_state == 'game':
        if collision_delay > 0:
            collision_delay -= 1
        
        player.update(1.0 / 60.0, keyboard) 
        
        for enemy in enemies:
            enemy.update()
        
        if collision_delay == 0:
            for enemy in enemies:
                if player.rect.colliderect(enemy.rect):
                    game_state = 'game_over'
        
        items_to_remove = []
        for item in items:
            if player.rect.colliderect(item.rect):
                items_to_remove.append(item)
                sounds.collect.play()
                player.grow()
        
        for item in items_to_remove:
            items.remove(item)

        if not items:
            game_state = 'win'

def on_mouse_down(pos):
    global game_state, music_on
    if game_state == 'menu':
        if start_button.collidepoint(pos):
            game_state = 'game'
            music.play("musica")
        elif music_button.collidepoint(pos):
            if music.get_volume() > 0:
                music.set_volume(0)
                print("Música está: Desligada")
            else:
                music.set_volume(0.5)
                print("Música está: Ligada")
        elif quit_button.collidepoint(pos):
            quit()
    elif game_state == 'win' or game_state == 'game_over':
        if play_again_button.collidepoint(pos):
            reset_game()
        elif exit_button.collidepoint(pos):
            quit()

# COMO RODAR:
# 1. Certifique-se de ter o Pygame instalado.
# 2. Coloque todas as imagens na pasta "img", o mesmo para music e sounds.
# 3. Execute este script usando pgzrun gym_quest.py(por alguns problemas de path, no meu caso tive de usar .\pgzrun gym_quest.py).