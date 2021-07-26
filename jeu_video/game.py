#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jeu vidéo.

Projet de jeu vidéo utilisant Python.
"""
import pygame
from pygame.locals import *
import physics

pygame.init()

main_window = physics.Window(1000, 700, "PLAGUE: Time Wanderer", physics.Image("images/icon.png").get())

bgcolor = (52,51,67) #couleur de fond

def calccenter(img):
	global main_window
	scsize = (main_window.width, main_window.height)
	isl = img.get().get_size()
	return (scsize[0]/2-isl[0]/2,scsize[1]/2-isl[1]/2) #calcul condensé du centre de l'écran soustrait aux centre de l'image pour arriver pile au... milieu


main_window.bgfill(bgcolor)

splash = physics.Image("images/splash.png") #splash screen au démarrage
main_window.add_image(splash, calccenter(splash)) #afficher le splash screen

progress = physics.Image("images/Progress.png")
progress_y = calccenter(progress)[1]-(0-main_window.height*0.3) #centre y - 30% de la taille de l'écran
main_window.add_image(progress, (calccenter(progress)[0], progress_y))

main_loop = True

while main_loop:
	for event in pygame.event.get():
		if event.type == QUIT:
			main_loop = False

exit(0)
