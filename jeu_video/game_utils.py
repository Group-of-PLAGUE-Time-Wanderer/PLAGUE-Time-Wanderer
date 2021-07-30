#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projet du jeu vidéo - Moteur de jeu.

Ce script rassemblera tous les éléments pour le fonctionnement du jeu
"""
import time
import pygame
from pygame.locals import *

pygame.init()


def center_coords(coords, image, window):
    image_size = image.get().get_size()
    image_center = (image_size[0] / 2, image_size[1] / 2)
    centered_coords = (coords[0] + window.width / 2 - image_center[0],
                       coords[1] + window.height / 2 - image_center[1])
    return centered_coords


class physic:
    pass


class Window:
    def __init__(self, width, height, title, icon):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.title = title
        self.icon = Image(icon).get()
        self.images = list()
        self.bg = None
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption(self.title)

    def refresh(self):
        pygame.display.flip()

    def bgfill(self, color):
        self.bg = color
        self.window.fill(color)

    def image_center(self, image):
        image_size = image.get().get_size()
        image_center = (image_size[0] / 2, image_size[1] / 2)
        return image_center

    def add_image(self, image, position):
        self.images.append((image, position))
        self.load_image(image, position)

    def load_image(self, image, position):
        self.window.blit(image.get(),
                         center_coords(position, image, self))

    def main_loop(self):
        main_loop = True
        print(self.images)
        while main_loop:
            print("loop")
            for event in pygame.event.get():
                if event.type == QUIT:
                    main_loop = False
            if self.bg:
                self.bgfill(self.bg)
            for image in self.images:
                print(image[0])
                self.load_image(image[0], image[1])
            self.refresh()


class Image:
    def __init__(self, path):
        self.path = path
        self.image = pygame.image.load(path).convert_alpha()

    def get(self):
        return self.image

    def __str__(self):
        return "Image from " + self.path
