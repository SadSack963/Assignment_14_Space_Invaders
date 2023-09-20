import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, name: str, start_pos: tuple):
        super().__init__()
        self.image = pygame.image.load(f'graphics/aliens/{name}.png').convert_alpha()
        self.rect = self.image.get_rect(center=start_pos)
        self.move = -2

    def destroy(self):
        if self.rect.y > 600:
            self.kill()

    def update(self):
        self.rect.x += self.move
        if self.rect.x < 50 or self.rect.x > 1100:
            self.move *= -1
        self.destroy()
