#!/usr/python
# -*- coding: utf-8 -*-
from config import *
import loadutils as load_util

pygame.init()

disp.set_caption(window["title"])
disp.set_icon(window["icon"])

progress = load_util.ProgressBar((window["size"][0]/2 - 500, window["size"][1]/2 + 20))

splash = load("assets/splash.png")
print("é")

running = True

while running:
    refresh()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    clock.tick(window["FPS"])

pygame.quit()
