import pygame
pygame.init()
pygame.display.set_caption("flowers!")
screen = pygame.display.set_mode((800, 800))
screen.fill((0,0,0))

RED = (250,0,0)
ORANGE = (200, 100, 0)
GREEN = (0,150, 0)

def flower(flx,fly,stem = GREEN,petal = RED,thing = ORANGE):
    pygame.draw.rect(screen, (stem), (flx-10, fly+20, 20, 100))
    pygame.draw.circle(screen, (petal), (flx-20, fly+20), 20)
    pygame.draw.circle(screen, (petal), (flx-20, fly-20), 20)
    pygame.draw.circle(screen, (petal), (flx+20, fly+20), 20)
    pygame.draw.circle(screen, (petal), (flx+20, fly-20), 20)
    pygame.draw.circle(screen, (thing), (flx, fly), 20)

flower(200,200,(34,139,34),(255,193,37),(139,58,98))
flower(200,400,GREEN,(127,255,212),(227,207,87))
flower(400,200,(69,139,0),(0,0,255),(138,43,226))
flower(400,400,GREEN,(255,255,255),(255,215,0))
pygame.display.flip()
print("Where is the next flower's x?")
fleex = int(input())
print("Where is the next flower's y?")
fleey = int(input())


flower(fleex,fleey)


pygame.display.flip()