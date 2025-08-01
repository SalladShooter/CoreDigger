import pygame

pygame.init()

class Text(pygame.sprite.Sprite):
    def __init__(self, screen, scale, text, x, y):
        super().__init__()
        self.screen = screen
        self.scale = scale
        self.text_group = pygame.sprite.Group()
        self.x = x
        self.y = y
        self.font = pygame.font.Font("assets/font/smallest_pixel-7.ttf", 6 * self.scale)
        text_surface = self.font.render(text, False, (255, 255, 255))
        self.image = pygame.transform.scale(text_surface, (6 * len(text) * self.scale, 7 * self.scale))
        self.rect = self.image.get_rect(topleft=(self.x * self.scale, self.y * self.scale))

    def change_text(self, new_text):
        text_surface = self.font.render(new_text, False, (255, 255, 255))
        self.image = pygame.transform.scale(text_surface, (6 * len(new_text) * self.scale, 7 * self.scale))
        self.rect = self.image.get_rect(topleft=(self.x * self.scale, self.y * self.scale))
