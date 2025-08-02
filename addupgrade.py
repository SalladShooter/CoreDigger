import pygame
import random
from upgrade import Upgrade

pygame.init()

class AddUpgrade(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.upgrades = [
            "hearts",
            "energy",
            "damage",
        ]
        self.selecting = False
        self.select = None
    def new_upgrade(self, player, screen, scale, upgrade_group, select, selecting):
        self.select = select
        self.selecting = True
        self.upgrade_group = upgrade_group
        items = []
        self.upgrade_group.empty()
        for _ in range(3):
            items.append(random.randint(0,2))
        for _ in range(3):
            upgrade = Upgrade(screen, scale, _ * 16 * scale, 48 * scale, items[_], True)
            self.upgrade_group.add(upgrade)
        self.select.change_selecting(True, items)

    def update(self):
        if hasattr(self.select, "selecting") and not self.select.selecting:
            self.upgrade_group.empty()
