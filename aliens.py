import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, name: str, start_pos: tuple):
        super().__init__()
        image_1 = pygame.image.load(f'graphics/aliens/{name}_1.png').convert_alpha()
        image_2 = pygame.image.load(f'graphics/aliens/{name}_2.png').convert_alpha()
        self.image_list = [image_1, image_2]
        self.image_index = 0
        self.image = self.image_list[self.image_index]
        self.rect = self.image.get_rect(center=start_pos)
        self.move_distance = 20
        self.move_direction = -1

    def animate(self):
        self.image_index += 1
        if self.image_index >= len(self.image_list):
            self.image_index = 0
        self.image = self.image_list[self.image_index]

    def destroy(self):
        if self.rect.y > 600:
            self.kill()

    def update(self):
        self.destroy()


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f'graphics/aliens/ship.png').convert_alpha()
        self.rect = self.image.get_rect(center=(-200, 40))
        self.move = 5

    def destroy(self):
        if self.rect.x > 1300:
            self.kill()

    def update(self):
        self.rect.x += self.move
        self.destroy()
