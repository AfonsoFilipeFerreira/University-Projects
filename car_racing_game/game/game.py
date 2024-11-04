import random
import pygame
import os
from car import Car
from powerups import Shield, Slowing, Invincible, Shrink, ScoreX2


# Save the highest score in a text file
def save_highest_score(highest_score):
    """
    Save the highest score in a text file.

    Parameters
    ----------

    - highest_score : int
        The highest score to be saved.
    """
    with open("highest_score.txt", "w") as file:
        file.write(str(highest_score))


# Function to set the window position
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


def game(highest_score):
    """
    Run the car racing game.

    This function initializes and runs a singleplayer car racing game.
    The Player control his car using arrow keys.
    The game includes randomly generated cars, power-ups, and a speedometer.

    The game window has a road, the road has 4 lanes with dashed lines and borders.
    The Player needs to avoid collisions with incoming cars and collect power-ups (only one at the time).

    Power-ups include:
        - Invincible: Makes the player's car invulnerable to collisions.
        - Shield: Creates a shield that protects the player from one collision.
        - Slowing: Slows down the speed of incoming cars temporarily.
        - Shrink: Shrinks the player's car for a short duration.

    The Player can pause the game by pressing the 'P' key.
    In pause mode, the player can continue the game, return to the main menu, or quit the game.

    The game has a scoring system and ends when the player collides with an incoming car.

    Parameters
    ----------

    - highest_score : int
        The highest score from previous games.
    """
    # Coordinates for the window
    x = 450
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
    size = (750, 500)
    screen = pygame.display.set_mode(size)
    surface = pygame.Surface(size, pygame.SRCALPHA)
    pygame.display.set_caption("Car Racing Game")

    # Define the player car and the 4 incoming cars
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

    incoming_cars = pygame.sprite.Group()
    incoming_cars.add(car1, car2, car3, car4)
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player_car, car1, car2, car3, car4)

    # Create power-up instances
    # As we want only one power-up to appear at the time we defined the probability spawn rates together
    def generate_power_up():
        """
        Generate a random power-up based on specified probabilities.
        Probability Distribution:
        - Invincible: 10%
        - Shield: 30%
        - Slowing: 25%
        - Shrink: 15%
        - ScoreX2 : 20%

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
        elif 0.80 < prob <= 1:
            powerup_class = ScoreX2()  # 20%
            return powerup_class

    powerup = generate_power_up()
    powerup.rect.x = random.choice([90, 190, 290, 390])
    powerup.rect.y = random.randint(-2000, -1000)
    powerups = pygame.sprite.Group()
    powerups.add(powerup)
    all_sprites_list.add(powerups)

    # Set a variable to track if a power-up is active
    powerup_active = False

    # Condition to maintain the loop and pause the game
    carry_on = True
    pause = False

    # Set the initial player car speed, the initial score, initialize the timer, timed paused (so power-ups do not
    # expire while on pause), and the font used to display the score and the speed and define images to load in game
    player_car_speed = 1
    comicsansfont = pygame.font.SysFont('Comic Sans MS', 25)
    speedometer = pygame.image.load('images/back_grounds/speedometer.png').convert_alpha()
    bck_pause = pygame.image.load('images/back_grounds/pause.png').convert_alpha()
    continue_ = pygame.image.load('images/button/continue.png').convert_alpha()
    continue_hoover = pygame.image.load('images/button/continue_hoover.png').convert_alpha()
    menu = pygame.image.load('images/button/main_menu.png').convert_alpha()
    menu_hoover = pygame.image.load('images/button/main_menu_hoover.png').convert_alpha()
    quit_ = pygame.image.load('images/button/quit.png').convert_alpha()
    quit_hoover = pygame.image.load('images/button/quit_hoover.png').convert_alpha()
    score = 0
    timer = 0
    time_paused = 0

    # Define Pause Menu
    def pause_menu():
        """
        Display the pause menu on the screen.

        This function draws a colored rectangle on the game screen to act as the background for the pause menu.
        It displays buttons for continuing the game, going to the main menu, and quitting the game.
        """
        # Color the game screen and display Pause Menu
        pygame.draw.rect(surface, pause_color, (0, 0, size[0], size[1]))
        screen.blit(surface, (0, 0))
        screen.blit(bck_pause, (205.5, 108))

        # Continue Button
        if 330 <= mouse[0] <= 429 and 220 <= mouse[1] <= 263:
            screen.blit(continue_hoover, (330, 220))
        else:
            screen.blit(continue_, (330, 220))

        # Menu Button
        if 330 <= mouse[0] <= 429 and 270 <= mouse[1] <= 313:
            screen.blit(menu_hoover, (330, 270))
        else:
            screen.blit(menu, (330, 270))

        # Quit Button
        if 330 <= mouse[0] <= 429 and 320 <= mouse[1] <= 363:
            screen.blit(quit_hoover, (330, 320))
        else:
            screen.blit(quit_, (330, 320))

        pygame.display.update()

    clock = pygame.time.Clock()

    # Loop of the game
    while carry_on:
        mouse = pygame.mouse.get_pos()  # Get Mouse position
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            # Close game
            if event.type == pygame.QUIT:
                carry_on = False
            # If P key is pressed
            if keys[pygame.K_p]:
                # Unpause the Game if the Game is Paused
                if pause:
                    pause = False  # Close Pause Menu and Resume the Game
                    # Get the time the game was Paused
                    time_diff = pygame.time.get_ticks() - time_paused
                    # Add the time the game was paused to the power-up timer to prevent the power-up expiring while
                    # Game is Pause
                    timer += time_diff
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
                    if 330 <= mouse[0] <= 429 and 220 <= mouse[1] <= 263:
                        pause = False  # Close Pause Menu and Resume the Game
                        # Get the time the game was Paused
                        time_diff = pygame.time.get_ticks() - time_paused
                        # Add the time the game was paused to the power-up timer to prevent the power-up expiring while
                        # Game is Pause
                        timer += time_diff
                    if 330 <= mouse[0] <= 429 and 270 <= mouse[1] <= 313:
                        # Go to Main Menu
                        from interface import interface
                        interface(highest_score)
                    if 330 <= mouse[0] <= 429 and 320 <= mouse[1] <= 363:
                        # Close the Game
                        pygame.quit()

        if not pause:
            # Set the controls of the game and the speed of the car
            if keys[pygame.K_LEFT]:
                player_car.move_left(5)
            if keys[pygame.K_RIGHT]:
                player_car.move_right(5)
            if keys[pygame.K_UP] and player_car.rect.y >= 30:
                player_car.move_up(5)
            if keys[pygame.K_DOWN] and player_car.rect.y <= 400:
                player_car.move_down(5)

        if pause:
            pause_menu()  # Call Pause Menu

        # Drawing the game
        screen.fill(bck)

        # Draw speedometer and car speed
        screen.blit(speedometer, [480, 400])
        speed = str(player_car_speed).split('.')[0]
        screen.blit(comicsansfont.render(f'{speed}', True, white), (522.5 if len(speed) == 1 else 515, 430))

        # Road
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

        if not pause:
            # Increase speed over time
            player_car_speed += 0.002

            # Generate incoming cars
            for car in incoming_cars:
                car.move_down(player_car_speed)
                if car.rect.y >= 500:
                    car.rect.y = random.randint(-500, -100)
                    car.change_speed(random.random() * 3)
                    car.incoming_cars_generator(random.choice(cars_size))

            # Car collision
            if powerup_active and isinstance(powerup, Shield):
                powerup.affect_traffic(incoming_cars, player_car, cars_size, player_car_speed)
                if powerup.duration == 1:
                    powerup_active = False
                    image_path = 'images/car_images/player_car/player_car_base.png'
                    car_image = pygame.image.load(image_path).convert_alpha()
                    player_car.image.blit(car_image, (0, 0))
                    powerup = generate_power_up()
                    powerup.rect.x = random.choice([90, 190, 290, 390])
                    powerup.rect.y = random.randint(-2000, -1000)
                    powerups.add(powerup)

            elif powerup_active and isinstance(powerup, Invincible):
                powerup.affect_traffic(incoming_cars, player_car, cars_size, player_car_speed)

            else:
                for car in incoming_cars:
                    if pygame.sprite.collide_mask(player_car, car) is not None:
                        # Pass the score value to the game over interface
                        game_over(score, highest_score)

            # Power-ups
            # Check for collisions with power-ups
            powerup_collisions = pygame.sprite.spritecollide(player_car, powerups, True)
            for powerup in powerup_collisions:
                # Set the active power-up
                powerup_active = True
                timer = pygame.time.get_ticks()
            # Apply the power-up effect
            if powerup_active and isinstance(powerup, Shield):
                powerup.affect_player(player_car)
                powerup.affect_traffic(incoming_cars, player_car, cars_size, player_car_speed)
                screen.blit(comicsansfont.render(f'Power-up:{powerup}', True, grey), (480, 250))
            elif powerup_active and not isinstance(powerup, Shield):
                powerup.affect_player(player_car)
                powerup.affect_traffic(incoming_cars, player_car, cars_size, player_car_speed)
                screen.blit(comicsansfont.render(f'Power-up:{powerup}', True, grey), (480, 250))
                remaining_time = int((timer + powerup.duration * 1000 - pygame.time.get_ticks()) / 1000)
                screen.blit(comicsansfont.render(f'Remaining Time: {remaining_time} sec', True, grey),
                            (480, 275))

            if (powerup_active and pygame.time.get_ticks() - timer > powerup.duration * 1000
                    and not isinstance(powerup, Shield)):
                # The power-up has expired
                powerup_active = False
                player_car.image = pygame.transform.scale(player_car.image, (30, 60))  # In the case of shrink
                image_path = 'images/car_images/player_car/player_car_base.png'
                car_image = pygame.image.load(image_path).convert_alpha()
                player_car.image.blit(car_image, (0, 0))
                powerup = generate_power_up()
                powerup.rect.x = random.choice([90, 190, 290, 390])
                powerup.rect.y = random.randint(-2000, -1000)
                powerups.add(powerup)

            # Generate power-ups based on probability and if no power-up is currently active
            for powerup in powerups:
                powerup.move_down(player_car_speed)
                if not powerup_active and (powerup_collisions or powerup.rect.y > 500):
                    powerups.empty()
                    powerup = generate_power_up()
                    powerup.rect.x = random.choice([90, 190, 290, 390])
                    powerup.rect.y = random.randint(-2000, -1000)
                    powerups.add(powerup)

            # Increment the score and display it
            if powerup_active and isinstance(powerup, ScoreX2):
                score_increment = 0.3 * player_car_speed * 2
            else:
                score_increment = 0.3 * player_car_speed
            score += score_increment
            screen.blit(comicsansfont.render(f'Score:{int(score)}', True, grey), (550, 50))

            # Update the highest_score
            if score > highest_score:
                highest_score = score
                save_highest_score(int(highest_score))
            screen.blit(comicsansfont.render(f'Highest Score:{int(highest_score)}', True, grey), (480, 25))

        all_sprites_list.draw(screen)
        powerups.draw(screen)
        all_sprites_list.update()
        powerups.update()

        if not pause:
            pygame.display.flip()

        clock.tick(60)
    pygame.quit()


# Set a game over page when a crash occurs
def game_over(score, highest_score):
    """
    Display the game over screen, the player's score,
    and provides options to retry the game, go to the main menu, or quit the game.

    Parameters
    ----------

    - score : float
        The player's score at the end of the game.

    - highest_score : float
        The highest score achieved in the game.
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

    # Colors
    white = (255, 255, 255)

    # Define font type and text to be displayed
    comicsansfont = pygame.font.SysFont('Comic Sans MS', 25)
    retry = pygame.image.load('images/button/retry.png').convert_alpha()
    retry_hoover = pygame.image.load('images/button/retry_hoover.png').convert_alpha()
    menu = pygame.image.load('images/button/main_menu.png').convert_alpha()
    menu_hoover = pygame.image.load('images/button/main_menu_hoover.png').convert_alpha()
    quit_ = pygame.image.load('images/button/quit.png').convert_alpha()
    quit_hoover = pygame.image.load('images/button/quit_hoover.png').convert_alpha()
    bck = pygame.image.load('images/back_grounds/game_over.png').convert_alpha()

    while True:
        mouse = pygame.mouse.get_pos()

        # Define events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 550 <= mouse[0] <= 659 and 300 <= mouse[1] <= 343:
                    game(highest_score)
                if 550 <= mouse[0] <= 659 and 350 <= mouse[1] <= 393:
                    from interface import interface
                    interface(highest_score)
                if 550 <= mouse[0] <= 649 and 400 <= mouse[1] <= 443:
                    pygame.quit()

        screen.blit(bck, (0, 0))

        # Display the score and the text
        screen.blit(comicsansfont.render(f'Score:{int(score)}', True, white), (530, 250))

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
