import pygame

pygame.init()

class Gem(pygame.sprite.Sprite):
    def __init__(self, screen, scale, x, y):
        super().__init__()
        self.screen = screen
        self.scale = scale
        self.x = x
        self.y = y
        self.asset_image = "assets/Gem.png"
        loaded_image = pygame.image.load(self.asset_image).convert_alpha()
        self.image = pygame.transform.scale(loaded_image, (8 * self.scale, 8 * self.scale))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
