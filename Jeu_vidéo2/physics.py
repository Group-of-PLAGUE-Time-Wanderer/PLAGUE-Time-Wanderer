#!/usr/bin/python
# coding: utf-8
from config import *


class GravitySprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_vel = 0
        self.y_vel = 0
        self.speed = 10
        self.image = load("assets/placeholder.bmp")
        self.rect = self.image.get_rect()
        self.controls = None
        self.gravity = gravity
        self.collide_with = pygame.sprite.Group()
        self.can_jump = False
        self.jump_power = None

    def move(self, direction):
        if direction == "up" and self.can_jump:
            self.y_vel += self.jump_power
            self.can_jump = False
        elif direction == "down":
            self.rect.y += self.speed
        elif direction == "left":
            self.rect.x -= self.speed
        elif direction == "right":
            self.rect.x += self.speed

    def auto_move(self):
        for thing in self.controls:
            if control(thing):
                self.move(thing)

    def collide(self, group):
        return pygame.sprite.spritecollide(self, group, False)

    def update(self):
        while self.collide(self.collide_with):
            self.can_jump = True
            self.y_vel = 0
            self.rect.y -= 1

        self.auto_move()
        self.y_vel -= gravity
        self.rect.y -= self.y_vel

        insert(self.image, self.rect)
