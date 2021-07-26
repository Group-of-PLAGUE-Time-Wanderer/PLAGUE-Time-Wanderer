#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projet du jeu vidéo - Moteur de jeu.

Ce script rassemblera tous les éléments pour le fonctionnement du jeu
"""
import pygame
from pygame.locals import *

pygame.init()


class physic:
    pass


class Window:
    def __init__(self, width, height, title, icon):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.title = title
        self.icon = icon
        self.images = list()
        self.bg = None
        pygame.display.set_icon(icon)
        pygame.display.set_caption(self.title)

    def refresh(self):
        pygame.display.update()

    def bgfill(self, color):
        self.bg = color
        self.window.fill(color)
        self.refresh()

    def image_center(self, image):
        image_size = image.get().get_size()
        image_center = (image_size[0] / 2, image_size[1] / 2)
        return image_center

    def center_coords(self, coords, image):
        image_size = image.get().get_size()
        image_center = (image_size[0] / 2, image_size[1] / 2)
        centered_coords = (coords[0] + self.width / 2 - image_center[0], coords[1] + self.height / 2 - image_center[1])
        return centered_coords

    def add_image(self, image, position):
        self.images.append((image, position))
        self.window.blit(image.get(), self.center_coords(position, image))
        self.refresh()

    def main_loop(self):
        main_loop = True
        while main_loop:
            for event in pygame.event.get():
                if event.type == QUIT:
                    main_loop = False
            if self.bg:
                self.bgfill(self.bg)
            for image in self.images:
                self.add_image(image[0], image[1])

class Image:
    def __init__(self, path):
        self.image = pygame.image.load(path)

    def get(self):
        return self.image
