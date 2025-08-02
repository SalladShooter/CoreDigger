import pygame
from player import Player
from world_gen import World_Gen

scale = 8
x = 0
y = 0
energy = 20
max_energy = energy
hearts = 5
max_hearts = hearts
damage = 1
upgrade = 9
max_upgrade = 10
depth = 0

pygame.init()
screen = pygame.display.set_mode((160 * scale, 128 * scale))
clock = pygame.time.Clock()
running = True

player = Player(screen, scale, x, y, energy, max_energy, hearts, max_hearts, damage, upgrade, max_upgrade, depth)
world = World_Gen(screen, scale, player)

upgrade_pending = False

def should_trigger_upgrade(player):
    return player.upgrade >= player.max_upgrade

while running:
    events = pygame.event.get()
    if world.select.selecting:
        for event in events:
            world.select.move_select(event)
            if event.type == pygame.QUIT:
                runing = False
            if not world.select.selecting and should_trigger_upgrade(player):
                upgrade_pending = True
            if not world.select.selecting and upgrade_pending:
                choice = world.select.selected_item
                items = world.select.items
                if items[choice] == 0:
                    player.max_hearts += 5
                elif items[choice] == 1:
                    player.max_energy += 5
                elif items[choice] == 2:
                    player.damage += 1
                upgrade_pending = False
                player.upgrade = 0
                player.max_upgrade += 5
                player.can_move = True
    else:
        for event in events:
            player.move(event)
            world.select.move_select(event)
            if event.type == pygame.QUIT:
                running = False

        if player.moving:
            for enemy in world.enemy_group:
                enemy.move(player)
                world.update.check_mine(enemy, world.dirt_group)
                world.update.check_explode(enemy, world.dirt_group)
                world.update.check_wall(enemy, world.wall_group)
            player.moving = False

        if should_trigger_upgrade(player):
            world.select.change_selecting(True, world.select.items)
            upgrade_pending = True
            player.can_move = False

    screen.fill("black")
    world.render_world()

    pygame.display.flip()
    if player.hearts == 0 or player.energy == 0:
        running = False

    clock.tick(24)

pygame.quit()
