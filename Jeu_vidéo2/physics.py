#!/usr/bin/python
# coding: utf-8
from config import *


class GravitySprite(pygame.sprite.Sprite):
    def __init__(self, controls: dict = None):
        super().__init__()
        self.velocity = (0, 0)  # x-vel, y-vel
        self.speed = 10
        self.controls = controls
        self.image = load("assets/player.bmp")
        self.rect = self.image.get_rect()

    def move(self, direction):
        if direction == "up":
            self.velocity[1] += self.speed
        elif direction == "down":
            self.velocity[1] -= self.speed
        elif direction == "left":
            self.velocity[0] -= self.speed
        elif direction == "right":
            self.velocity[0] += self.speed

    def collide(self, group):
        print(pygame.sprite.spritecollide(self, group, False))

    def update(self):
        self.rect.x = self.velocity[0]
        self.rect.y = self.velocity[1]

        insert(self.image, self.rect)

#    def update(self):
#        pass
