import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    player = pygame.sprite.GroupSingle()
    player.add(Player())
    print(player)
