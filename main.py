import pygame
from player import Player
from world_gen import World_Gen

scale = 8
x = 0
y = 0
energy = 20
max_energy = energy
hearts = 3
max_hearts = hearts
damage = 1
depth = 0

pygame.init()
screen = pygame.display.set_mode((160 * scale, 128 * scale))
clock = pygame.time.Clock()
running = True

player = Player(screen, scale, x, y, energy, max_energy, hearts, max_hearts, damage, depth)
world = World_Gen(screen, scale, player)

while running:
    events = pygame.event.get()
    for event in events:
        player.move(event)
        if event.type == pygame.QUIT:
            running = False

    if player.moving:
        for enemy in world.enemy_group:
            enemy.move(player)
            world.update.check_mine(enemy, world.dirt_group)
            world.update.check_explode(enemy, world.dirt_group)
            world.update.check_wall(enemy, world.wall_group)
        player.moving = False

    screen.fill("black")
    world.render_world()

    pygame.display.flip()
    if player.hearts == 0 or player.energy == 0:
        running = False
        pygame.quit()

    clock.tick(24)

pygame.quit()
