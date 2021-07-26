#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jeu vidéo.

Projet de jeu vidéo utilisant Python.
"""
import pygame
from pygame.locals import *
import game_utils

pygame.init()

main_window = game_utils.Window(1000, 700, "PLAGUE: Time Wanderer", game_utils.Image("images/icon.png").get())

bgcolor = (52,51,67) #couleur de fond

def calccenter(img):
	global main_window
	scsize = (main_window.width, main_window.height)
	isl = img.get().get_size()
	return (scsize[0]/2-isl[0]/2,scsize[1]/2-isl[1]/2) #calcul condensé du centre de l'écran soustrait aux centre de l'image pour arriver pile au... milieu


main_window.bgfill(bgcolor)

splash = game_utils.Image("images/splash.png") #splash screen au démarrage
main_window.add_image(splash, (0, 0)) #afficher le splash screen

progress = game_utils.Image("images/Progress.png")
progressed = game_utils.Image("images/progressed.png")
main_window.add_image(progress, (0, 200))
main_window.add_image(progressed, (-301, 200))

main_window.main_loop()

exit(0)
