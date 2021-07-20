#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jeu vidéo - Installation.

Installation du jeu vidéo.
"""
import pkgutil

required_modules = ["pygame"]

def get_installed_packages():
    module_list = list()
    for module in pkgutil.iter_modules():
        module_name = module.name
        if module_name in required_modules:
            module_list.append(module_name)
    return module_list

print("Bienvenue dans le programme d'installation de Jeu vidéo !")
print("Paquets dèja installés :")
print("   ", "\t".join(get_installed_packages()))
