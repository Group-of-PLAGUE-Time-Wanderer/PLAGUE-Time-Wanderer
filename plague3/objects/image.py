#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Image object
"""
import pygame
#import plague3.objects


class Image(object):
    """Base class for images."""
    def __init__(self, window: plague3.objects.Window, /, path: str = ""):
        self.window = window
        self.path = path
        self.surface = pygame.image.load(self.path).convert_alpha()
        self.rect = self.surface.get_rect()  # Replacement de "pos" par le rectangle
        self.rect_type = "corner"

    def get(self) -> pygame.Surface:
        return self.surface

    def show(self):
        self.window.add_image(self.surface, self.rect)

    def convert_rect(self, convert):
        pass
