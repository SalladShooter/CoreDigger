import pygame

class Select_Upgrade:
    def __init__(self, screen, scale, x, y):
        self.screen = screen
        self.scale = scale
        self.selecting = False
        self.asset_image = "assets/Select.png"
        loaded_image = pygame.image.load(self.asset_image).convert_alpha()
        self.selector_img = pygame.transform.scale(loaded_image, (8 * self.scale, 8 * self.scale))
        self.start_x = x * self.scale
        self.y = y * self.scale
        self.slot_spacing = 16 * self.scale
        self.n_slots = 3
        self.selected_item = 0
        self.rects = [
            pygame.Rect(self.start_x + i * self.slot_spacing, self.y, 
                        self.selector_img.get_width(), self.selector_img.get_height())
            for i in range(self.n_slots)
        ]
    
    def change_selecting(self, selecting, items):
        self.selecting = selecting
        if selecting:
            self.selected_item = 0
        self.items = items

    def move_select(self, event):
        if not self.selecting:
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if self.selected_item < self.n_slots - 1:
                    self.selected_item += 1
            elif event.key == pygame.K_LEFT:
                if self.selected_item > 0:
                    self.selected_item -= 1
            elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                self.selecting = False

    def render(self):
        if self.selecting:
            self.screen.blit(self.selector_img, self.rects[self.selected_item].topleft)

