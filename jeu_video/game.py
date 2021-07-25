#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jeu vidéo.

Projet de jeu vidéo utilisant Python.
"""
import pygame
from pygame.locals import *

pygame.init()

bgcolor = (52,51,67) #couleur de fond

longueur = 1000
largeur = 700 #ajout de tailles réglables à l'avenir

window = pygame.display.set_mode((longueur, largeur))
pygame.display.set_caption("PLAGUE: Time Wanderer")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

window.fill(bgcolor) #remplir uniformément
splash = pygame.image.load("images/splash.png") #splash screen au démarrage
tmppos = (longueur/2-300,largeur/2-261) #centrer l'image
window.blit(splash, tmppos) #afficher le splash screen
pygame.display.update() #ne pas oublier de rafraîchir l'écran !

main_loop = True

while main_loop:
	for event in pygame.event.get():
		if event.type == QUIT:
			main_loop = False

exit(0)