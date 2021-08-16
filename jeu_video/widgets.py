#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PLAGUE: Time Wanderer - Widgets.

All the widgets for the game.
"""
import sys
import pygame
from game_utils import Image, Window


class ProgressBar:
    """Progress bar widget."""
    def __init__(self, outer: Image, inner: Image, x: int, y: int, infinite: bool = False):
        """Initialize progress bar.

        :param Image outer: The progress bar outer image.
        :param Image inner: The progress bar inner image.
        :param int x: X position of the progress bar
        :param int y: Y position of the progress bar
        :param bool infinite: Perpetual progress bar or not.

        """
        self.outer: Image = outer
        self.inner: Image = inner
        self.infinite: bool = infinite
        self.x: int = x
        self.y: int = y
        self.state: float = 0

    def update(self):
        """
        Change progression.

        @return: self
        """
        self.state += 1
        return self

    def show(self, window: Window):
        """
        Show progress bar.

        @param window: Window
        @return: self
        """
        window.load_image(self.outer, (self.x, self.y))
        window.load_image(self.inner, (self.x + 1 + self.state, self.y))
        window.refresh()
        if window.check_close():
            sys.exit(1)
        return self
