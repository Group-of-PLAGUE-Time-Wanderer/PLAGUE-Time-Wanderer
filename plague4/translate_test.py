#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test translate module."""
import configparser
import os

import pygameui.translate

os.chdir("plague4")


def test_load():
    trans = pygameui.translate.Translator("fr")
    assert type(trans) == pygameui.translate.Translator


def test_getattr():
    trans = pygameui.translate.Translator("fr")
    assert type(trans["TestSection"]) == configparser.SectionProxy
    assert type(trans["TestSection"]["Test"]) == str
    assert trans["TestSection"]["Test"] == "TEST STRING - IGNORE IT: fr"


def test_work():
    trans = pygameui.translate.Translator("fr")
    trans.work("TestSection")
    assert trans.section == "TestSection"
    assert type(trans.get("Test")) == str
    assert trans.get("Test") == "TEST STRING - IGNORE IT: fr"


def test_get():
    trans = pygameui.translate.Translator("fr")
    assert type(trans.get("Test", "TestSection")) == str
    assert trans.get("Test", "TestSection") == "TEST STRING - IGNORE IT: fr"
