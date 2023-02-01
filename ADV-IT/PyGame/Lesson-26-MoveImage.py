import pygame

MAX_X = 800
MAX_Y = 600
bg_color = (0, 10, 0)

pygame.init()


screen = pygame.display.set_mode((MAX_X, MAX_Y))

pygame.display.set_caption("Hello my First PyGame")
print(pygame.image.get_extended())

myimage = pygame.image.load("intel_imag.png").convert()
myimage = pygame.transform.scale(myimage, (50, 50))
game_over = False

x = 0
y = 0
while game_over == False:

#-----Main Game Loop------
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                x -= 20
            if event.key == pygame.K_RIGHT:
                x += 20
            if event.key == pygame.K_UP:
                y -= 20
            if event.key == pygame.K_DOWN:
                y += 20
        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = event.pos
    screen.fill(bg_color)
    screen.blit(myimage, (x, y))
    pygame.display.flip()