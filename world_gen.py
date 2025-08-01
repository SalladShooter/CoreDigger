import pygame
from update import Update
from player import Player
from upgrade import Upgrade
from wall import Wall
from dirt import Dirt
from gem import Gem
from redgem import RedGem
from text import Text
from heart import Heart
from energy import Energy
from enemy import Enemy

import random


class World_Gen:
    def __init__(self, screen, scale, player):
        self.screen = screen
        self.scale = scale
        self.player = player

        self.dirt_group = pygame.sprite.Group()
        self.wall_group = pygame.sprite.Group()
        self.gem_group = pygame.sprite.Group()
        self.text_group = pygame.sprite.Group()
        self.ui_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.upgrade_group = pygame.sprite.Group()

        self.world = ["    ############"]

        self.path_col = random.randint(5,15)
        self.row_width = 12
        self.generate_row("h", True)
        self.generate_row("/", False)
        self.generate_row("S", False)
        for _ in range(12):
            self.generate_row()

        self.add_sprites(self.world, 0, 0)

    def add_sprites(self, world, start_row, start_col):
        for row in range(start_row, len(world)):
            for col in range(start_col, len(world[row])):
                char = world[row][col]
                x_pix = col * 8 * self.scale
                y_pix = row * 8 * self.scale

                if char == "d":
                    dirt = Dirt(self.screen, self.scale, x_pix, y_pix)
                    self.dirt_group.add(dirt)
                elif char == "x":
                    explosive_dirt = Dirt(self.screen, self.scale, x_pix, y_pix, True)
                    self.dirt_group.add(explosive_dirt)
                elif char == "p":
                    self.player.move_to(col * self.scale, row * self.scale)
                    self.player.render()
                elif char == "#":
                    wall = Wall(self.screen, self.scale, x_pix, y_pix)
                    self.wall_group.add(wall)
                elif char == "$":
                    gem = Gem(self.screen, self.scale, x_pix, y_pix)
                    self.gem_group.add(gem)
                elif char == "g":
                    redgem = RedGem(self.screen, self.scale, x_pix, y_pix, 1)
                    self.gem_group.add(redgem)
                elif char == "h":
                    heart = Heart(self.screen, self.scale, x_pix, y_pix)
                    self.ui_group.add(heart)
                elif char == "/":
                    energy = Energy(self.screen, self.scale, x_pix, y_pix)
                    self.ui_group.add(energy)
                elif char == "e":
                    enemy = Enemy(self.screen, self.scale, x_pix, y_pix, 1, 1)
                    enemy.move_to(x_pix / 8, y_pix / 8)
                    enemy.render()
                    self.enemy_group.add(enemy)
                elif char == "H":
                    heart = Upgrade(self.screen, self.scale, x_pix, y_pix, 0, True)
                    if heart.ui:
                        self.ui_group.add(heart)
                    else:
                        self.upgrade_group.add(heart)
                elif char == "E":
                    energy = Upgrade(self.screne, self.scale, x_pix, y_pix, 1, True)
                    if energy.ui:
                        self.ui_group.add(energy)
                    else:
                        self.upgrade_group.add(energy)
                elif char == "S":
                    sword = Upgrade(self.screen, self.scale, x_pix, y_pix, 2, True)
                    if sword.ui:
                        self.ui_group.add(sword)
                    else:
                        self.upgrade_group.add(sword)
        self.player_hearts_text = self.add_text_screen(f"*{self.player.hearts}", 8, 8)
        self.player_energy_text = self.add_text_screen(f"*{self.player.energy}", 8, 16)
        self.player_damage_text = self.add_text_screen(f"*{self.player.damage}", 8, 24)
        self.update = Update()

    def add_text_screen(self, text, x, y):
        text_surface = Text(self.screen, self.scale, text, x, y)
        self.text_group.add(text_surface)
        return text_surface

    def render_world(self):
        self.update.check_mine(self.player, self.dirt_group)
        self.update.check_explode(self.player, self.dirt_group)
        self.update.check_wall(self.player, self.wall_group)
        self.update.check_gem(self.player, self.gem_group)
        self.update.check_attack(self.player, self.enemy_group)

        if self.player.generate_world:
            self.generate_world()

        for enemy in self.enemy_group:
            if enemy.hearts <= 0:
                enemy.kill()
            enemy.render()
        self.player.render()
        self.wall_group.draw(self.screen)
        self.gem_group.draw(self.screen)
        self.dirt_group.draw(self.screen)
        self.update_text()
        self.text_group.draw(self.screen)
        self.ui_group.draw(self.screen)
        self.upgrade_group.draw(self.screen)

    def generate_row(self, ui_level=" ", player=False):
        move = random.choice([-1, 0, 1])
        new_path_col = self.path_col + move
        min_col = 1
        max_col = self.row_width - 2
        self.path_col = max(min_col, min(new_path_col, max_col))

        if player:
            rand_gen = ""
            for col in range(1, self.row_width - 1):
                if col == self.path_col:
                    rand_gen += "p"
                else:
                    rand_gen += "d"

            rand_gen += "#"
            self.world.append(f"{ui_level}   #{rand_gen}")
            return

        rand_gen = ""
        for col in range(1, self.row_width - 1):
            if col == self.path_col:
                rand_gen += "d"
            else:
                tile_choice = random.choices(['x', '$', 'g', 'd', 'e'], weights=[31, 3, 3, 60, 3])[0]

                if abs(col - self.path_col) == 1 and tile_choice == 'x':
                    tile_choice = 'd'

                rand_gen += tile_choice
        rand_gen += "#"

        self.world.append(f"{ui_level}   #{rand_gen}")

    def generate_world(self):
        self.player.generate_world = False

        self.world.pop(0)
        self.generate_row()

        tile_height = 8 * self.scale

        def remove_top_row_sprites(sprite_group):
            for sprite in sprite_group.sprites():
                if sprite.rect.top < tile_height:
                    sprite.kill()

        remove_top_row_sprites(self.dirt_group)
        remove_top_row_sprites(self.wall_group)
        remove_top_row_sprites(self.gem_group)
        remove_top_row_sprites(self.enemy_group)

        def move_sprites_up(sprite_group):
            for sprite in sprite_group.sprites():
                sprite.rect.y -= tile_height

        move_sprites_up(self.dirt_group)
        move_sprites_up(self.wall_group)
        move_sprites_up(self.gem_group)
        move_sprites_up(self.enemy_group)

        self.player.rect.y -= tile_height

        new_row_index = len(self.world) - 1
        row = self.world[new_row_index]
        for col, char in enumerate(row):
            x_pix = col * 8 * self.scale
            y_pix = new_row_index * 8 * self.scale
            if char == "d":
                dirt = Dirt(self.screen, self.scale, x_pix, y_pix)
                self.dirt_group.add(dirt)
            elif char == "x":
                explosive_dirt = Dirt(self.screen, self.scale, x_pix, y_pix, True)
                self.dirt_group.add(explosive_dirt)
            elif char == "p":
                self.player.move_to(x_pix, y_pix)
                self.player.render()
            elif char == "#":
                wall = Wall(self.screen, self.scale, x_pix, y_pix)
                self.wall_group.add(wall)
            elif char == "$":
                gem = Gem(self.screen, self.scale, x_pix, y_pix)
                self.gem_group.add(gem)
            elif char == "g":
                redgem = RedGem(self.screen, self.scale, x_pix, y_pix, 1)
                self.gem_group.add(redgem)
            elif char == "e":
                enemy = Enemy(self.screen, self.scale, x_pix, y_pix, 1, 1)
                enemy.move_to(x_pix / 8, y_pix / 8)
                enemy.render()
                self.enemy_group.add(enemy)
        self.update_text()

    def update_text(self):
        self.player_hearts_text.change_text(f"*{self.player.hearts}")
        self.player_energy_text.change_text(f"*{self.player.energy}")
        self.player_damage_text.change_text(f"*{self.player.damage}")
