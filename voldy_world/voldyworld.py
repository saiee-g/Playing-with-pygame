import pygame
import sys
import random

#initialize pygame
pygame.init()

CELL_SIZE = 200
GRID_SIZE = 4
WIDTH = HEIGHT = CELL_SIZE * GRID_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Voldy World')

#load images
harry_img = pygame.image.load('harry.jpg')
voldy_img = pygame.image.load('voldy.png')
snitch_img = pygame.image.load('goldensnitch.jpg')
dementor_img = pygame.image.load('dementor.jpg')

#scale images
harry_img = pygame.transform.scale(harry_img, (CELL_SIZE, CELL_SIZE))
snitch_img = pygame.transform.scale(snitch_img, (CELL_SIZE, CELL_SIZE))
voldy_img = pygame.transform.scale(voldy_img, (CELL_SIZE, CELL_SIZE))
dementor_img = pygame.transform.scale(dementor_img, (CELL_SIZE, CELL_SIZE))

#entities
harry_pos = [0,0]
snitch_pos = [random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE)]
voldy_pos = [random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE)]
dementors = []

for _ in range(3):
    dementors.append([random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)])

#Avoid placing entities in same cell
while snitch_pos == harry_pos:
    snitch_pos = [random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)]
while voldy_pos == harry_pos or voldy_pos == snitch_pos:
    voldy_pos = [random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)]
for dementor in dementors:
    while dementor == harry_pos or dementor == snitch_pos or dementor == voldy_pos:
        dementor[:] = [random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)]


def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

def draw_entities():
    screen.blit(harry_img, (harry_pos[0] * CELL_SIZE, harry_pos[1] * CELL_SIZE))
    screen.blit(snitch_img, (snitch_pos[0] * CELL_SIZE, snitch_pos[1] * CELL_SIZE))
    screen.blit(voldy_img, (voldy_pos[0] * CELL_SIZE, voldy_pos[1] * CELL_SIZE))
    for dementor in dementors:
        screen.blit(dementor_img, (dementor[0] * CELL_SIZE, dementor[1] * CELL_SIZE))

def move_harry(direction):
    if direction == 'UP' and harry_pos[1] > 0:
        harry_pos[1] -= 1
    elif direction == 'DOWN' and harry_pos[1] < GRID_SIZE-1:
        harry_pos[1] += 1
    elif direction == 'LEFT' and harry_pos[0] > 0:
        harry_pos[0] -= 1
    elif direction == 'RIGHT' and harry_pos[1] < GRID_SIZE-1:
        harry_pos[0] +=1

def check_game_over():
    if harry_pos == snitch_pos:
        return "You've caught the golden snitch! Gryffindor Won!"
    if harry_pos == voldy_pos:
        return "Voldy Avada Kedavra-ed you! Game over!"
    if harry_pos in dementors:
        return "You recieved a dementor's kiss! Game over!"
    return None

def main():
    running = True
    while running:
        screen.fill(BLACK)
        draw_grid()
        draw_entities()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_harry('UP')
                elif event.key == pygame.K_DOWN:
                    move_harry('DOWN')
                elif event.key == pygame.K_LEFT:
                    move_harry('LEFT')
                elif event.key == pygame.K_RIGHT:
                    move_harry('RIGHT')

        game_over_message = check_game_over()
        if game_over_message:
            font = pygame.font.SysFont('arial', 40, bold=True)
            message = font.render(game_over_message, True, RED)
            screen.blit(message, (WIDTH//2 - message.get_width()//2, HEIGHT//2 - message.get_height()//2))
            pygame.display.update()
            pygame.time.wait(3000)
            running = False

        pygame.display.update()

if __name__ == "__main__":
    main()

