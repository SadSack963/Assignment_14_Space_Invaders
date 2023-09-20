
import pygame
from player import Player, Bullet
from aliens import Alien


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

screen_centre = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

player = pygame.sprite.GroupSingle()
player.add(Player())
bullet = pygame.sprite.GroupSingle()
aliens = pygame.sprite.Group()
aliens.add(Alien("alien_10", (300, 300)))

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

    pygame.display.update()
    clock.tick(60)

pygame.quit()
