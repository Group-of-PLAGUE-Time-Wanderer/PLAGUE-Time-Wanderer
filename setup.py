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

def get_missing_packages(installed_packages):
    module_list = required_modules
    module_list.append("jeu_video")
    for module in installed_packages:
        module_list.remove(module)
    return module_list

installed_packages = get_installed_packages()
missing_packages = get_missing_packages(installed_packages)

print("Bienvenue dans le programme d'installation de Jeu vidéo !")
print()
print("Paquets dèja installés :")
print("   ", "\t".join(installed_packages))
print("Paquets à installer :")
print("   ", "\t".join(missing_packages))
