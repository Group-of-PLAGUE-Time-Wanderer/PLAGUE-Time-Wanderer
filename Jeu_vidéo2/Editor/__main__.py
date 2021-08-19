# coding: utf-8
import pygame
from time import sleep

pygame.init()
window = pygame.display.set_mode((1080, 720))
refresh = pygame.display.flip
clock = pygame.time.Clock()

black = (0, 0, 0)
bgcolor = (50, 50, 100)
white = (255, 255, 255)
loadrect = [
            450,  # début x
            155,  # début y
            270,  # fin x (relatif)
            45,  # fin y (relatif)
        ]
loadsquare = pygame.draw.rect(window, white, loadrect)
pygame.display.set_caption("Time Wanderer: Map Editor (Indev 0.3)", "PLAGUE: Time wanderer; Map editor")

title = pygame.font.SysFont("Calibri", 50)
h2 = pygame.font.SysFont("Calibri", 45)
h4 = pygame.font.SysFont("Calibri", 20)

mousepos = ""
freeze = False

running = True

while running:
    window.fill(bgcolor)
    window.blit(title.render("Map Editor", True, white), (450, 20))
    load = h2.render("Load", True, black)

    loadhover = h2.render("> Load", True, black)
    loadsquare = pygame.draw.rect(window, white, loadrect)
    window.blit(load, (450, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        try:  # toggleing
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                if freeze:
                    freeze = False
                else:
                    freeze = True
        except AttributeError:
            pass

        if not freeze:
            mousepos = str(pygame.mouse.get_pos())

    mpos = h4.render(mousepos, True, white)
    window.blit(mpos, (10, 10))

    refresh()
    clock.tick(120)

pygame.quit()
