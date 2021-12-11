#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Plague 4 - Translations.

Module for Plague 4 translations, provide Translator object.
"""
import configparser


class Translator(object):
    """Base class for translation"""
    def __init__(self, locale: str) -> None:
        """Initialize translator.

        Args:
            locale (str): Locale to translate (fr, en, de).
        """
        self.config = configparser.ConfigParser()
        self.config.read(f"locales/{locale}.ini")
        self.section = None
    
    def __getitem__(self, key) -> str:
        """Simple implementation of object[].

        Args:
            key (Any): Key to get.

        Returns:
            str: Translation.
        """
        return self.config.__getitem__(key)
    
    def work(self, section: str) -> None:
        self.section = section
    
    def get(self, key, section=None) -> str:
        
