from config import *


class ProgressBar(pygame.sprite.Sprite):
    def __init__(self, pos: tuple = (0, 0), height: int = 10, full_size: int = 100,
                 color: tuple = (255, 255, 255), back_color: tuple = (0, 0, 0)):
        super().__init__()
        self.size = 0
        self.full_size = full_size*10
        self.position = pos
        self.color = color
        self.back_color = back_color
        self.height = height

    def resize(self, value):
        if self.size < self.full_size:
            self.size = value*10
        pygame.draw.rect(screen, self.back_color,
                         [self.position[0], self.position[1],
                          self.full_size, self.height])

        pygame.draw.rect(screen, self.color,
                         [self.position[0], self.position[1],
                          self.size, self.height])
