import pygame
import random

# Inicializar pygame
pygame.init()

# Definir el tamaño de la pantalla
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de Bloques")

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir la posición y tamaño del jugador
player_width = 50
player_height = 50
player_x = width // 2 - player_width // 2
player_y = height - player_height - 10

# Definir la velocidad del jugador y del bloque
player_speed = 2
block_speed = 2

# Definir la puntuación
score = 0

# Definir la lista de bloques
blocks = []

# Función para generar un nuevo bloque
def generate_block():
    block_width = 200
    block_height = 200
    block_x = random.randint(0, width - block_width)
    block_y = -block_height
    return {'x': block_x, 'y': block_y}

# Generar el primer bloque
blocks.append(generate_block())

# Variable para controlar el estado del juego
game_state = "menu"

# Fuente para la puntuación
score_font = pygame.font.Font(None, 36)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_state == "menu":
        # Lógica del menú
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_state = "playing"

        # Dibujar el menú en la pantalla
        screen.fill(WHITE)
        menu_font = pygame.font.Font(None, 36)
        title_text = menu_font.render("Juego de Bloques", True, BLACK)
        start_text = menu_font.render("Presiona ESPACIO para comenzar", True, BLACK)
        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 2 - 50))
        screen.blit(start_text, (width // 2 - start_text.get_width() // 2, height // 2))
        pygame.display.flip()

    elif game_state == "playing":
        # Lógica del juego
        # Mover al jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_width:
            player_x += player_speed

        # Mover los bloques y verificar colisión con el jugador
        for block in blocks:
            block['y'] += block_speed

            if player_x < block['x'] + player_width and player_x + player_width > block['x'] and player_y < block['y'] + player_height and player_y + player_height > block['y']:
                print("¡Perdiste!")
                running = False

            # Verificar si el bloque ha salido de la pantalla
            if block['y'] > height:
                score += 1
                blocks.remove(block)
                blocks.append(generate_block())

        # Dibujar en la pantalla
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))
        for block in blocks:
            pygame.draw.rect(screen, BLACK, (block['x'], block['y'], player_width, player_height))

        # Mostrar la puntuación en la pantalla
        score_text = score_font.render("Puntuación: " + str(score), True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

# Salir del juego
pygame.quit()
print("Puntuación final:", score)
