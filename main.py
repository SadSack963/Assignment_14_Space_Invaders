
import pygame
from player import Player


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
# dt is delta time in seconds since last frame, used for framerate-independent physics
dt = 0

screen_centre = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

player = pygame.sprite.GroupSingle()
player.add(Player())
print(player)

running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from the last frame
    screen.fill("black")

    player.update()
    player.draw(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        # Shoot
        # player_pos.y -= 300 * dt
        pass
    if keys[pygame.K_DOWN]:
        # Start / Pause / Resume
        # player_pos.y += 300 * dt
        pass
    if keys[pygame.K_LEFT]:
        # Move left
        # player_pos.x -= 300 * dt
        pass
    if keys[pygame.K_RIGHT]:
        # Move right
        # player_pos.x += 300 * dt
        pass

    # flip the display to put buffer on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics
    dt = clock.tick(60) / 1000

pygame.quit()