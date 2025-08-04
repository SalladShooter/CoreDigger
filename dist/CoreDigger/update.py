import pygame
from pygame import Surface
from addupgrade import AddUpgrade

pygame.init()

class Update:
    def __init__(self):
        self.collided = None
        self.addupgrade = AddUpgrade()

    def update(self):
        self.addupgrade.update()

    def check_mine(self, sprite, dirt_group):
        for dirt in dirt_group:
            if sprite.rect.colliderect(dirt.rect) and not dirt.explosive:
                dirt.kill()
                if hasattr(sprite, "energy"):
                    sprite.energy -= 1
                return True
        return False

    def check_wall(self, sprite, wall_group):
        for wall in wall_group:
            if sprite.rect.colliderect(wall.rect):
                sprite.move_to(sprite.prev_x / sprite.scale, sprite.prev_y / sprite.scale)
                return True
        return False

    def check_gem(self, sprite, gem_group, upgrade_group, select):
        for gem in gem_group:
            if sprite.rect.colliderect(gem.rect):
                gem.kill()
                if hasattr(gem, "heal_value"):
                    sprite.hearts += gem.heal_value
                elif hasattr(gem, "upgrade_value"):
                    sprite.upgrade += gem.upgrade_value
                    if sprite.upgrade >= sprite.max_upgrade:
                        select.selecting = True
                        sprite.can_move = False
                        self.addupgrade.new_upgrade(sprite, sprite.screen, sprite.scale, upgrade_group, select, self.addupgrade.selecting)
                if hasattr(sprite, "energy") and not hasattr(gem, "heal_value") and not hasattr(gem, "upgrade_value"):
                    sprite.energy += 10
                return True
        return False

    def check_explode(self, sprite, dirt_group):
        for dirt in dirt_group:
            if sprite.rect.colliderect(dirt.rect) and dirt.explosive:
                dirt.kill()
                if hasattr(sprite, "energy"):
                    sprite.energy -= 1
                if hasattr(sprite, "hearts"):
                    sprite.hearts -= 1
                return True
        return False

    def check_attack(self, sprite, enemy_group):
        for enemy in enemy_group:
            if sprite.rect.colliderect(enemy.rect):
                enemy.hearts -= sprite.damage
                if hasattr(sprite, "hearts"):
                    sprite.hearts -= enemy.damage
                return True
        return False
