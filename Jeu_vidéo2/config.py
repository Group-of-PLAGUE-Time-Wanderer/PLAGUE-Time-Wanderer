import pygame

load = pygame.image.load

# Configuration du jeu
window = {
    "size": (1080, 740),
    "title": "PLAGUE: Time Wanderer",
    "icon": load("assets/icon.png"),
    "FPS": 999,  # Changing it later
}

# Alias
disp = pygame.display
screen = disp.set_mode(window["size"])
insert = screen.blit
refresh = disp.flip
clock = pygame.time.Clock()


def calccenter(img):
    global screen
    scsize = (screen.width, screen.height)
    isl = img.get_size()
    # calcul condensé du centre de l'écran soustrait aux centre de l'image pour arriver pile au... milieu
    return scsize[0]/2-isl[0]/2, scsize[1]/2-isl[1]/2
