import pygame

pygame.init()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, scale, x, y, hearts, damage):
        super().__init__()
        self.screen = screen
        self.scale = scale
        self.hearts = hearts
        self.damage = damage
        self.prev_direction = 0
        self.enemy_images_paths = [
            "assets/Enemy_FaceRight.png",
            "assets/Enemy_FaceLeft.png",
            "assets/Enemy_FaceDown.png",
        ]
        self.enemy_images = []
        for path in self.enemy_images_paths:
            img = pygame.image.load(path).convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * self.scale, img.get_height() * self.scale))
            self.enemy_images.append(img)
        self.enemy_direction = 2

        width, height = self.enemy_images[0].get_size()
        width /= 8
        height /= 8
        self.rect = pygame.Rect(x * self.scale, y * self.scale, width, height)

    def move_to(self, x, y):
        self.rect.topleft = (x * self.scale, y * self.scale)

    def move(self, player):
        dx, dy = 0, 0

        if player.rect.y == self.rect.y and player.moving:
            if player.rect.x > self.rect.x:
                dx = 8 * self.scale
                self.enemy_direction = 0
            elif player.rect.x < self.rect.x:
                dx = -8 * self.scale
                self.enemy_direction = 1
        else:
            if player.rect.y > self.rect.y and player.moving:
                dy = 8 * self.scale
                self.enemy_direction = 2

        self.rect.x += dx
        self.rect.y += dy

    def render(self):
        self.screen.blit(self.enemy_images[self.enemy_direction], self.rect.topleft)
