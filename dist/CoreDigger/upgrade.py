import pygame

pygame.init()

class Upgrade(pygame.sprite.Sprite):
    def __init__(self, screen, scale, x, y, selected_image, ui=False):
        super().__init__()
        self.screen = screen
        self.scale = scale
        self.x = x
        self.y = y
        self.asset_images = [
            "assets/HeartUpgrade.png",
            "assets/EnergyUpgrade.png",
            "assets/SwordUpgrade.png",
        ]
        self.selected_image = selected_image
        self.ui = ui
        loaded_image = pygame.image.load(self.asset_images[self.selected_image]).convert_alpha()
        self.image = pygame.transform.scale(loaded_image, (8 * self.scale, 8 * self.scale))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
