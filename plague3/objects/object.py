import pygame.sprite
import keys
import objects.image


class StaticObject(objects.image.Image):
    def __init__(self, window, image_path: str = "assets/images/placeholder.bmp"):
        super().__init__(window, image_path)

    def update(self, position):
        return self.image, position


class Entity(objects.image.Image):
    def __init__(self, window, image_path, controllable: bool = True, controls: dict = None):
        super().__init__(window, image_path)
        if controllable:
            self.left_ctrl = keys.get_key(controls["left"])
            self.right_ctrl = keys.get_key(controls["right"])
            self.jump_ctrl = keys.get_key(controls["jump"])
            self.down_ctrl = keys.get_key(controls["down"])
            self.up_ctrl = keys.get_key(controls["up"])

            self.can_jump = False

        self.collide_with = pygame.sprite.Group()
