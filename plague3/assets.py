#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Load game assets
"""
import json

with open("plague3/assets.json") as assets_file:
    assets = json.load(assets_file)
