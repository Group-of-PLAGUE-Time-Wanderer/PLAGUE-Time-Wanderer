#!/user/bin/python
# coding: utf-8

import pygame
import button

pygame.init()

window = pygame.display.set_mode((1080, 720))
refresh = pygame.display.flip
clock = pygame.time.Clock()

black = (0, 0, 0)
bgcolor = (50, 50, 100)
white = (255, 255, 255)
yellow = (255, 255, 0)

pygame.display.set_caption("Time Wanderer: Map Editor (Indev 0.51)", "PLAGUE: Time wanderer; Map editor")

title = pygame.font.SysFont("Calibri", 50)
h2 = pygame.font.SysFont("Calibri", 45)
h4 = pygame.font.SysFont("Calibri", 20)

loadbutton = button.TextButton(
    pygame.Rect((445, 200), (122, 45)),
    h2.render("Load", True, white),
    h2.render(">> Load", True, yellow),
)
newbutton = button.TextButton(
    pygame.Rect((445, 147), (122, 45)),
    h2.render("New", True, white),
    h2.render(">> New", True, yellow),
)
buttons = [loadbutton, newbutton]


def update_bevents(pos, e):
    for bt in buttons:
        bt.testforcollision(pos, e)


def update_bdisp(w):
    for bt in buttons:
        bt.update(w)


def menu():
    window.fill(bgcolor)
    window.blit(title.render("Map Editor", True, white), (450, 20))

    mpos = h4.render(str(mousepos), True, white)
    window.blit(mpos, (10, 10))

    update_bdisp(window)

    refresh()
    clock.tick(120)


mousepos = (0, 0)

freeze = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        update_bevents(mousepos, event)

        try:  # toggleing
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                if freeze:
                    freeze = False
                else:
                    freeze = True
        except AttributeError:
            pass

    if not freeze:
        mousepos = pygame.mouse.get_pos()

    menu()

pygame.quit()
