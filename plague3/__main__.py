#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PLAGUE: Time Wanderer - Version 3.0.1

Mix of precedent versions of Plague.
"""
import pygame.event
import objects
import json

with open("config.json") as config_file:
    config = json.load(config_file)

main_window = objects.window.NewWindow(config["assets"]["icon"], "Plague: Time Wanderer EarlyDev v3",
                                       "Time Wanderer ED3", config["screen"]["size"][0], config["screen"]["size"][1])

clock = pygame.time.Clock()
running = True
current_state = "menu"

while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Displaying
    # Refreshing
    pygame.display.flip()

    clock.tick(config["screen"]["FPS"])

pygame.quit()
