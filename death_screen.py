import pygame
from text import Text

pygame.init()

class Death_Screen:
    def __init__(self, screen, scale, player):
        self.screen = screen
        self.scale = scale
        self.player = player
        self.text_group = pygame.sprite.Group()
        self.middle = self.screen.get_width() / 2 / 8
        self.game_over_text = self.add_text_screen("Game Over", self.middle - 26, 0)
        self.player_depth_text = self.add_text_screen(f"{self.player.depth}m", self.middle - 6, 2 * self.scale)
        self.reset_text_first = self.add_text_screen("ENTER/SPACE", self.middle - 30, 11 * self.scale)
        self.reset_text_last = self.add_text_screen("To Exit", self.middle - 18, 12 * self.scale)
        self.start = False

    def add_text_screen(self, text, x, y):
        text_surface = Text(self.screen, self.scale, text, x, y)
        self.text_group.add(text_surface)
        return text_surface

    def update_text(self):
        self.game_over_text.change_text("Game Over")
        self.player_depth_text.change_text(f"{self.player.depth}m")
        self.reset_text_first.change_text("ENTER/SPACE")
        self.reset_text_last.change_text("To Exit")
        self.player_depth_text.move_text((len(f"{self.player.depth}m") + 3.25) * self.scale, 2 * self.scale)

    def render(self):
        self.update_text()
        self.text_group.draw(self.screen)

    def restart(self, event, hearts, max_hearts, energy, max_energy, upgrade, max_upgrade):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                self.start = True
                self.player.hearts = hearts
                self.player.max_hearts = max_hearts
                self.player.energy = energy
                self.player.max_energy = max_energy
                self.player.upgrade = upgrade
                self.player.max_upgrade = max_upgrade
