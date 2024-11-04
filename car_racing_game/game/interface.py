import pygame
import os
from game import game
from multiplayer import multiplayer


# Define windows positions
def set_window_position(x, y):
    """
    Set the position of the game window.

    Parameters
    ----------

    x : int
        The x-coordinate of the window position.
    y : int
        The y-coordinate of the window position.
    """
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
    pygame.display.quit()
    pygame.display.init()


# Define the main interface
def interface(highest_score):
    """
    Display the main interface with menu options.

    Parameters
    ----------

    highest_score : int
        The highest score to be displayed on the interface.
    """
    # Coordinates for the window
    x = 500
    y = 100
    set_window_position(x, y)
    pygame.init()

    # Set up the screen and the name of the window
    pygame.display.set_caption("Menu")
    size = (600, 600)
    screen = pygame.display.set_mode(size)

    # Colors
    white = (255, 255, 255)

    # Define text font and text to be displayed
    comicsansfont = pygame.font.SysFont('Comic Sans MS', 25)
    record = comicsansfont.render(f'Highest Score:{int(highest_score)}', True, white)
    background = pygame.image.load('images/back_grounds/menu.png')
    singleplayer = pygame.image.load('images/button/single_player.png').convert_alpha()
    singleplayer_hoover = pygame.image.load('images/button/single_player_hoover.png').convert_alpha()
    multiplayer_ = pygame.image.load('images/button/multiplayer.png').convert_alpha()
    multiplayer_hoover = pygame.image.load('images/button/multiplayer_hoover.png').convert_alpha()
    info_ = pygame.image.load('images/button/info.png').convert_alpha()
    info_hoover = pygame.image.load('images/button/info_hoover.png').convert_alpha()
    credits_button = pygame.image.load('images/button/credits.png').convert_alpha()
    credits_hoover = pygame.image.load('images/button/credits_hoover.png').convert_alpha()
    quit_ = pygame.image.load('images/button/quit.png').convert_alpha()
    quit_hoover = pygame.image.load('images/button/quit_hoover.png').convert_alpha()

    while True:
        mouse = pygame.mouse.get_pos()

        # Display the highest score
        screen.blit(record, (100, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Define the actions of the buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= mouse[0] <= 149 and 250 <= mouse[1] <= 293:
                    game(highest_score)
                if 50 <= mouse[0] <= 150 and 300 <= mouse[1] <= 343:
                    multiplayer()
                if 50 <= mouse[0] <= 150 and 350 <= mouse[1] <= 393:
                    info()
                if 50 <= mouse[0] <= 150 and 400 <= mouse[1] <= 443:
                    credits_()
                if 50 <= mouse[0] <= 150 and 450 <= mouse[1] <= 493:
                    pygame.quit()

        screen.blit(background, (0, 0))

        # Draw buttons
        # Singleplayer Button
        if 50 <= mouse[0] <= 149 and 250 <= mouse[1] <= 293:
            screen.blit(singleplayer_hoover, (50, 250))
        else:
            screen.blit(singleplayer, (50, 250))

        # Multiplayer
        if 50 <= mouse[0] <= 150 and 300 <= mouse[1] <= 343:
            screen.blit(multiplayer_hoover, (50, 300))
        else:
            screen.blit(multiplayer_, (50, 300))

        # Info
        if 50 <= mouse[0] <= 150 and 350 <= mouse[1] <= 393:
            screen.blit(info_hoover, (50, 350))
        else:
            screen.blit(info_, (50, 350))

        # Credits
        if 50 <= mouse[0] <= 150 and 400 <= mouse[1] <= 443:
            screen.blit(credits_hoover, (50, 400))
        else:
            screen.blit(credits_button, (50, 400))

        # Quit
        if 50 <= mouse[0] <= 150 and 450 <= mouse[1] <= 493:
            screen.blit(quit_hoover, (50, 450))
        else:
            screen.blit(quit_, (50, 450))

        # Display the highest score
        screen.blit(record, (50, 75))
        pygame.display.update()


# Define the Credits interface
def credits_():
    """
    Display the Credits interface.
    """
    x = 450
    y = 100
    set_window_position(x, y)
    pygame.init()

    # Colors
    blue = (91, 177,	249)

    # Set up the screen and the name of the window
    size = (678, 568)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Credits")

    # Load images
    credits_bck = pygame.image.load('images/back_grounds/credits.png')
    back = pygame.image.load('images/button/back.png')
    back_hoover = pygame.image.load('images/button/back_hoover.png')

    while True:
        mouse = pygame.mouse.get_pos()

        # Define events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 280 <= mouse[0] <= 379 and 450 <= mouse[1] <= 493:
                    from main import load_highest_score
                    highest_score = load_highest_score()  # Guarantee that the highest scores remains correct
                    interface(highest_score)

        screen.fill(blue)
        screen.blit(credits_bck, (0, 0))

        # Draw back button
        if 280 <= mouse[0] <= 379 and 450 <= mouse[1] <= 493:
            screen.blit(back_hoover, (280, 450))
        else:
            screen.blit(back, (280, 450))

        pygame.display.update()


# Define Information handling
def info():
    """
    Display the Info interface with options to the different info pages:
        -Game;
        -Multiplayer;
        -Power-ups;
        -Controls.
    """
    x = 700
    y = 200
    set_window_position(x, y)
    pygame.init()

    # Colors
    blue = (91, 177, 249)

    # Set up the screen and the name of the window
    size = (210, 426)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Info")

    # Load images
    info_ = pygame.image.load('images/back_grounds/info.png').convert_alpha()
    back = pygame.image.load('images/button/back.png').convert_alpha()
    back_hoover = pygame.image.load('images/button/back_hoover.png').convert_alpha()
    game_button = pygame.image.load('images/button/game.png').convert_alpha()
    game_button_hoover = pygame.image.load('images/button/game_hoover.png').convert_alpha()
    powerups = pygame.image.load('images/button/powerups.png').convert_alpha()
    powerups_hoover = pygame.image.load('images/button/powerups_hoover.png').convert_alpha()
    controls_ = pygame.image.load('images/button/controls.png')
    controls_hoover = pygame.image.load('images/button/controls_hoover.png')
    multiplayer_ = pygame.image.load('images/button/multiplayer.png')
    multiplayer_hoover = pygame.image.load('images/button/multiplayer_hoover.png')

    while True:
        mouse = pygame.mouse.get_pos()

        # Define events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 55 <= mouse[0] <= 154 and 325 <= mouse[1] <= 368:
                    from main import load_highest_score
                    highest_score = load_highest_score()  # Guarantee that the highest scores remains correct
                    interface(highest_score)
                if 55 <= mouse[0] <= 154 and 100 <= mouse[1] <= 143:
                    game_info()
                if 55 <= mouse[0] <= 154 and 150 <= mouse[1] <= 193:
                    multiplayer_info()
                if 55 <= mouse[0] <= 155 and 200 <= mouse[1] <= 243:
                    powerups_info()
                if 55 <= mouse[0] <= 155 and 250 <= mouse[1] <= 293:
                    controls()

        screen.fill(blue)
        screen.blit(info_, (0, 0))

        # Game button
        if 55 <= mouse[0] <= 154 and 100 <= mouse[1] <= 143:
            screen.blit(game_button_hoover, (55, 100))
        else:
            screen.blit(game_button, (55, 100))

        # Multiplayer button
        if 55 <= mouse[0] <= 154 and 150 <= mouse[1] <= 193:
            screen.blit(multiplayer_hoover, (55, 150))
        else:
            screen.blit(multiplayer_, (55, 150))

        # Powerups button
        if 55 <= mouse[0] <= 155 and 200 <= mouse[1] <= 243:
            screen.blit(powerups_hoover, (55, 200))
        else:
            screen.blit(powerups, (55, 200))

        # Controls button
        if 55 <= mouse[0] <= 155 and 250 <= mouse[1] <= 293:
            screen.blit(controls_hoover, (55, 250))
        else:
            screen.blit(controls_, (55, 250))

        # Back button
        if 55 <= mouse[0] <= 154 and 325 <= mouse[1] <= 368:
            screen.blit(back_hoover, (55, 325))
        else:
            screen.blit(back, (55, 325))

        pygame.display.update()


def game_info():
    """
    Display the Game Info interface.
    """
    x = 250
    y = 100
    set_window_position(x, y)
    pygame.init()

    # Colors
    blue = (91, 177, 249)

    # Set up the screen and the name of the window
    size = (1078, 576)
    screen = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption("Game Info")

    # Load images
    bck = pygame.image.load('images/back_grounds/info_game.png').convert_alpha()
    back = pygame.image.load('images/button/back.png').convert_alpha()
    back_hoover = pygame.image.load('images/button/back_hoover.png').convert_alpha()

    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 480 <= mouse[0] <= 579 and 475 <= mouse[1] <= 518:
                    info()

        screen.fill(blue)
        screen.blit(bck, (0, 0))

        # Back button
        if 480 <= mouse[0] <= 579 and 490 <= mouse[1] <= 533:
            screen.blit(back_hoover, (480, 490))
        else:
            screen.blit(back, (480, 490))

        pygame.display.update()


def powerups_info():
    """
    Display the Powerups Info interface.
    """
    x = 200
    y = 30
    set_window_position(x, y)
    pygame.init()

    # Colors
    blue = (91, 177, 249)

    # Set up the screen and the name of the window
    size = (1176, 783)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game Info")

    # Load images
    bck = pygame.image.load('images/back_grounds/info_powerups.png').convert_alpha()
    back = pygame.image.load('images/button/back.png').convert_alpha()
    back_hoover = pygame.image.load('images/button/back_hoover.png').convert_alpha()

    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 520 <= mouse[0] <= 619 and 700 <= mouse[1] <= 743:
                    info()

        screen.fill(blue)
        screen.blit(bck, (0, 0))

        # Back button
        if 520 <= mouse[0] <= 619 and 700 <= mouse[1] <= 743:
            screen.blit(back_hoover, (520, 700))
        else:
            screen.blit(back, (520, 700))

        pygame.display.update()


def controls():
    """
    Display the Controls Info interface.
    """
    x = 450
    y = 100
    set_window_position(x, y)
    pygame.init()

    # Colors
    blue = (91, 177, 249)

    # Set up the screen and the name of the window
    size = (756, 518)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Controls")

    # Load images
    bck = pygame.image.load('images/back_grounds/controls.png').convert_alpha()
    back = pygame.image.load('images/button/back.png').convert_alpha()
    back_hoover = pygame.image.load('images/button/back_hoover.png').convert_alpha()

    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 325 <= mouse[0] <= 424 and 450 <= mouse[1] <= 493:
                    info()

        screen.fill(blue)
        screen.blit(bck, (0, 0))

        # Back button
        if 325 <= mouse[0] <= 424 and 450 <= mouse[1] <= 493:
            screen.blit(back_hoover, (325, 450))
        else:
            screen.blit(back, (325, 450))

        pygame.display.update()


def multiplayer_info():
    """
    Display the Multiplayer Info interface.
    """
    x = 250
    y = 100
    set_window_position(x, y)
    pygame.init()

    # Colors
    blue = (91, 177, 249)

    # Set up the screen and the name of the window
    size = (1078, 576)
    screen = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption("Multiplayer Info")

    # Load images
    bck = pygame.image.load('images/back_grounds/info_multiplayer.png').convert_alpha()
    back = pygame.image.load('images/button/back.png').convert_alpha()
    back_hoover = pygame.image.load('images/button/back_hoover.png').convert_alpha()

    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 480 <= mouse[0] <= 579 and 475 <= mouse[1] <= 518:
                    info()

        screen.fill(blue)
        screen.blit(bck, (0, 0))

        # Back button
        if 480 <= mouse[0] <= 579 and 490 <= mouse[1] <= 533:
            screen.blit(back_hoover, (480, 490))
        else:
            screen.blit(back, (480, 490))

        pygame.display.update()
