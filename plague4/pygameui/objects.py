#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Objects for pygameui."""
import pygame


class Image:
    """Base class for images."""

    def __init__(self, path: str):
        """Create new image.

        Args:
            path (str): Path to image.
        """
        self.surface: pygame.Surface = pygame.image.load(path)

    def get(self) -> pygame.Surface:
        """Get Surface object.

        Returns:
            pygame.Surface: Surface object.
        """
        return self.surface
