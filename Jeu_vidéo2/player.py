#!/usr/bin/python
# coding: utf-8
from config import *
import physics


class Player(physics.GravitySprite):
    def __init__(self, controls: dict):
        super().__init__(controls)
        self.image = load("assets/player.bmp")
