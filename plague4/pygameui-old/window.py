#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Window class.

Base window object for Plague v0.4.
"""
import pygame

from pygameui.objects import Image


class Window(object):
    """Window object."""

    def __init__(self, /, icon: Image, title: str, subtitle: str, width: int = 500, height: int = 500):
        """Create a new window.

        Args:
            icon (Image): Path to icon file.
            title (str): Window title.
            subtitle (str): Window subtitle.
            width (int, optional): Width of the window.. Defaults to 500.
            height (int, optional): Height of the window. Defaults to 500.
        """
        self.icon: str = icon
        self.title: str = title
        self.subtitle: str = subtitle
        self.width: int = width
        self.height: int = height
        self.surface: pygame.Surface = pygame.display.set_mode(
            (self.width, self.height))
        pygame.display.set_caption(self.title, self.subtitle)
        pygame.display.set_icon(icon.get())
