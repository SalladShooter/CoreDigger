import pygame
from text import Text

pygame.init()

class Main_Screen:
    def __init__(self, screen, scale):
        self.screen = screen
        self.scale = scale
        self.text_group = pygame.sprite.Group()
        self.middle = self.screen.get_width() / 2 / 8
        self.title_text = self.add_text_screen("CoreDigger", self.middle - 28, 0)
        self.start_text_first = self.add_text_screen("ENTER/SPACE", self.middle - 30, 11 * self.scale)
        self.start_text_last = self.add_text_screen("To Start", self.middle - 18, 12 * self.scale)
        self.start = False

    def add_text_screen(self, text, x, y):
        text_surface = Text(self.screen, self.scale, text, x, y)
        self.text_group.add(text_surface)
        return text_surface

    def update_text(self):
        self.title_text.change_text("CoreDigger")
        self.start_text_first.change_text("ENTER/SPACE")
        self.start_text_last.change_text("To Start")

    def render(self):
        self.update_text()
        self.text_group.draw(self.screen)

    def start_game(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                self.start = True
