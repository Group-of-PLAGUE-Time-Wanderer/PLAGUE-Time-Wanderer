#!/usr/bin/python
# coding: utf-8
from config import *


class GravitySprite(pygame.sprite.Sprite):
    def __init__(self, controls: dict = None):
        super().__init__()
        self.xvel = 0
        self.yvel = 0
        self.speed = 10
        self.controls = controls
        self.image = load("assets/placeholder.bmp")
        self.rect = self.image.get_rect()
        self.controls = ["up", "down", "left", "right"]
        self.gravity = gravity
        self.collidewith = pygame.sprite.Group()
        self.canjump = False
        self.jump_power = jump_power

    def move(self, direction):
        if direction == "up" and self.canjump:
            self.yvel += self.jump_power
            self.canjump = False
        elif direction == "down":
            self.rect.y += self.speed
        elif direction == "left":
            self.rect.x -= self.speed
        elif direction == "right":
            self.rect.x += self.speed

    def automove(self):
        for thing in self.controls:
            if control(thing):
                self.move(thing)

    def collide(self, group):
        return pygame.sprite.spritecollide(self, group, False)

    def update(self):
        while self.collide(self.collidewith):
            self.canjump = True
            self.yvel = 0
            self.rect.y -= 1

        self.automove()
        self.yvel -= gravity
        self.rect.y -= self.yvel

        insert(self.image, self.rect)

#    def update(self):
#        pass
