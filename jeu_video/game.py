# -*- coding: utf-8 -*-
"""
PLAGUE: Time Wanderer

Python Video Game.
"""
import pygame
import game_utils
import widgets
import sentry_sdk  # Sentry bug tracking
import time

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

progress = game_utils.Image("images/Progress.png")
progressed = game_utils.Image("images/progressed.png")
progress = widgets.ProgressBar(main_window, 0, 200, progress, progressed, 18)
main_window.bgfill(bgcolor)
progress.update()
splash = game_utils.Image("images/splash.png")  # splash screen au démarrage
progress.update()
launch_button = game_utils.Image("images/launch_button.png")
progress.update()
main_window.add_image(splash, (0, 0))  # afficher le splash screen
progress.update()
button = widgets.Button(main_window, 0, 250, launch_button)
progress.update()
def click():
    print("click")
progress.update()
button.onclick(click)
progress.update()
while progress.available():
    time.sleep(0.01)
    progress.update()
del progress
button.show()
while not main_window.check_close():
    main_window.reload()
    button.events()
    time.sleep(1)

main_window.main_loop()

exit(0)
