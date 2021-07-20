#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jeu vidéo.

Projet de jeu vidéo utilisant Python.
"""
import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((500, 500))

main_loop = True

while main_loop:
	for event in pygame.event.get():
		if event.type == QUIT:
			main_loop = False
