import pygame

pygame.init()

class Player:
    def __init__(self, screen, scale, x, y, energy, max_energy, hearts, max_hearts, damage, upgrade, max_upgrade, depth):
        self.screen = screen
        self.scale = scale
        self.energy = energy
        self.max_energy = max_energy
        self.hearts = hearts
        self.max_hearts = hearts
        self.damage = damage
        self.upgrade = upgrade
        self.max_upgrade = max_upgrade
        self.depth = depth
        self.prev_direction = 0
        self.player_images_paths = [
            "assets/Player_FaceRight.png",
            "assets/Player_FaceLeft.png",
            "assets/Player_FaceDown.png",
        ]
        self.player_images = []
        for path in self.player_images_paths:
            img = pygame.image.load(path).convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * self.scale, img.get_height() * self.scale))
            self.player_images.append(img)
        self.generate_world = False
        self.player_direction = 0

        width, height = self.player_images[0].get_size()
        width /= 8
        height /= 8
        self.rect = pygame.Rect(x * self.scale, y * self.scale, width, height)
        self.moving = False
        self.can_move = True

    def move_to(self, x, y):
        self.rect.topleft = (x * self.scale, y * self.scale)

    def move(self, event):
        if event.type == pygame.KEYDOWN and self.can_move:
            dx, dy = 0, 0
            self.prev_x = self.rect.x
            self.prev_y = self.rect.y
            if event.key == pygame.K_RIGHT:
                dx = 8 * self.scale
                self.player_direction = 0
                self.moving = True
            elif event.key == pygame.K_LEFT:
                dx = -8 * self.scale
                self.player_direction = 1
                self.moving = True
            elif event.key == pygame.K_DOWN:
                dy = 8 * self.scale
                self.player_direction = 2
                self.moving = True
                self.generate_world = True
                self.depth += 1
            else:
                self.moving = False

            self.rect.x += dx
            self.rect.y += dy
        else:
            self.moving = False

    def render(self):
        if self.energy > self.max_energy:
            self.energy = self.max_energy
        if self.hearts > self.max_hearts:
            self.hearts = self.max_hearts
        self.screen.blit(self.player_images[self.player_direction], self.rect.topleft)    
