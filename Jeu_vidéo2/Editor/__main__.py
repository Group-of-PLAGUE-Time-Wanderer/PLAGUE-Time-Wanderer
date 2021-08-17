#!/usr/bin/python
# coding: utf-8
import pygame

pygame.init()
window = pygame.display.set_mode((1080, 720))
refresh = pygame.display.flip

black = (0, 0, 0)
bgcolor = (50, 50, 100)
white = (255, 255, 255)
pygame.display.set_caption("Time Wanderer: Map Editor (Indev 0.3)", "PLAGUE: Time wanderer; Map editor")
title = pygame.font.SysFont("Calibri", 50)
h2 = pygame.font.SysFont("Calibri", 45)

running = True

while running:
    window.fill(bgcolor)
    window.blit(title.render("Map Editor", True, white), (450, 20))
    load = h2.render("Load", True, white)

    loadhover = h2.render("> Load", True, white)
    window.blit(load, (450, 150))
    refresh()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
