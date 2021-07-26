#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PLAGUE: Time Wanderer - Widgets.

All the widgets for the game.
"""
import pygame
from game_utils import Image


class ProgressBar:
    """Short summary."""
    def __init__(self, outer: Image, inner: Image, x: int, y: int, infinite: bool=False):
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

    def show(self, window):
