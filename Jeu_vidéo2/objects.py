#!/usr/bin/python
# coding: utf-8
from config import *
import physics


# Entities
class Player(physics.GravitySprite):
    def __init__(self):
        super().__init__()
        self.image = load("assets/player.bmp")
        self.rect.x = window["size"][0]/2
        self.rect.y = 250
        self.jump_power = jump_power
        self.controls = ["up", "down", "left", "right"]


# Solid objects
class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load("assets/floor.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = window["size"][1] - 50

    def update(self):
        insert(self.image, self.rect)
