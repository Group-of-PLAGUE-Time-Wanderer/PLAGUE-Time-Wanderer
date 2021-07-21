#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jeu vidéo - Installation.

Installation du jeu vidéo.
"""
import os
import sys
import pkgutil
import requests

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

def detect_python():
    test = os.system("python3 --version > " + os.devnull)
    if test == 0:
        return "python3"
    test = os.system("py -3 --version > " + os.devnull)
    if test == 0:
        return "py -3"
    print()
    print("/!\\ Votre installation Python est instrouvable ! Merci d'installer Python et de vérifier qu'il peut être lancé avec la commande 'python3'.")
    sys.exit(1)

def detect_pip(python):
    print("Détection de l'installateur de paquets...", end=" ", flush=True)
    test = os.system(python + " -m pip > " + os.devnull)
    print("Terminé.")
    if test == 0:
        return
    print("Installation de l'installateur de paquets...", end=" ", flush=True)
    test = os.system(python + " get-pip.py > " + os.devnull)
    print("Terminé.")
    if test == 0:
        return
    print()
    print("/!\\ Echec de l'installationde pip.")
    sys.exit(1)

def install_mods(mods, python):
    print("Téléchargement en cours...")
    for mod in mods:
        if mod == "pip":
            print("Téléchargement: https://bootstrap.pypa.io/get-pip.py...", end=" ", flush=True)
            r = requests.get("https://bootstrap.pypa.io/get-pip.py", stream=True)
            with open("file_name.pdf", 'wb') as f:
                f.write(r.read())
            print("Terminé.")
        elif mod == "jeu_video":
            print("Téléchargement: https://gitlab.com/groupe-jeu-vid-o/jeu-video/-/archive/main/jeu-video-main.zip...", end=" ", flush=True)
            r = requests.get("https://gitlab.com/groupe-jeu-vid-o/jeu-video/-/archive/main/jeu-video-main.zip", stream=True)
            with open("file_name.pdf", 'wb') as f:
                f.write(r.read())
            print("Terminé.")
        else:
            print("Téléchargement: https://pypi.org/simple/{0}/...".format(mod), end=" ", flush=True)
            os.system(python + " -m pip download " + mod + " > " + os.devnull)
            print("Terminé.")
    print("Téléchargement terminé. Installation en cours...")

def install():
    print("Détection de l'installation python...", end=" ", flush=True)
    python = detect_python()
    print("Terminé.")
    detect_pip(python)

installed_packages = get_installed_packages()
missing_packages = get_missing_packages(installed_packages)

print("Bienvenue dans le programme d'installation de Jeu vidéo !")
print()
print("Paquets dèja installés :")
print("   ", "\t".join(installed_packages))
print("Paquets à installer :")
print("   ", "\t".join(missing_packages))
answer = input("Continuer ? [O/n] ")
if not answer or answer.lower() in ("o", "oui"):
    answer = True
elif answer.lower() in ("n", "non"):
    answer = False
else:
    print("Réponse invalide. Annulation...")
    answer = False

if not answer:
    print("Installation annulée.")
else:
    install()
