#!/usr/bin/python
# coding: utf-8
from config import *


class GravitySprite(pygame.sprite.Sprite):
    def __init__(self, controls: dict = None):
        super().__init__()
        self.x_vel = 0
        self.y_vel = 0
        self.speed = 10
        self.controls = controls
        self.image = load("assets/player.bmp")
        self.rect = self.image.get_rect()
        self.controls = ["up", "down", "left", "right"]
#        self.keyy = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]

    def move(self, direction):
        if direction == "up":
            self.y_vel -= self.speed
        elif direction == "down":
            self.y_vel += self.speed
        elif direction == "left":
            self.x_vel -= self.speed
        elif direction == "right":
            self.x_vel += self.speed

    def automove(self):
        for thing in self.controls:
            if control(thing):
                self.move(thing)

    def collide(self, group):
        print(pygame.sprite.spritecollide(self, group, False))

    def update(self):
        self.rect.x = self.x_vel
        self.rect.y = self.y_vel

        self.automove()

        insert(self.image, self.rect)

#    def update(self):
#        pass
