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

scsize = (1000, 700) #ajout de tailles réglables à l'avenir

def calccenter(img):
	global scsize
	isl = img.get_size()
	return (scsize[0]/2-isl[0]/2,scsize[1]/2-isl[1]/2) #calcul condensé du centre de l'écran soustrait aux centre de l'image pour arriver pile au... milieu

window = pygame.display.set_mode(scsize)
pygame.display.set_caption("PLAGUE: Time Wanderer")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

window.fill(bgcolor) #remplir uniformément

splash = pygame.image.load("images/splash.png") #splash screen au démarrage
window.blit(splash, calccenter(splash)) #afficher le splash screen

progress = pygame.image.load("images/Progress.png")
window.blit(progress, calccenter(progress))

pygame.display.update() #ne pas oublier de rafraîchir l'écran !

main_loop = True

while main_loop:
	for event in pygame.event.get():
		if event.type == QUIT:
			main_loop = False

exit(0)