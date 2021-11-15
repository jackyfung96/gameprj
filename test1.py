import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()  # Capitalise
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground = pygame.image.load('graphics/ground.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))  # blit = block image transfer
    screen.blit(ground, (0, 300))

    pygame.display.update()
    clock.tick(60)
