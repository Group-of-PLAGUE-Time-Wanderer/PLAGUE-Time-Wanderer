#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PLAGUE: Time Wanderer - Widgets.

All the widgets for the game.
"""
import sys
import pygame
from jeu_video.game_utils import Image, Window, center_coords

function_type = type(sys.exit)


class Widget:
    """
    Base class for widgets.
    """

    def __init__(self, subclass):
        print(f"Widget: {type(subclass).__name__} loaded")


class ProgressBar(Widget):
    """Progress bar widget."""

    def __init__(self, window: Window, x: int, y: int, outer: Image, inner: Image, border: int = 1):
        """Initialize progress bar.

        :param Image outer: The progress bar outer image.
        :param Image inner: The progress bar inner image.
        :param int x: X position of the progress bar
        :param int y: Y position of the progress bar
        :param bool infinite: Perpetual progress bar or not.

        """
        super().__init__(self)
        self.window: Window = window
        self.outer: Image = outer
        self.inner: Image = inner
        self.border: int = border
        self.x: int = x
        self.y: int = y
        self.state: float = 0

    def __del__(self):
        self.window.clear()
        self.window.reload()
        self.window.refresh()

    def update(self):
        """
        Change progression.

        @return: self
        """
        self.state += 1
        return self.show()

    def available(self):
        """
        Check if there is available progression.
        """
        return self.state < (self.outer.width - self.border * 2) - self.inner.width

    def show(self):
        """
        Show progress bar.

        @return: self
        """
        self.window.load_image(self.outer, (self.x, self.y))
        for state in range(self.state):
            x_position = self.x - self.outer.width / 2 + self.inner.width / 2 + self.border + state
            self.window.load_image(self.inner, (x_position, self.y))
        self.window.refresh()
        if self.window.check_close():
            sys.exit(1)
        return self


class Button(Widget):
    """
    Button widget.
    """

    def __init__(self, window: Window, x: int, y: int, image: Image):
        super().__init__(self)
        self.window = window
        self.x = x
        self.y = y
        self.image = image
        self.click = None

    def onclick(self, func: function_type):
        self.click = func

    def events(self):
        for event in self.window.events():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Click: {event.pos}")
                print(f"Center: {event.pos[0] - (self.window.width / 2)}, {event.pos[1] - (self.window.height / 2)}")

    def show(self):
        self.window.load_image(self.image, (self.x, self.y))
        self.window.refresh()
