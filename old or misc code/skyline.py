import pygame
import random
pygame.init()
pygame.display.set_caption("flowers!")
screen = pygame.display.set_mode((800, 800))
screen.fill((255,255,255))

def floor(floorx,floory,floryin,flooryan):
    pygame.draw.rect(screen, (random.randrange(0, 256),random.randrange(0, 256),random.randrange(0, 256)), (floorx, floory, flooryan*floryin, flooryan))
    windowcol = (random.randrange(0, 256),random.randrange(0, 256),random.randrange(0, 256))
    for w in range(floryin):
        pygame.draw.rect(screen, (windowcol), ((floorx+(flooryan/4)+(flooryan*w)), floory+(flooryan/4), flooryan/2, flooryan/2))
        
def building(xxx,size):
    floors = random.randrange(2, 10)
    floorsize = size/floors
    for i in range(floors+random.randrange(1, 10-round(size/50))):
        floor(xxx,((-i*floorsize)+800),floors,floorsize)
    floorheight = (-i*floorsize)+800
    pygame.draw.polygon(screen, (random.randrange(0, 256),random.randrange(0, 256),random.randrange(0, 256)), ((xxx, floorheight), (size, floorheight), (size/2, floorheight-(size/2))))
print("buildings")
stuff = int(input())
jek = 0
for u in range(stuff):
    if u == stuff-1:
        building(jek,800-jek)
    else:
        print("stuff is", stuff)
        stuff = 800//stuff
        rend = random.randrange(5, stuff)
        print("rend is", rend)
        building(jek,rend)
        jek += rend
pygame.display.flip()