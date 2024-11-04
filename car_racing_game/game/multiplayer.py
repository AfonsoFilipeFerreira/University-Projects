import random
import pygame
import os
from car import Car
from powerups import Shield, Slowing, Invincible, Shrink, Accelerator, Engorgio, Mirror


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


def multiplayer():
    """
    Run the multiplayer car racing game.

    This function initializes and runs a two-player car racing game.
    Players control their cars using WASD keys (Player 1) or arrow keys (Player 2).
    The game includes randomly generated cars, power-ups (one at the time for each player), and a speedometer.

    The game window has a road for each player, and the road have 4 lanes with dashed lines and borders.
    Players need to avoid collisions with incoming cars and collect power-ups.

    Power-ups include:
        - Invincible: Makes the player's car invulnerable to collisions.
        - Shield: Creates a shield that protects the player from one collision.
        - Slowing: Slows down the speed of incoming cars temporarily.
        - Shrink: Shrinks the player's car for a short duration.
        - Mirror: Reverses the other player's controls.
        - Engorgio: Enlarges the other player's car temporarily.
        - Accelerator: Speeds up the other player's incoming cars temporarily.

    Players can pause the game by pressing the 'P' key.
    In pause mode, players can continue the game, return to the main menu, or quit the game.

    The game has no scoring system and ends when one of the players collides with an incoming car.
    The winner is determined by who doesn't crash first.
    """
    # Coordinates for the window
    x = 200
    y = 100
    set_window_position(x, y)
    pygame.init()

    # Colors
    white = (255, 255, 255)
    red = (255, 0, 0)
    grey = (51, 51, 51)
    pause_color = (128, 128, 128, 150)
    bck = (26, 128, 14)

    # Cars types and dimensions
    motorbike = (15, 33, random.choice(['images/car_images/motorbike/motorbike.png',
                                        'images/car_images/motorbike/motorbike2.png']))
    sedan = (27, 49, random.choice(['images/car_images/sedan/sedan_blue.png',
                                    'images/car_images/sedan/sedan_green.png',
                                    'images/car_images/sedan/sedan_red.png']))
    suv = (40, 65, random.choice(['images/car_images/suv/suv_black.png',
                                  'images/car_images/suv/suv_blue.png']))
    pickup_truck = (50, 95, random.choice(['images/car_images/pickup_truck/pickup_truck_blue.png',
                                           'images/car_images/pickup_truck/pickup_truck_green.png',
                                           'images/car_images/pickup_truck/pickup_truck_grey.png',
                                           'images/car_images/pickup_truck/pickup_truck_red.png',
                                           'images/car_images/pickup_truck/pickup_truck_white.png',
                                           'images/car_images/pickup_truck/pickup_truck_yellow.png']))
    hatchback = (30, 60, random.choice(['images/car_images/hatchback/hatchback_grey.png',
                                        'images/car_images/hatchback/hatchback_white.png',
                                        'images/car_images/hatchback/hatchback_yellow.png']))
    sports_car = (30, 61, random.choice(['images/car_images/sports_car/sports_car_blue.png',
                                         'images/car_images/sports_car/sports_car_green.png',
                                         'images/car_images/sports_car/sports_car_orange.png',
                                         'images/car_images/sports_car/sports_car_white.png',
                                         'images/car_images/sports_car/sports_car_yellow.png']))
    convertible = (24, 41, random.choice(['images/car_images/convertible/convertible_blue.png',
                                          'images/car_images/convertible/convertible_green.png',
                                          'images/car_images/convertible/convertible_red.png']))
    limousine = (40, 104, random.choice(['images/car_images/limousine/limousine_black.png',
                                         'images/car_images/limousine/limousine_white.png']))
    normal_truck = (70, 136, random.choice(['images/car_images/truck/truck_blue.png',
                                            'images/car_images/truck/truck_blue2.png',
                                            'images/car_images/truck/truck_red.png',
                                            'images/car_images/truck/truck_red2.png',
                                            'images/car_images/truck/truck_white.png']))
    long_truck = (85, 170, random.choice(['images/car_images/long_truck/long_truck_black.png',
                                          'images/car_images/long_truck/long_truck_blue.png',
                                          'images/car_images/long_truck/long_truck_green.png',
                                          'images/car_images/long_truck/long_truck_red.png',
                                          'images/car_images/long_truck/long_truck_white.png']))

    cars_size = [motorbike, sedan, suv, pickup_truck, hatchback, sports_car, convertible, limousine,
                 normal_truck, long_truck]

    # Set up the screen and the name of the window
    size = (1100, 500)
    screen = pygame.display.set_mode(size)
    surface = pygame.Surface(size, pygame.SRCALPHA)
    pygame.display.set_caption("Car Racing Game Multiplayer")

    # Define the player car and the 4 incoming cars for player 1
    player_car = Car('images/car_images/player_car/player_car_base.png', 30, 60)
    player_car.rect.x = 200
    player_car.rect.y = 400

    random_car1 = random.choice(cars_size)
    random_car2 = random.choice(cars_size)
    random_car3 = random.choice(cars_size)
    random_car4 = random.choice(cars_size)

    car1 = Car(random_car1[2], random_car1[0], random_car1[1], random.random() * 3, 1)
    car1.rect.x = 100 + (20 - random_car1[0]) / 2
    car1.rect.y = -100

    car2 = Car(random_car2[2], random_car2[0], random_car2[1], random.random() * 3, 2)
    car2.rect.x = 200 + (20 - random_car2[0]) / 2
    car2.rect.y = -200

    car3 = Car(random_car3[2], random_car3[0], random_car3[1], random.random() * 3, 3)
    car3.rect.x = 300 + (20 - random_car3[0]) / 2
    car3.rect.y = -500

    car4 = Car(random_car4[2], random_car4[0], random_car4[1], random.random() * 3, 4)
    car4.rect.x = 400 + (20 - random_car4[0]) / 2
    car4.rect.y = -300

    incoming_cars_1 = pygame.sprite.Group()
    incoming_cars_1.add(car1, car2, car3, car4)
    all_sprites_list_1 = pygame.sprite.Group()
    all_sprites_list_1.add(player_car, car1, car2, car3, car4)

    # Define the player car and the 4 incoming cars for player 2
    player_car_2 = Car('images/car_images/player_car/player_car_2_base.png', 30, 60)
    player_car_2.rect.x = 800
    player_car_2.rect.y = 400

    random_car5 = random.choice(cars_size)
    random_car6 = random.choice(cars_size)
    random_car7 = random.choice(cars_size)
    random_car8 = random.choice(cars_size)

    car5 = Car(random_car5[2], random_car5[0], random_car5[1], random.random() * 3, 7)
    car5.rect.x = 700 + (20 - random_car5[0]) / 2
    car5.rect.y = -100

    car6 = Car(random_car6[2], random_car6[0], random_car6[1], random.random() * 3, 8)
    car6.rect.x = 800 + (20 - random_car6[0]) / 2
    car6.rect.y = -200

    car7 = Car(random_car7[2], random_car7[0], random_car7[1], random.random() * 3, 9)
    car7.rect.x = 900 + (20 - random_car7[0]) / 2
    car7.rect.y = -500

    car8 = Car(random_car8[2], random_car8[0], random_car8[1], random.random() * 3, 10)
    car8.rect.x = 1000 + (20 - random_car8[0]) / 2
    car8.rect.y = -300

    incoming_cars_2 = pygame.sprite.Group()
    incoming_cars_2.add(car5, car6, car7, car8)
    all_sprites_list_2 = pygame.sprite.Group()
    all_sprites_list_2.add(player_car_2, car5, car6, car7, car8)

    # Load images and font type
    comicsansfont = pygame.font.SysFont('Comic Sans MS', 25)
    speedometer = pygame.image.load('images/back_grounds/speedometer.png')
    bck_pause = pygame.image.load('images/back_grounds/pause.png').convert_alpha()
    continue_ = pygame.image.load('images/button/continue.png').convert_alpha()
    continue_hoover = pygame.image.load('images/button/continue_hoover.png').convert_alpha()
    menu = pygame.image.load('images/button/main_menu.png').convert_alpha()
    menu_hoover = pygame.image.load('images/button/main_menu_hoover.png').convert_alpha()
    quit_ = pygame.image.load('images/button/quit.png').convert_alpha()
    quit_hoover = pygame.image.load('images/button/quit_hoover.png').convert_alpha()

    # Create power-up instances
    # As we want only one power-up to appear at the time we defined the spawning probabilities this way
    def generate_power_up():
        """
        Generate a random power-up based on specified probabilities.
        Probability Distribution:
        - Invincible: 10%
        - Shield: 30%
        - Slowing: 25%
        - Shrink: 15%
        - Other Player Effects (Total 20%):
            - Mirror: 25%
            - Engorgio: 25%
            - Accelerator: 50%

        Returns
        -------

        powerup_class : PowerUp
            An instance of a PowerUp class.
        """
        prob = random.random()
        if prob <= 0.1:
            powerup_class = Invincible()  # 10%
            return powerup_class
        elif 0.1 < prob <= 0.4:
            powerup_class = Shield()  # 30%
            return powerup_class
        elif 0.4 < prob <= 0.65:
            powerup_class = Slowing()  # 25%
            return powerup_class
        elif 0.65 < prob <= 0.80:
            powerup_class = Shrink()  # 15%
            return powerup_class
        elif 0.80 < prob <= 1:  # 20% for spawning a power-up that affects the other player
            prob2 = random.random()
            if prob2 <= 0.25:
                powerup_class = Mirror()  # 25%
                return powerup_class
            elif 0.25 < prob2 <= 0.5:
                powerup_class = Engorgio()  # 25%
                return powerup_class
            elif 0.5 < prob2 <= 1:
                powerup_class = Accelerator()  # 50%
                return powerup_class

    # Generate player 1 power-ups
    powerup_1 = generate_power_up()
    powerup_1.rect.x = random.choice([90, 190, 290, 390])
    powerup_1.rect.y = random.randint(-2000, -1000)
    powerups_1 = pygame.sprite.Group()
    powerups_1.add(powerup_1)
    all_sprites_list_1.add(powerups_1)

    # Generate player 2 power-ups
    powerup_2 = generate_power_up()
    powerup_2.rect.x = random.choice([690, 790, 890, 990])
    powerup_2.rect.y = random.randint(-2000, -1000)
    powerups_2 = pygame.sprite.Group()
    powerups_2.add(powerup_2)
    all_sprites_list_2.add(powerups_2)

    # Set a variable to track if a power-up is active
    powerup_active_1 = False  # player 1
    powerup_active_2 = False  # player 2
    powerup_active_1_2 = False  # player 1 to affect player 2
    powerup_active_2_1 = False  # player 2 to affect player 1

    # Condition to maintain the loop and pause the game
    carry_on = True
    pause = False

    # Set the initial player car speed, the increment (this variable will define the base pace of the game
    # the pace of the game will be the same for both players),the initial score and the font used to display the score
    player_car_speed = 1
    player2_car_speed = 1
    timer_1 = 0
    timer_2 = 0
    time_paused = 0

    # Define Pause Menu
    def pause_menu():
        """
        Pause the game display the pause menu on the screen.

        This function draws a colored rectangle on the game screen to act as the background for the pause menu.
        It displays buttons for continuing the game, going to the main menu, and quitting the game.
        """
        # Color the game screen and display Pause Menu
        pygame.draw.rect(surface, pause_color, (0, 0, size[0], size[1]))
        screen.blit(surface, (0, 0))
        screen.blit(bck_pause, (380.5, 108))

        # Continue Button
        if 500 <= mouse[0] <= 599 and 220 <= mouse[1] <= 263:
            screen.blit(continue_hoover, (500, 220))
        else:
            screen.blit(continue_, (500, 220))

        # Menu Button
        if 500 <= mouse[0] <= 599 and 270 <= mouse[1] <= 313:
            screen.blit(menu_hoover, (500, 270))
        else:
            screen.blit(menu, (500, 270))

        # Quit Button
        if 500 <= mouse[0] <= 599 and 320 <= mouse[1] <= 363:
            screen.blit(quit_hoover, (500, 320))
        else:
            screen.blit(quit_, (500, 320))

        pygame.display.update()

    clock = pygame.time.Clock()

    # Loop of the game
    while carry_on:
        mouse = pygame.mouse.get_pos()  # Get Mouse position
        keys = pygame.key.get_pressed()
        # Close the window of the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carry_on = False
            if keys[pygame.K_p]:
                # Unpause the Game if the Game is Paused
                if pause:
                    pause = False  # Close Pause Menu and Resume the Game
                    # Get the time the game was Paused
                    time_diff = pygame.time.get_ticks() - time_paused
                    # Add the time the game was paused to the power-up timer to prevent the power-up expiring while
                    # Game is Pause
                    timer_1 += time_diff
                    timer_2 += time_diff
                # Pause the Game
                else:
                    pause = True  # Pause the Game
                    time_paused = pygame.time.get_ticks()  # Get the time the Game was Paused
            # If the user makes the game window lose focus (if user clicks outside the game window) pause the game
            # to prevent a crash
            if event.type == pygame.WINDOWFOCUSLOST:
                pause = True  # Pause the Game
                time_paused = pygame.time.get_ticks()  # Get the time the Game was Paused
                # Pause Buttons functionalities
            if pause:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 500 <= mouse[0] <= 599 and 220 <= mouse[1] <= 263:
                        pause = False  # Close Pause Menu and Resume the Game
                        # Get the time the game was Paused
                        time_diff = pygame.time.get_ticks() - time_paused
                        # Add the time the game was paused to the power-up timer to prevent the power-up expiring while
                        # Game is Pause
                        timer_1 += time_diff
                        timer_2 += time_diff
                    if 500 <= mouse[0] <= 599 and 270 <= mouse[1] <= 313:
                        # Go to Main Menu
                        from interface import interface
                        from main import load_highest_score
                        highest_score = load_highest_score()  # Guarantee that the highest scores remains correct
                        interface(highest_score)
                    if 500 <= mouse[0] <= 599 and 320 <= mouse[1] <= 363:
                        # Close the Game
                        pygame.quit()

        # Set the controls (normal and if affected by the mirror power-up) of the game and the speed of the cars
        # Player 1
        if not pause:
            if powerup_active_2_1 and isinstance(powerup_2, Mirror):
                powerup_2.affect_player(player_car)
                if keys[pygame.K_a]:
                    player_car.move_right(5)
                if keys[pygame.K_d]:
                    player_car.move_left(5)
                if keys[pygame.K_w] and player_car.rect.y <= 400:
                    player_car.move_down(5)
                if keys[pygame.K_s] and player_car.rect.y >= 30:
                    player_car.move_up(5)
            else:
                if keys[pygame.K_a]:
                    player_car.move_left(5)
                if keys[pygame.K_d]:
                    player_car.move_right(5)
                if keys[pygame.K_w] and player_car.rect.y >= 30:
                    player_car.move_up(5)
                if keys[pygame.K_s] and player_car.rect.y <= 400:
                    player_car.move_down(5)
            # Player 2
            if powerup_active_1_2 and isinstance(powerup_1, Mirror):
                powerup_1.affect_player(player_car_2)
                if keys[pygame.K_LEFT]:
                    player_car_2.move_right(5)
                if keys[pygame.K_RIGHT]:
                    player_car_2.move_left(5)
                if keys[pygame.K_UP] and player_car_2.rect.y <= 400:
                    player_car_2.move_down(5)
                if keys[pygame.K_DOWN] and player_car_2.rect.y >= 30:
                    player_car_2.move_up(5)
            else:
                if keys[pygame.K_LEFT]:
                    player_car_2.move_left(5)
                if keys[pygame.K_RIGHT]:
                    player_car_2.move_right(5)
                if keys[pygame.K_UP] and player_car_2.rect.y >= 30:
                    player_car_2.move_up(5)
                if keys[pygame.K_DOWN] and player_car_2.rect.y <= 400:
                    player_car_2.move_down(5)

        # Increase speed over time
        player_car_speed += 0.002
        player2_car_speed += 0.002

        all_sprites_list_1.update()
        all_sprites_list_2.update()

        if pause:
            pause_menu()  # Call Pause Menu

        # Drawing the game
        screen.fill(bck)

        # Draw speedometer
        screen.blit(speedometer, [510, 400])
        speed = str(player_car_speed).split('.')[0]
        screen.blit(comicsansfont.render(f'{speed}', True, white), (552.5 if len(speed) == 1 else 545, 430))

        pygame.draw.rect(screen, grey, [60, 0, 400, 500])

        # Draw the dashed lines limiting the lanes
        for lane in range(160, 460, 100):
            for line_gap in range(5, 495, 50):
                pygame.draw.line(screen, white, [lane, line_gap], [lane, line_gap + 35], 5)

        # Draw the borders of the road
        for road_border in [54.5, 464.5]:
            for line_color in range(0, 500, 25):
                color = white if line_color % 50 == 0 else red
                pygame.draw.line(screen, color, [road_border, line_color],
                                 [road_border, line_color + 25], 10)

        # Player 2 game
        # Road
        pygame.draw.rect(screen, grey, [660, 0, 400, 500])

        # Draw the dashed lines limiting the lanes
        for lane in range(760, 1060, 100):
            for line_gap in range(5, 495, 50):
                pygame.draw.line(screen, white, [lane, line_gap], [lane, line_gap + 35], 5)

        # Draw the borders of the road
        for road_border in [654.5, 1064.5]:
            for line_color in range(0, 500, 25):
                color = white if line_color % 50 == 0 else red
                pygame.draw.line(screen, color, [road_border, line_color],
                                 [road_border, line_color + 25], 10)

        if not pause:
            # Generate incoming cars for player 1
            for car in incoming_cars_1:
                car.move_down(player_car_speed)
                if car.rect.y >= 500:
                    car.rect.y = random.randint(-500, -100)
                    car.change_speed(random.random() * 3)
                    car.incoming_cars_generator(random.choice(cars_size))

            # Generate incoming cars for player 2
            for car in incoming_cars_2:
                car.move_down(player2_car_speed)
                if car.rect.y >= 500:
                    car.rect.y = random.randint(-500, -100)
                    car.change_speed(random.random() * 3)
                    car.incoming_cars_generator(random.choice(cars_size))

            # Player 1 collision
            if powerup_active_1 and isinstance(powerup_1, Shield):
                powerup_1.affect_traffic(incoming_cars_1, player_car, cars_size, player_car_speed)
                if powerup_1.duration == 1:
                    powerup_active_1 = False
                    image_path = 'images/car_images/player_car/player_car_base.png'
                    car_image = pygame.image.load(image_path).convert_alpha()
                    player_car.image.blit(car_image, (0, 0))
                    powerup_1 = generate_power_up()
                    powerup_1.rect.x = random.choice([90, 190, 290, 390])
                    powerup_1.rect.y = random.randint(-2000, -1000)
                    powerups_1.add(powerup_1)

            elif powerup_active_1 and isinstance(powerup_1, Invincible):
                powerup_1.affect_traffic(incoming_cars_1, player_car, cars_size, player_car_speed)

            else:
                for car in incoming_cars_1:
                    if pygame.sprite.collide_mask(player_car, car) is not None:
                        # Pass the score value to the game over interface
                        game_over_multiplayer(winner=True)

            # Player 2 collision
            if powerup_active_2 and isinstance(powerup_2, Shield):
                powerup_2.affect_traffic(incoming_cars_2, player_car_2, cars_size, player2_car_speed)
                if powerup_2.duration == 1:
                    powerup_active_2 = False
                    image_path = 'images/car_images/player_car/player_car_2_base.png'
                    car_image = pygame.image.load(image_path).convert_alpha()
                    player_car_2.image.blit(car_image, (0, 0))
                    powerup_2 = generate_power_up()
                    powerup_2.rect.x = random.choice([690, 790, 890, 990])
                    powerup_2.rect.y = random.randint(-2000, -1000)
                    powerups_2.add(powerup_2)

            elif powerup_active_2 and isinstance(powerup_2, Invincible):
                powerup_2.affect_traffic(incoming_cars_2, player_car_2, cars_size, player2_car_speed)

            else:
                for car in incoming_cars_2:
                    if pygame.sprite.collide_mask(player_car_2, car) is not None:
                        # Pass the score value to the game over interface
                        game_over_multiplayer(winner=False)

            # Power-ups
            # Check for player 1 collision with power-up
            powerup_collisions_1 = pygame.sprite.spritecollide(player_car, powerups_1, True)
            for powerup_1 in powerup_collisions_1:
                if isinstance(powerup_1, (Mirror, Engorgio, Accelerator)):
                    if powerup_active_2:
                        powerup_active_2 = False
                        # In the case of engorgio
                        player_car_2.image = pygame.transform.scale(player_car_2.image, (30, 60))
                        image_path = 'images/car_images/player_car/player_car_2_base.png'
                        car_image = pygame.image.load(image_path).convert_alpha()
                        player_car_2.image.blit(car_image, (0, 0))
                        powerup_active_1_2 = True
                        timer_1 = pygame.time.get_ticks()
                    else:
                        powerup_active_1_2 = True
                        powerups_1.empty()
                        timer_1 = pygame.time.get_ticks()
                else:
                    # Set the active power-up
                    powerup_active_1 = True
                    timer_1 = pygame.time.get_ticks()

            # Check for player 2 collision with power-up
            powerup_collisions_2 = pygame.sprite.spritecollide(player_car_2, powerups_2, True)
            for powerup_2 in powerup_collisions_2:
                if isinstance(powerup_2, (Mirror, Engorgio, Accelerator)):
                    if powerup_active_1:
                        powerup_active_1 = False
                        player_car.image = pygame.transform.scale(player_car.image, (30, 60))  # In the case of engorgio
                        image_path = 'images/car_images/player_car/player_car_base.png'
                        car_image = pygame.image.load(image_path).convert_alpha()
                        player_car.image.blit(car_image, (0, 0))
                        powerup_active_2_1 = True
                        timer_2 = pygame.time.get_ticks()
                    else:
                        powerup_active_2_1 = True
                        powerups_2.empty()
                        timer_2 = pygame.time.get_ticks()
                else:
                    powerup_active_2 = True
                    timer_2 = pygame.time.get_ticks()

            # Apply power-up effects
            # For the power-ups that affect the other player, they will count as power-ups of the player affected
            # Player 1
            if powerup_active_2_1 and isinstance(powerup_2, (Mirror, Engorgio, Accelerator)):
                powerup_2.affect_player(player_car)
                powerup_2.affect_traffic(incoming_cars_1, player_car, cars_size, player_car_speed)
                screen.blit(comicsansfont.render('Player 1', True, grey), (500, 125))
                screen.blit(comicsansfont.render(f'{powerup_2}', True, grey), (500, 150))
                remaining_time = int((timer_2 + powerup_2.duration * 1000 - pygame.time.get_ticks()) / 1000)
                screen.blit(comicsansfont.render(f'{remaining_time} sec', True, grey),
                            (500, 175))

            if powerup_active_1 and isinstance(powerup_1, Shield):
                powerup_1.affect_player(player_car)
                powerup_1.affect_traffic(incoming_cars_1, player_car, cars_size, player_car_speed)
                screen.blit(comicsansfont.render('Player 1', True, grey), (500, 125))
                screen.blit(comicsansfont.render(f'{powerup_1}', True, grey), (500, 150))
            elif powerup_active_1:
                powerup_1.affect_player(player_car)
                powerup_1.affect_traffic(incoming_cars_1, player_car, cars_size, player_car_speed)
                screen.blit(comicsansfont.render('Player 1', True, grey), (500, 125))
                screen.blit(comicsansfont.render(f'{powerup_1}', True, grey), (500, 150))
                remaining_time = int((timer_1 + powerup_1.duration * 1000 - pygame.time.get_ticks()) / 1000)
                screen.blit(comicsansfont.render(f'{remaining_time} sec', True, grey),
                            (500, 175))

            # Player 2
            if powerup_active_1_2 and isinstance(powerup_1, (Mirror, Engorgio, Accelerator)):
                powerup_1.affect_player(player_car_2)
                powerup_1.affect_traffic(incoming_cars_2, player_car_2, cars_size, player2_car_speed)
                screen.blit(comicsansfont.render('Player 2', True, grey), (500, 225))
                screen.blit(comicsansfont.render(f'{powerup_1}', True, grey), (500, 250))
                remaining_time = int((timer_1 + powerup_1.duration * 1000 - pygame.time.get_ticks()) / 1000)
                screen.blit(comicsansfont.render(f'{remaining_time} sec', True, grey),
                            (500, 275))
            # Apply effects on Player 2, and show the type of power-up active and timer for the end of the effects
            if powerup_active_2 and isinstance(powerup_2, Shield):
                powerup_2.affect_player(player_car_2)
                powerup_2.affect_traffic(incoming_cars_2, player_car_2, cars_size, player2_car_speed)
                screen.blit(comicsansfont.render('Player 2', True, grey), (500, 225))
                screen.blit(comicsansfont.render(f'{powerup_2}', True, grey), (500, 250))
            elif powerup_active_2:
                powerup_2.affect_player(player_car_2)
                powerup_2.affect_traffic(incoming_cars_2, player_car_2, cars_size, player2_car_speed)
                screen.blit(comicsansfont.render('Player 2', True, grey), (500, 225))
                screen.blit(comicsansfont.render(f'{powerup_2}', True, grey), (500, 250))
                remaining_time = int((timer_2 + powerup_2.duration * 1000 - pygame.time.get_ticks()) / 1000)
                screen.blit(comicsansfont.render(f'{remaining_time} sec', True, grey),
                            (500, 275))

            # Deactivate powerups
            # Player 1
            if (powerup_active_1 and pygame.time.get_ticks() - timer_1 > powerup_1.duration * 1000 and
                    not isinstance(powerup_1, Shield)):
                # The power-up has expired
                powerup_active_1 = False
                player_car.image = pygame.transform.scale(player_car.image, (30, 60))  # In the case of shrink
                image_path = 'images/car_images/player_car/player_car_base.png'
                car_image = pygame.image.load(image_path).convert_alpha()
                player_car.image.blit(car_image, (0, 0))
                powerup_1 = generate_power_up()
                powerup_1.rect.x = random.choice([90, 190, 290, 390])
                powerup_1.rect.y = random.randint(-2000, -1000)
                powerups_1.add(powerup_1)

            if powerup_active_2_1 and pygame.time.get_ticks() - timer_2 > powerup_2.duration * 1000:
                powerup_active_2_1 = False
                player_car.image = pygame.transform.scale(player_car.image, (30, 60))  # In the case of shrink
                image_path = 'images/car_images/player_car/player_car_base.png'
                car_image = pygame.image.load(image_path).convert_alpha()
                player_car.image.blit(car_image, (0, 0))
                powerup_1 = generate_power_up()
                powerup_1.rect.x = random.choice([90, 190, 290, 390])
                powerup_1.rect.y = random.randint(-2000, -1000)
                powerups_1.add(powerup_1)

            # Player 2
            if (powerup_active_2 and pygame.time.get_ticks() - timer_2 > powerup_2.duration * 1000 and
                    not isinstance(powerup_2, Shield)):
                # The power-up has expired
                powerup_active_2 = False
                player_car_2.image = pygame.transform.scale(player_car_2.image, (30, 60))  # In the case of shrink
                image_path = 'images/car_images/player_car/player_car_2_base.png'
                car_image = pygame.image.load(image_path).convert_alpha()
                player_car_2.image.blit(car_image, (0, 0))
                powerup_2 = generate_power_up()
                powerup_2.rect.x = random.choice([690, 790, 890, 990])
                powerup_2.rect.y = random.randint(-2000, -1000)
                powerups_2.add(powerup_2)

            if powerup_active_1_2 and pygame.time.get_ticks() - timer_1 > powerup_1.duration * 1000:
                powerup_active_1_2 = False
                player_car_2.image = pygame.transform.scale(player_car_2.image, (30, 60))  # In the case of shrink
                image_path = 'images/car_images/player_car/player_car_2_base.png'
                car_image = pygame.image.load(image_path).convert_alpha()
                player_car_2.image.blit(car_image, (0, 0))
                powerup_2 = generate_power_up()
                powerup_2.rect.x = random.choice([690, 790, 890, 990])
                powerup_2.rect.y = random.randint(-2000, -1000)
                powerups_2.add(powerup_2)

            # Generate power-ups based on probability and if no power-up is currently active for player 1
            for powerup_1 in powerups_1:
                powerup_1.move_down(player_car_speed)
                if not powerup_active_1 and (powerup_collisions_1 or powerup_1.rect.y > 500):
                    powerups_1.empty()
                    powerup_1 = generate_power_up()
                    powerup_1.rect.x = random.choice([90, 190, 290, 390])
                    powerup_1.rect.y = random.randint(-2000, -1000)
                    powerups_1.add(powerup_1)

            # Generate power-ups based on probability and if no power-up is currently active for player 2
            for powerup_2 in powerups_2:
                powerup_2.move_down(player2_car_speed)
                if not powerup_active_2 and (powerup_collisions_2 or powerup_2.rect.y > 500):
                    powerups_2.empty()
                    powerup_2 = generate_power_up()
                    powerup_2.rect.x = random.choice([690, 790, 890, 990])
                    powerup_2.rect.y = random.randint(-2000, -1000)
                    powerups_2.add(powerup_2)

        all_sprites_list_1.draw(screen)
        all_sprites_list_2.draw(screen)
        powerups_1.draw(screen)
        powerups_2.draw(screen)
        all_sprites_list_1.update()
        all_sprites_list_2.update()
        powerups_1.update()
        powerups_2.update()

        if not pause:
            pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def game_over_multiplayer(winner):
    """
    Display the game over screen for a multiplayer game.

    This function creates a game over screen with the option to retry the game, return to the main menu, or quit.
    The screen displays the winner's page.

    Parameters
    ----------

    winner : bool
        A boolean value indicating the winner of the game.
        If True, displays Player 2's victory page.
        If False, displays Player 1's victory page.
    """
    # Coordinates for the window
    x = 450
    y = 100
    set_window_position(x, y)
    pygame.init()
    # Define game over screen and window name
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game Over")

    # Define font type and text to be displayed
    winner_1 = pygame.image.load('images/back_grounds/Player_1_wins.png').convert_alpha()
    winner_2 = pygame.image.load('images/back_grounds/Player_2_wins.png').convert_alpha()
    retry = pygame.image.load('images/button/retry.png').convert_alpha()
    retry_hoover = pygame.image.load('images/button/retry_hoover.png').convert_alpha()
    menu = pygame.image.load('images/button/main_menu.png').convert_alpha()
    menu_hoover = pygame.image.load('images/button/main_menu_hoover.png').convert_alpha()
    quit_ = pygame.image.load('images/button/quit.png').convert_alpha()
    quit_hoover = pygame.image.load('images/button/quit_hoover.png').convert_alpha()

    while True:
        mouse = pygame.mouse.get_pos()

        # Define events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 550 <= mouse[0] <= 659 and 300 <= mouse[1] <= 343:
                    multiplayer()
                if 550 <= mouse[0] <= 659 and 350 <= mouse[1] <= 393:
                    from interface import interface
                    from main import load_highest_score
                    highest_score = load_highest_score()  # Guarantee that the highest scores remains correct
                    interface(highest_score)
                if 550 <= mouse[0] <= 649 and 400 <= mouse[1] <= 443:
                    pygame.quit()

        # Draw Game Over flags, display the score and the text and the trophy
        if winner:
            screen.blit(winner_2, (0, 0))
        else:
            screen.blit(winner_1, (0, 0))

        # Draw Retry button
        if 550 <= mouse[0] <= 659 and 300 <= mouse[1] <= 343:
            screen.blit(retry_hoover, (550, 300))
        else:
            screen.blit(retry, (550, 300))

        # Draw Menu button
        if 550 <= mouse[0] <= 659 and 350 <= mouse[1] <= 393:
            screen.blit(menu_hoover, (550, 350))
        else:
            screen.blit(menu, (550, 350))

        # Draw Quit button
        if 550 <= mouse[0] <= 649 and 400 <= mouse[1] <= 443:
            screen.blit(quit_hoover, (550, 400))
        else:
            screen.blit(quit_, (550, 400))

        pygame.display.update()
