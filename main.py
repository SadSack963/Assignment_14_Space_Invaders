
import pygame
from player import Player, Bullet
from aliens import Alien, Ship


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

screen_centre = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Sprites
player = pygame.sprite.GroupSingle()
player.add(Player())
bullet = pygame.sprite.GroupSingle()
aliens = pygame.sprite.Group()
aliens.add(Alien("alien_10", (500, 500)))
aliens.add(Alien("alien_10", (400, 400)))
aliens.add(Alien("alien_20", (300, 300)))
aliens.add(Alien("alien_20", (200, 200)))
aliens.add(Alien("alien_30", (100, 100)))
ship = pygame.sprite.GroupSingle()
ship.add(Ship())


running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Player fires a bullet
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not bullet.sprite:
                bullet.add(Bullet(player.sprite.rect.center))

    # fill the screen with a color to wipe away anything from the last frame
    screen.fill("black")

    # update and draw sprites
    player.update()
    player.draw(screen)
    bullet.update()
    bullet.draw(screen)
    aliens.update()
    aliens.draw(screen)
    ship.update()
    ship.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
