import pygame

pygame.init()

class Upgrade(pygame.sprite.Sprite):
    def __init__(self, screen, scale, x, y, selected_image):
        super().__init__()
        self.screen = screen
        self.scale = scale
        self.x = x
        self.y = y
        self.asset_images = [
            "assets/Sword.png"
        ]
        self.select_image = selected_image
        loaded_image = pygame.image.load(self.asset_images[self.selected_image], (8 * self.scale, 8 * self.scale))
        self.image = pygame.transform.scale(loaded_image, (8 * self.scale, 8 * self.scale))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
