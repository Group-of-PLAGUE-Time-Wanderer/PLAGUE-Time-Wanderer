#!/usr/bin/python
# coding: utf-8
from config import *
from time import sleep
import loadutils as load_util

pygame.init()

disp.set_caption(window["title"], "Time Wanderer")
disp.set_icon(window["icon"])

loading_bar = load_util.ProgressBar((
    window["size"][0]/2 - 500,
    window["size"][1]/2 + 200),

    10, 1000
)

loading_bar.totalsteps = 5
step = loading_bar.incrementfromstep

loading_bar.update()
import objects
step()
splash = load("assets/splash.png")
splashpos = calccenter(splash)
step()
start_button = load("assets/launch_button.png")
start_button = pygame.transform.scale(start_button, (400, 400))
launchrect = start_button.get_rect()
launchrect.x = calccenter(start_button)[0]
launchrect.y = round(window["size"][1]/2 - 150)
step()
floor = objects.Floor()
step()
player = objects.Player()
player.collidewith.add(floor)
step()
sleep(0.1)

del loading_bar

running = True
i = 0
main_menu = True

while running:
    screen.fill((52, 51, 67))
    if main_menu:
        insert(splash, splashpos)
        insert(start_button, launchrect)
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
            print("mouse")
            if launchrect.collidepoint(e.pos) and main_menu:
                print("start")
                main_menu = False

        if e.type == pygame.KEYDOWN:
            print("key pressed")
            keys[e.key] = True
        elif e.type == pygame.KEYUP:
            print("key released")
            keys[e.key] = False

    clock.tick(window["FPS"])

pygame.quit()
