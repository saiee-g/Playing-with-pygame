import pygame

pygame.init()

screenWidth = 800
screenHeight = 800
pygame.display.set_caption("Box Game")

screen = pygame.display.set_mode((screenWidth, screenHeight))

player = pygame.Rect(((screenWidth-50)/2, (screenHeight-50)/2, 30, 30))
player2 = pygame.Rect(((screenWidth-50)/2, (screenHeight-50)/2, 30, 30))

run = True
while run:

    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, (156, 207, 231), player)
    pygame.draw.rect(screen, (255, 204, 255), player2)

    key = pygame.key.get_pressed()
    if key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] == True:
        player2.move_ip(1,0)
    elif key[pygame.K_LEFT] == True:
        player2.move_ip(-1,0)
    elif key[pygame.K_DOWN] == True:
        player2.move_ip(0,1)
    elif key[pygame.K_UP] == True:
        player2.move_ip(0,-1)

    if player.left<0:
        player.left=0
        pygame.draw.rect(screen, (128, 128, 255), player)
    elif player.right>screenWidth:
        player.right=screenWidth
        pygame.draw.rect(screen, (215, 179, 255), player)
    if player.top<0:
        player.top=0
        pygame.draw.rect(screen, (51, 153, 255), player)
    elif player.bottom>screenHeight:
        player.bottom=screenHeight
        pygame.draw.rect(screen, (102, 255, 204), player)

    if player2.left<0:
        player2.left=0
        pygame.draw.rect(screen, (153, 0, 204), player2)
    elif player2.right>screenWidth:
        player2.right=screenWidth
        pygame.draw.rect(screen, (255, 102, 102), player2)
    if player2.top<0:
        player2.top=0
        pygame.draw.rect(screen, (204, 255, 102), player2)
    elif player2.bottom>screenHeight:
        player2.bottom=screenHeight
        pygame.draw.rect(screen, (191, 64, 128), player2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()
    pygame.time.Clock().tick(100000)

pygame.quit()
