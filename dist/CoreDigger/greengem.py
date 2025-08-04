import pygame

pygame.init()

class GreenGem(pygame.sprite.Sprite):
    def __init__(self, screen, scale, x, y, upgrade_value):
        super().__init__()
        self.screen = screen
        self.scale = scale
        self.x = x
        self.y = y
        self.upgrade_value = upgrade_value
        self.asset_image = "assets/MoneyGem.png"
        loaded_image = pygame.image.load(self.asset_image).convert_alpha()
        self.image = pygame.transform.scale(loaded_image, (8 * self.scale, 8 * self.scale))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
