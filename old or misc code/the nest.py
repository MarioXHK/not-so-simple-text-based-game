#Hey! I already did this with a partner >:(
import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("nested for loops")
clock = pygame.time.Clock()
GameLoop = True

for i in range(20):
    for j in range (20):
        pygame.draw.rect(screen, (200,0,100), (i*40, j*40, 20, 20))
        pygame.draw.circle(screen, (100, 0, 200), ((i*40)+10, (j*40)+10), 8)
        
pygame.display.flip()