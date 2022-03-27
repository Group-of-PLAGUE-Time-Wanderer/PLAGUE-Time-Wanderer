#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Plague 4 - Translations.

Module for Plague 4 translations, provide Translator object.
"""
import configparser
from typing import Optional


class Translator(object):
    """Base class for translation"""
    def __init__(self, locale: str) -> None:
        """Initialize translator.

        Args:
            locale (str): Locale to translate (fr, en, de).
        """
        self.config: configparser.ConfigParser = configparser.ConfigParser()
        self.config.read(f"locales/{locale}.ini")
        self.section: Optional[str] = None
    
    def __getitem__(self, key: str) -> str:
        """Simple implementation of object[].

        Args:
            key (Any): Key to get.

        Returns:
            str: Translation.
        """
        return self.config.__getitem__(key)
    
    def work(self, section: str) -> None:
        """Set current working section.

        Args:
            section (str): Working section of INI file.
        """
        self.section: Optional[str] = section
    
    def get(self, key: str, section: str=None) -> str:
        """Get a translated string from a key.

        Args:
            key (str): Key of string to get.
            section (str, optional): Section to get key. Defaults to current working section.

        Returns:
            str: Translated string.
        """
        if section is None:
            return self.config[self.section][key]
        else:
            return self.config[section][key]
