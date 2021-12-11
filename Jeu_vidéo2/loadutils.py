#!/usr/bin/python
# coding: utf-8
from config import *


class ProgressBar(pygame.sprite.Sprite):
    def __init__(self, pos: tuple = (0, 0), height: int = 10, full_size: int = 100,
                 color: tuple = (255, 255, 255), back_color: tuple = (0, 0, 0)):
        super().__init__()
        self.size = 0
        self.full_size = full_size
        self.position = pos
        self.color = color
        self.back_color = back_color
        self.height = height
        self.totalsteps = None
        self.step = 0

    def resize(self, percent):
        if self.size < self.full_size:
            self.size = (percent/100) * self.full_size
        else:
            self.size = self.full_size

        self.update()

    def incrementfromstep(self):
        if self.totalsteps:
            self.step += 1
            self.resize(self.step / self.totalsteps*100)

    def update(self):

        pygame.draw.rect(screen, self.back_color,
                         [self.position[0], self.position[1],
                          self.full_size, self.height])

        pygame.draw.rect(screen, self.color,
                         [self.position[0], self.position[1],
                          self.size, self.height])
        refresh()
