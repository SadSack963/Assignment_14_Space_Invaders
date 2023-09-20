
import pygame
from player import Player, Bullet
from aliens import Alien, Ship


def intro() -> None:
    pass


def aliens_move(group) -> None:
    """
    Move all aliens in the group

    :param group: a Sprite group instance
    :type group: pygame.sprite.Group
    :return: None
    :rtype:
    """
    for alien in group:
        alien.rect.x += alien.move_direction * alien.move_distance


def aliens_check() -> None:
    """
    Check if any alien in the group has reached the edge of the play area

    :return: None
    :rtype:
    """
    reverse = False
    for group in aliens:
        for alien in group:
            if alien.rect.left <= 50 or alien.rect.right >= 1230:
                reverse = True
    if reverse:
        global aliens_move_time
        if aliens_move_time > frame_time + 20:
            aliens_move_time -= 20
            pygame.time.set_timer(aliens_move_timer, aliens_move_time)
            print(aliens_move_time)
        for group in aliens:
            alien_reverse(group)


def alien_reverse(group) -> None:
    """
    Drop aliens to the next level, increase the speed and
    reverse the direction of all aliens in the group

    :param group: a Sprite group instance
    :type group: pygame.sprite.Group
    :return: None
    :rtype:
    """
    for alien in group:
        alien.move_direction *= -1
        alien.rect.y += 20


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
frame_time = 0  # Seconds since last frame

screen_centre = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Sprites
player = pygame.sprite.GroupSingle()
player.add(Player())
bullet = pygame.sprite.GroupSingle()
# aliens = pygame.sprite.Group()
# aliens.add(Alien("alien_10", (500, 500)))
# aliens.add(Alien("alien_10", (400, 400)))
# aliens.add(Alien("alien_20", (300, 300)))
# aliens.add(Alien("alien_20", (200, 200)))
# aliens.add(Alien("alien_30", (100, 100)))

aliens_10_1 = pygame.sprite.Group()
aliens_10_2 = pygame.sprite.Group()
aliens_20_3 = pygame.sprite.Group()
aliens_20_4 = pygame.sprite.Group()
aliens_30_5 = pygame.sprite.Group()
for x in range(150, 850, 100):
    aliens_10_1.add(Alien("alien_10", (x, 500)))
    aliens_10_2.add(Alien("alien_10", (x, 400)))
    aliens_20_3.add(Alien("alien_20", (x, 300)))
    aliens_20_4.add(Alien("alien_20", (x, 200)))
    aliens_30_5.add(Alien("alien_30", (x, 100)))

ship = pygame.sprite.GroupSingle()
ship.add(Ship())

aliens = [aliens_10_1, aliens_10_2, aliens_20_3, aliens_20_4, aliens_30_5 ]
aliens_index = 0
aliens_move_time = 200  # Time interval (milliseconds) to move aliens

aliens_move_timer = pygame.USEREVENT + 1  # Pointer to the timer
pygame.time.set_timer(aliens_move_timer, aliens_move_time)


running = True
game_active = False

while running:
    # Poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_active:
            # Player fires a bullet
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not bullet.sprite:
                    bullet.add(Bullet(player.sprite.rect.center))

            # Move aliens
            if event.type == aliens_move_timer:
                aliens_move(aliens[aliens_index])
                aliens_index += 1
                if aliens_index >= len(aliens):
                    aliens_index = 0
                    aliens_check()

        # Start a new game
        if not game_active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_active = True

    if game_active:
        # Fill the screen with a color to wipe away anything from the last frame
        screen.fill("black")

        # Update and draw sprites
        player.update()
        player.draw(screen)
        bullet.update()
        bullet.draw(screen)
        aliens_10_1.update()
        aliens_10_1.draw(screen)
        aliens_10_2.update()
        aliens_10_2.draw(screen)
        aliens_20_3.update()
        aliens_20_3.draw(screen)
        aliens_20_4.update()
        aliens_20_4.draw(screen)
        aliens_30_5.update()
        aliens_30_5.draw(screen)
        ship.update()
        ship.draw(screen)
    else:
        intro()

    pygame.display.update()
    frame_time = clock.tick(60)

pygame.quit()
