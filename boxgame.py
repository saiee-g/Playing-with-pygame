import pygame

pygame.init()

screenWidth = 800
screenHeight = 800
pygame.display.set_caption("Box Game")

screen = pygame.display.set_mode((screenWidth, screenHeight))

player = pygame.Rect(((screenWidth-50)/2, (screenHeight-50)/2, 30, 30))

run = True
while run:

    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, (156, 207, 231), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_d] or key[pygame.K_RIGHT] == True:
        player.move_ip(1,0)
    elif key[pygame.K_a] or key[pygame.K_LEFT] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_s] or key[pygame.K_DOWN] == True:
        player.move_ip(0,1)
    elif key[pygame.K_w] or key[pygame.K_UP] == True:
        player.move_ip(0,-1)

    if player.left<0:
        player.left=0
        pygame.draw.rect(screen, (253, 208, 218), player)
    elif player.right>screenWidth:
        player.right=screenWidth
        pygame.draw.rect(screen, (163, 159, 225), player)

    if player.top<0:
        player.top=0
        pygame.draw.rect(screen, (254, 236, 214), player)
    elif player.bottom>screenHeight:
        player.bottom=screenHeight
        pygame.draw.rect(screen, (222, 179, 224), player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    pygame.time.Clock().tick(100000)

pygame.quit()
