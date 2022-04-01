import pygame.sprite
import objects.image
from math import fabs


class StaticObject(objects.image.Image):
    def __init__(self, window, image_path: str = "assets/images/placeholder.bmp"):
        super().__init__(window, image_path)

    def update(self, position):
        return self.image, position


class Entity(objects.image.Image):
    def __init__(self, window, max_vel, image_path=None):
        super().__init__(window, image_path)
        self.can_jump = False
        self.collide_with = pygame.sprite.Group()
        self.vx = 0
        self.vy = 0
        self.max_vel = max_vel

    def move(self, direction, force):
        if direction == "up":
            self.vy += force
        elif direction == "down":
            self.vy -= force
        elif direction == "right":
            self.vx += force
        elif direction == "left":
            self.vx -= force

        #
        is_max_y = (fabs(self.vy) > self.max_vel, 1 if fabs(self.vy) == self.vy else -1)
        is_max_x = (fabs(self.vx) > self.max_vel, 1 if fabs(self.vx) == self.vy else -1)

        if is_max_y[0]:
            self.vy = self.max_vel*is_max_y[1]
        if is_max_x[0]:
            self.vx = self.max_vel*is_max_x[1]

    def auto_move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def update(self):
        self.auto_move()
        self.insert(self.rect)
