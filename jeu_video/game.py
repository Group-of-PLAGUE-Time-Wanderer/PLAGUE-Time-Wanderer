# -*- coding: utf-8 -*-
"""
PLAGUE: Time Wanderer

Python Video Game.
"""
import pygame
import game_utils
import sentry_sdk  # Sentry bug tracking

sentry_sdk.init(
    "https://5d1eb25621ff48679b0a91f045593c73@o936010.ingest.sentry.io/5886066",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)
pygame.init()

main_window = game_utils.Window(
    1000, 700, "PLAGUE: Time Wanderer", "images/icon.png")

bgcolor = (52, 51, 67)  # couleur de fond


def calccenter(img):
    global main_window
    scsize = (main_window.width, main_window.height)
    isl = img.get().get_size()
    # calcul condensé du centre de l'écran soustrait aux centre de l'image pour arriver pile au... milieu
    return scsize[0]/2-isl[0]/2, scsize[1]/2-isl[1]/2


main_window.bgfill(bgcolor)

splash = game_utils.Image("images/splash.png")  # splash screen au démarrage
main_window.add_image(splash, (0, 0))  # afficher le splash screen

progress = game_utils.Image("images/Progress.png")
progressed = game_utils.Image("images/progressed.png")
main_window.add_image(progress, (0, 200))
main_window.add_image(progressed, (-301, 200))

main_window.main_loop()

exit(0)
