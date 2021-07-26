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
        pygame.display.set_icon(icon)
        pygame.display.set_caption(self.title)

    def refresh(self):
        pygame.display.update()

    def bgfill(self, color):
        self.window.fill(color)
        self.refresh()

    def add_image(self, image, position):
        self.window.blit(image.get(), position)
        self.refresh()


class Image:
    def __init__(self, path):
        self.image = pygame.image.load(path)

    def get(self):
        return self.image
