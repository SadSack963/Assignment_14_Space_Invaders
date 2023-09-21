
import pygame
from player import Player, Bullet
from aliens import Alien, Ship


BEZEL_SCALE = 2


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
        alien.animate()
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
screen = pygame.display.set_mode((950, 990))
screen_centre = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
clock = pygame.time.Clock()
frame_time = 0  # Seconds since last frame


# Screen area available for gameplay (inside bezel)
play_area_top_left = (55, 155)
play_area_bottom_right = (425, 395)
play_area_x_length = play_area_bottom_right[0] - play_area_top_left[0]
play_area_y_length = play_area_bottom_right[1] - play_area_top_left[1]
print(play_area_x_length, play_area_y_length)
play_area = pygame.Surface((play_area_x_length, play_area_y_length))
play_area_x0 = play_area_top_left[0] * BEZEL_SCALE
play_area_y0 = play_area_top_left[1] * BEZEL_SCALE
play_area_centre = pygame.Vector2(play_area.get_width() / 2, play_area.get_height() / 2)

# ===== EXPERIMENT =====
first_frame = pygame.image.load('Experiments/First_Frame.png').convert_alpha()
first_frame = pygame.transform.rotozoom(first_frame, 0, 0.19)
first_frame_rect = first_frame.get_rect()
# ======================

background_image = pygame.image.load('graphics/artwork/background.png').convert_alpha()
background_image = pygame.transform.rotozoom(background_image, 0, 0.5)
background_image_rect = background_image.get_rect()

bezel_image = pygame.image.load('graphics/artwork/spaceinvaders-full.png').convert_alpha()
bezel_image = pygame.transform.rotozoom(bezel_image, 0, BEZEL_SCALE)
bezel_image_rect = bezel_image.get_rect()

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
    aliens_10_1.add(Alien("crab", (x, 500)))
    aliens_10_2.add(Alien("crab", (x, 400)))
    aliens_20_3.add(Alien("octopus", (x, 300)))
    aliens_20_4.add(Alien("octopus", (x, 200)))
    aliens_30_5.add(Alien("squid", (x, 100)))

ship = pygame.sprite.GroupSingle()
ship.add(Ship())

aliens = [aliens_10_1, aliens_10_2, aliens_20_3, aliens_20_4, aliens_30_5 ]
aliens_index = 0
aliens_move_time = 200  # Time interval (milliseconds) to move aliens

aliens_move_timer = pygame.USEREVENT + 1  # Pointer to the timer
pygame.time.set_timer(aliens_move_timer, aliens_move_time)


running = True
game_play = False

while running:
    # Poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_play:
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
        if not game_play and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_play = True

    if game_play:
        # Fill the screen with a color to wipe away anything from the last frame
        # screen.fill("black")
        screen.blit(background_image, (0, 0))

        # Update and draw sprites
        # player.update()
        # player.draw(play_area)
        # bullet.update()
        # bullet.draw(play_area)
        # aliens_10_1.update()
        # aliens_10_1.draw(play_area)
        # aliens_10_2.update()
        # aliens_10_2.draw(play_area)
        # aliens_20_3.update()
        # aliens_20_3.draw(play_area)
        # aliens_20_4.update()
        # aliens_20_4.draw(play_area)
        # aliens_30_5.update()
        # aliens_30_5.draw(play_area)
        # ship.update()
        # ship.draw(play_area)

        play_area.blit(first_frame, (play_area.get_width() / 2 - first_frame.get_width() / 2, 0))
        # Scale and blit the play area on the screen
        play_area_surf = pygame.transform.rotozoom(play_area, 0, BEZEL_SCALE)
        screen.blit(play_area_surf, (play_area_x0, play_area_y0))
    else:
        intro()

    screen.blit(bezel_image, (0, 0))

    pygame.display.update()
    frame_time = clock.tick(60)

pygame.quit()
