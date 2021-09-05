#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Image object
"""
import pygame
import pygame.image
import plague3.objects


class Image(object):
    """Base class for images."""
    def __init__(self, window: plague3.objects.Window, /, path: str = "", x: int = 0, y: int = 0):
        self.window = window
        self.path = path
        self.pos = (x, y)
        self.x = x
        self.y = y
        self.surface = pygame.image.load(self.path).convert_alpha()

    def get(self) -> pygame.Surface:
        return self.surface

    def show(self):
        self.window.add_image(self.surface, self.pos)