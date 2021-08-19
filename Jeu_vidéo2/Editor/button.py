#!/user/bin/python
# coding: utf-8
import pygame


class TextButton:
    def __init__(self, rect: pygame.Rect, normal, hover=None):
        self.rect = rect
        self.disp_normal = normal
        self.disp_hover = hover
        self.is_hovering = False

    def testforcollision(self, pos, event):
        if self.rect.collidepoint(pos):
            self.is_hovering = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("!click")
        else:
            self.is_hovering = False

    def update(self, window):
        if self.disp_hover and self.is_hovering:
            window.blit(self.disp_hover, self.rect)
        else:
            window.blit(self.disp_normal, self.rect)
