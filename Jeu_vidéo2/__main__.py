#!/usr/python
# -*- coding: utf-8 -*-
from config import *
import loadutils as load_util

pygame.init()

disp.set_caption(window["title"], "Time Wanderer")
disp.set_icon(window["icon"])

loading_bar = load_util.ProgressBar((
    window["size"][0]/2 - 500,
    window["size"][1]/2 + 200),

    10, 1000
)

loading_bar.totalsteps = 2
step = loading_bar.incrementfromstep

loading_bar.update()
splash = load("assets/splash.png")
splashpos = calccenter(splash)
step()
start_button = load("assets/launch_button.png")
launchrect = start_button.get_rect()
launchrect.x = calccenter(start_button)[0]
launchrect.y = round(window["size"][1]/2)
step()
sleep(0.5)

del loading_bar

running = True
i = 0

while running:
    screen.fill((52, 51, 67))
    insert(splash, splashpos)
    insert(start_button, launchrect)
    refresh()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        elif e.type == pygame.MOUSEBUTTONDOWN:
            if launchrect.collidepoint(e.pos):
                print("start")

    clock.tick(window["FPS"])

pygame.quit()
