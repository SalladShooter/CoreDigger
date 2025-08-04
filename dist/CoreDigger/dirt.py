import pygame

pygame.init()

class Dirt(pygame.sprite.Sprite):
    def __init__(self, screen, scale, x, y, explosive=False):
        super().__init__()
        self.screen = screen
        self.scale = scale
        self.x = x
        self.y = y
        self.explosive = explosive
        if self.explosive:
            self.asset_image = "assets/ExplosiveDirt.png"
        else: 
            self.asset_image = "assets/Dirt.png"
        loaded_image = pygame.image.load(self.asset_image).convert_alpha()
        self.image = pygame.transform.scale(loaded_image, (8 * self.scale, 8 * self.scale))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
