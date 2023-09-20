import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/player/player_1.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(200, 600))

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 10
        if keys[pygame.K_RIGHT]:
            self.rect.x += 10

    def update(self):
        self.input()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        super().__init__()
        self.image = pygame.image.load('graphics/player/bullet.png').convert_alpha()
        self.rect = self.image.get_rect(center=start_pos)

    def destroy(self):
        if self.rect.y < 0:
            self.kill()

    def update(self):
        self.rect.y -= 20
        self.destroy()
