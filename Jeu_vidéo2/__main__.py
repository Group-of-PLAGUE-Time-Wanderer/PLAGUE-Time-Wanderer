#!/usr/bin/python
# coding: utf-8
from config import *
from time import sleep
import loadutils as load_util
import objects

pygame.init()

disp.set_caption(window["title"], "Time Wanderer")
disp.set_icon(window["icon"])

loading_bar = load_util.ProgressBar((
    window["size"][0]/2 - 500,
    window["size"][1]/2 + 200),

    10, 1000
)

loading_bar.total_steps = 5
step = loading_bar.incrementfromstep

loading_bar.update()
step()
splash = load("assets/splash.png")
splash_pos = calccenter(splash)
step()
start_button = load("assets/launch_button.png")
start_button = pygame.transform.scale(start_button, (400, 400))
launch_rect = start_button.get_rect()
launch_rect.x = calccenter(start_button)[0]
launch_rect.y = round(window["size"][1] / 2 - 150)
step()
floor = objects.Floor()
step()
player = objects.Player()
player.collide_with.add(floor)
step()
sleep(0.1)

del loading_bar

running = True
i = 0
main_menu = True

while running:
    screen.fill((52, 51, 67))
    if main_menu:
        insert(splash, splash_pos)
        insert(start_button, launch_rect)
    else:
        pass

    if not main_menu:
        player.update()
        floor.update()

    refresh()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            if launch_rect.collidepoint(e.pos) and main_menu:
                main_menu = False

        if e.type == pygame.KEYDOWN:
            keys[e.key] = True
        elif e.type == pygame.KEYUP:
            keys[e.key] = False

    clock.tick(window["FPS"])

pygame.quit()
