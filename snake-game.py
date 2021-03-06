import pygame
from pygame.locals import *
from random import randint
import os, sys

ARRAY_SIZE = 50

DIRECTIONS = {
    "LEFT": (-1, 0), "RIGHT": (1, 0), "UP": (0, 1), "DOWN": (0, -1)}

snake, fruit = None, None

def init():
    global snake
    snake = [ (0, 2), (0, 1), (0, 0)]

    place_fruit((ARRAY_SIZE // 2, ARRAY_SIZE // 2))

def place_fruit(coord=None):
    global fruit
    if coord:
        fruit = coord
        return

    while True:
        x = randint(0, ARRAY_SIZE-1)
        y = randint(0, ARRAY_SIZE-1)
        if (x, y) not in snake:
           fruit = x, y
           return

def step(direction):
    old_head = snake[0]
    movement = DIRECTIONS[direction]
    new_head = (old_head[0]+movement[0], old_head[1]+movement[1])

    if (
            new_head[0] < 0 or
            new_head[0] >= ARRAY_SIZE or
            new_head[1] < 0 or
            new_head[1] >= ARRAY_SIZE or
            new_head in snake
        ):
        return False
        
    if new_head == fruit:
        place_fruit()
    else:
        del snake[-1]

    snake.insert(0, new_head)
    return True

DIRS = ['UP', 'RIGHT', 'DOWN', 'LEFT']
def run():
    init()

    direction = 0

    pygame.init()
    s = pygame.display.set_mode((ARRAY_SIZE * 10, ARRAY_SIZE * 10))
    appleimage = pygame.Surface((10, 10))
    appleimage.fill((255, 0, 255))
    img = pygame.Surface((10, 10))
    img.fill((0, 255, 0))

    pygame.time.set_timer(1, 100)

    while True:
        e = pygame.event.wait()                             
        if e.type == QUIT:                                                                  
            pygame.quit()                               
        
        elif e.type == KEYDOWN:
            key=pygame.key.get_pressed()
            
            if      key[pygame.K_UP]:     direction = 0
            elif    key[pygame.K_RIGHT]:    direction = 1
            elif    key[pygame.K_DOWN]:       direction = 2
            elif    key[pygame.K_LEFT]:     direction = 3

        if not step(DIRS[direction]):                   
            pygame.quit()                          
            sys.exit()

        s.fill((255, 255, 255))	
        for bit in snake:
            s.blit(img, (bit[0] * 10, (ARRAY_SIZE - bit[1] - 1) * 10))
        s.blit(appleimage, (fruit[0] * 10, (ARRAY_SIZE - fruit[1]-1) * 10))
        pygame.display.flip()
run()
