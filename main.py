import pygame
from player import Player
from world_gen import World_Gen

scale = 8
x = 0
y = 0
energy = 20
hearts = 3
damage = 1

pygame.init()
screen = pygame.display.set_mode((128 * scale, 128 * scale))
clock = pygame.time.Clock()
running = True

player = Player(screen, scale, x, y, energy, hearts, damage)
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

    clock.tick(24)

pygame.quit()
