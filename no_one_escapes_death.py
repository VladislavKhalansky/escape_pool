from point import Point, Chaser
import pygame
import tkinter
from tkinter import messagebox


def manual():
    global event, flag, game_over
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            return game_over
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flag = False
            elif event.key == pygame.K_RIGHT:
                flag = True
    murder.move_set(pool_size, right=flag)


_SANIC = 'sanic_50p.png'
_PEPE = 'pepe_50p.png'

pool_size = 512
speed = 8

murder = Chaser(pool_size, 0, speed)
survivor = Point(pool_size // 2, pool_size // 2, speed / 3)

tkinter.Tk().wm_withdraw()
auto_game_mode = messagebox.askyesno('mode./', 'Автоматический режим ловца?')

pygame.init()
white = (170, 170, 170)
black = (0, 0, 0)
red = (255, 0, 0)
dis = pygame.display.set_mode((pool_size + 50, pool_size + 50))
pygame.display.set_caption('Catch me if you can!')
font = pygame.font.Font(None, 20)

x1 = murder.point.x
y1 = murder.point.y
x2 = survivor.x
y2 = survivor.y

clock = pygame.time.Clock()
game_over = False
flag = True
while not game_over:
    if 0 > survivor.x or 0 > survivor.y or \
            survivor.x > pool_size or survivor.y > pool_size:
        survivor = Point(pool_size // 2, pool_size // 2, speed / 3)

    if auto_game_mode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        murder.chaser_ai_core(survivor, pool_size)
    else:
        manual()

    survivor.move(murder.point)
    x1 = round(murder.point.x)
    y1 = round(murder.point.y)
    x2 = round(survivor.x)
    y2 = round(survivor.y)

    distance = str(round(murder.point.distance(survivor)))

    dis.fill(white)
    img = pygame.image.load(_PEPE)
    img2 = pygame.image.load(_SANIC)
    dis.blit(img, (x1, y1))
    dis.blit(img2, (x2, y2))

    text = font.render("Дистанция:", True, black)
    text2 = font.render(distance, True, black)
    dis.blit(text, (10, 50))
    dis.blit(text2, (200, 50))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
