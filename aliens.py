import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, name: str, start_pos: tuple):
        super().__init__()
        self.image = pygame.image.load(f'graphics/aliens/{name}.png').convert_alpha()
        self.rect = self.image.get_rect(center=start_pos)
        self.move = -1

    def destroy(self):
        if self.rect.y > 600:
            self.kill()

    def update(self):
        self.rect.x += self.move
        if self.rect.left < 50 or self.rect.right > 1230:
            self.move *= -1
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
