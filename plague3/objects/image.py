#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Image object
"""
import pygame
import objects


class Image(pygame.sprite.Sprite):
    """Basic class for importing images."""
    def __init__(self, window, /, path: str = "assets/images/placeholder.bmp"):
        super().__init__()
        self.window = window
        self.path = path
        self.image = pygame.image.load(self.path).convert_alpha()
        self.rect = self.image.get_rect()  # Replacement de "pos" par le rectangle
        self.rect_type = "corner"

    def get(self) -> pygame.Surface:
        return self.image

    def insert(self, surface: objects.window):
        self.window.add_image(surface, self.rect)

    def convert_rect(self, convert_to: str):
        if convert_to == "centered":
            self.rect = self.image.get_rect(center=self.rect.center)
        elif convert_to == "static" or convert_to == "default":
            self.rect = self.image.get_rect()
        else:
            raise ValueError(f"Rect can be centered or static, got {convert_to}.")
