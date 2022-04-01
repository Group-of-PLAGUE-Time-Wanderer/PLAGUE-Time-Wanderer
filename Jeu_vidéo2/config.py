# -*- coding: utf-8 -*-
import pygame
# from time import sleep

load = pygame.image.load

# Configuration du jeu
window = {
    "size": (1080, 740),
    "title": "PLAGUE: Time Wanderer Indev 1.4",
    "icon": load("../plague3/assets/images/icon.png"),
    "FPS": 60,  # Changing it later
}

# Physics
gravity = 0.5

# PLayer
jump_power = 15
player_controls = {
    "up": pygame.K_SPACE,
    "down": None,  # disabled
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
}

# Alias
disp = pygame.display
screen = disp.set_mode(window["size"])
insert = screen.blit
refresh = disp.flip
clock = pygame.time.Clock()
keys = {}


def calccenter(img):
    global screen
    scsize = window["size"]
    isl = img.get_size()
    # calcul condensé du centre de l'écran soustrait aux centre de l'image pour arriver pile au... milieu
    return round(scsize[0]/2-isl[0]/2), round(scsize[1]/2-isl[1]/2)


def control(direction: str):
    try:
        return keys[player_controls[direction]]
    except KeyError:
        return False
