import random
import pygame
from abc import ABC, abstractmethod

white = (255, 255, 255)
green = (111, 194, 118)
blue = (173, 216, 230)
black = (51, 51, 51)


class PowerUp(pygame.sprite.Sprite, ABC):
    """
    A class to represent a power-up.

    Attributes
    ----------

    image_path : str
        The file path to the image used for the power-up.

    duration : int
        The duration of the power-up effect.

    Methods
    -------

    affect_player(player_car)
        Abstract method to define how the power-up affects the player's car.

    affect_traffic(incoming_cars, player_car, cars_size, player_car_speed)
        Abstract method to define how the power-up affects traffic (incoming cars).

    move_down(player_car_speed)
        Move the power-up downward based on the player's car speed.
    """
    def __init__(self, image_path, duration=0):
        """
        Constructs all the necessary attributes for the power-up object.

        Parameters
        ----------

        image_path : str
            The file path to the image used for the power-up.

        duration : int
            The duration of the power-up effect (default is 0).
        """
        super().__init__()
        self.image = pygame.Surface([40, 40], pygame.SRCALPHA)
        self.image.fill(black)
        self.image.set_colorkey(black)
        self.duration = duration
        power_up_image = pygame.image.load(image_path).convert_alpha()
        self.image.blit(power_up_image, (0, 0))
        self.rect = self.image.get_rect()

    @abstractmethod
    def affect_player(self, player_car):
        """
        Abstract method to define how the power-up affects the player's car.

        Parameters
        ----------
        player_car : Car
            The player's car object.
        """
        pass

    @abstractmethod
    def affect_traffic(self, incoming_cars, player_car, cars_size, player_car_speed):
        """
        Abstract method to define how the power-up affects traffic (incoming cars).

        Parameters
        ----------

        incoming_cars : list
            List of incoming car objects.

        player_car : Car
            The player's car object.

        cars_size : tuple
            Tuple containing the width, height, and image path for incoming cars.

        player_car_speed : int
            The speed of the player's car.
        """
        pass

    def move_down(self, player_car_speed):
        """
        Move the power-up downward based on the player's car speed.

        Parameters
        ----------

        player_car_speed : int
            The speed of the player's car.
        """
        if player_car_speed <= 5:
            self.rect.y += player_car_speed
        else:
            self.rect.y += 5


class Invincible(PowerUp):
    """
        A class representing an invincibility power-up.

        Attributes
        ----------
        image_path : str
            The path to the image of the power-up.

        duration : int
            The duration of the invincibility effect.

        Methods
        -------

        affect_player(player_car)
            Set the player's car new color to show that the power-up is active

        affect_traffic(incoming_cars, player_car, cars_size, player_car_speed)
            Affect traffic when the player has the invincibility power-up.
        """
    def __init__(self):
        super().__init__('images/power_ups/invincible.png', 10)

    def affect_player(self, player_car):
        """
        Set the player's car new color to show that the power-up is active

        Parameters
        ----------

        player_car : Car
            The player's car object.
        """
        image_path = 'images/car_images/player_car/player_car_invincible.png'
        car_image = pygame.image.load(image_path).convert_alpha()
        player_car.image.blit(car_image, (0, 0))

    def affect_traffic(self, incoming_cars, player_car, cars_size, player_car_speed):
        """
        Remove incoming cars upon collision with the player's car.

        Parameters
        ----------

        incoming_cars : list
            List of incoming car objects.

        player_car : Car
            The player's car object.

        cars_size : tuple
            Tuple containing the width, height, and image path for incoming cars.

        player_car_speed : int
            The speed of the player's car.
        """
        for car in incoming_cars:
            if pygame.sprite.collide_mask(player_car, car) is not None:
                # Set the car's position off-screen to simulate collision
                car.rect.y = random.randint(-500, -100)
                car.change_speed(random.randint(1, 3))
                car.incoming_cars_generator(random.choice(cars_size))

    def __repr__(self):
        return 'Invincible'


class Shield(PowerUp):
    """
    A class representing a Shield power-up.

    Attributes
    ----------

    image_path : str
        The path to the image of the power-up.

    duration : int
        The duration of the Shield power-up (default is 0).

    Methods
    -------

    affect_player(player_car)
        Set the player's car new color to show that the power-up is active

    affect_traffic(incoming_cars, player_car, cars_size, player_car_speed)
        Checks for a collision to set the duration to 1
    """
    def __init__(self):
        super().__init__('images/power_ups/shield.png', 0)

    def affect_player(self, player_car):
        """
        Set the player's car new color to show that the power-up is active

        Parameters
        ----------

        player_car : Car
            The player's car object.
        """
        image_path = 'images/car_images/player_car/player_car_shield.png'
        car_image = pygame.image.load(image_path).convert_alpha()
        player_car.image.blit(car_image, (0, 0))

    def affect_traffic(self, incoming_cars, player_car, cars_size, player_car_speed):
        """
        Checks for a collision to set the duration to 1

        Parameters
        ----------

        incoming_cars : list
            List of incoming cars.

        player_car : Car
            The player's car object.

        cars_size : list
            List of car sizes.

        player_car_speed : int
            The speed of the player's car.
        """
        for car in incoming_cars:
            if pygame.sprite.collide_mask(player_car, car) is not None:
                # Set the car's position off-screen to simulate collision
                car.rect.y = random.randint(-500, -100)
                car.change_speed(random.randint(1, 3))
                car.incoming_cars_generator(random.choice(cars_size))
                self.duration = 1

    def __repr__(self):
        return 'Shield'


class Slowing(PowerUp):
    """
    A class representing a Slowing power-up.

    Attributes
    ----------

    image_path : str
        The path to the image of the power-up.

    duration : int
        The duration of the Slowing power-up (default is 10).

    Methods
    -------

    affect_player(player_car)
        Set the player's car new color to show that the power-up is active

    affect_traffic(incoming_cars, player_car, cars_size, player_car_speed)
        Apply the Slowing power-up effect to incoming traffic.
    """
    def __init__(self):
        super().__init__('images/power_ups/slowdown.png', 10)

    def affect_player(self, player_car):
        """
        Set the player's car new color to show that the power-up is active

        Parameters
        ----------

        player_car : Car
            The player's car object.
        """
        image_path = 'images/car_images/player_car/player_car_slowdown.png'
        car_image = pygame.image.load(image_path).convert_alpha()
        player_car.image.blit(car_image, (0, 0))

    def affect_traffic(self, incoming_cars, player_car, cars_size, player_car_speed):
        """
        Apply the Slowing power-up effect to incoming traffic.

        Parameters
        ----------

        incoming_cars : list
            List of incoming cars.

        player_car : Car
            The player's car object.

        cars_size : list
            List of car sizes.

        player_car_speed : int
            The speed of the player's car.
        """
        for car in incoming_cars:
            car.speed = - player_car_speed/2

    def __repr__(self):
        return 'Slowing'


class Shrink(PowerUp):
    """
    A class representing a Shrink power-up.

    Attributes
    ----------
    image_path : str
        The path to the image of the power-up.
    duration : int
        The duration of the Shrink power-up.

    Methods
    -------

    affect_player(player_car)
        Set the player's car new color to show that the power-up is active
        Apply the Shrink power-up effect to the player's car.

    affect_traffic(incoming_cars, player_car, cars_size, player_car_speed)
        Apply the Shrink power-up effect to incoming traffic.
    """
    def __init__(self):
        super().__init__('images/power_ups/shrink.png', 10)

    def affect_player(self, player_car):
        """
        Set the player's car new color to show that the power-up is active
        Apply the Shrink power-up effect to the player's car.

        Parameters
        ----------

        player_car : Car
            The player's car object.
        """
        player_car.image = pygame.transform.scale(player_car.image, (15, 30))
        image_path = 'images/car_images/player_car/player_car_shrink.png'
        car_image = pygame.image.load(image_path).convert_alpha()
        player_car.image.blit(car_image, (0, 0))

    def affect_traffic(self, incoming_cars, player_car, cars_size, player_car_speed):
        """
        Parameters
        ----------

        incoming_cars : list
            List of incoming cars.

        player_car : Car
            The player's car object.

        cars_size : list
            List of car sizes.

        player_car_speed : int
            The speed of the player's car.
        """
        pass

    def __repr__(self):
        return 'Shrink'


class ScoreX2(PowerUp):
    """
    A class representing a Score X2 power-up.

    Attributes
    ----------
    image_path : str
        The path to the image of the power-up.

    duration : int
        The duration of the Score X2 power-up.

    Methods
    -------

    affect_player(player_car)
        Set the player's car new color to show that the power-up is active

    affect_traffic(incoming_cars, player_car, cars_size, player_car_speed)
        ...
    """
    def __init__(self):
        super().__init__('images/power_ups/score_x2.png', 10)

    def affect_player(self, player_car):
        """
        Set the player's car new color to show that the power-up is active

        Parameters
        ----------

        player_car : Car
            The player's car object.
        """
        image_path = 'images/car_images/player_car/player_car_score_x2.png'
        car_image = pygame.image.load(image_path).convert_alpha()
        player_car.image.blit(car_image, (0, 0))

    def affect_traffic(self, incoming_cars, player_car, cars_size, player_car_speed):
        """
        Parameters
        ----------

        incoming_cars : list
            List of incoming cars.

        player_car : Car
            The player's car object.

        cars_size : list
            List of car sizes.

        player_car_speed : int
            The speed of the player's car.
        """
        pass

    def __repr__(self):
        return 'Score X2'


class Accelerator(PowerUp):
    """
    Increases the speed of the traffic.

    Parameters
    ----------
    image_path : str
        The path to the image of the power-up.

    duration : int
        The duration of the Accelerator power-up.

    Methods
    -------

    affect_player(player_car):
        Set the player's car new color to show that the power-up is active

    affect_traffic(incoming_cars, player_car, cars_size, player_car_speed):
        Changes the speed of all incoming cars of the other player.
    """
    def __init__(self):
        super().__init__('images/power_ups/accelerator.png', 5)

    def affect_player(self, player_car):
        """
        Set the player's car new color to show that the power-up is active

        Parameters
        ----------

        player_car : Car
            The player's car object.
        """
        image_path = 'images/car_images/player_car/player_car_accelerator.png'
        car_image = pygame.image.load(image_path).convert_alpha()
        player_car.image.blit(car_image, (0, 0))

    def affect_traffic(self, incoming_cars, player_car, cars_size, player_car_speed):
        """
        Parameters
        ----------

        incoming_cars : list
            List of incoming cars.

        player_car : Car
            The player's car object.

        cars_size : list
            List of car sizes.

        player_car_speed : int
            The speed of the player's car.
        """
        for car in incoming_cars:
            car.speed = 5

    def __repr__(self):
        return 'Accelerator'


class Engorgio(PowerUp):
    """
    Increases the speed of the traffic.

    Parameters
    ----------
    image_path : str
        The path to the image of the power-up.

    duration : int
        The duration of the Accelerator power-up.

    Methods
    -------

    affect_player(player_car):
        Set the player's car new color to show that the power-up is active

    affect_traffic(incoming_cars, player_car, cars_size, player_car_speed):
        ...
    """
    def __init__(self):
        super().__init__('images/power_ups/engorgio.png', 5)

    def affect_player(self, player_car):
        """
        Set the player's car new color to show that the power-up is active

        Parameters
        ----------

        player_car : Car
            The player's car object.
        """
        player_car.image = pygame.transform.scale(player_car.image, (45, 90))
        image_path = 'images/car_images/player_car/player_car_engorgio.png'
        car_image = pygame.image.load(image_path).convert_alpha()
        player_car.image.blit(car_image, (0, 0))

    def affect_traffic(self, incoming_cars, player_car, cars_size, player_car_speed):
        """
        Parameters
        ----------

        incoming_cars : list
            List of incoming cars.

        player_car : Car
            The player's car object.

        cars_size : list
            List of car sizes.

        player_car_speed : int
            The speed of the player's car.
        """
        pass

    def __repr__(self):
        return 'Engorgio'


class Mirror(PowerUp):
    """
    Inverts the other player controls (up is down, down is up, right is left, left is right)

    Parameters
    ----------
    image_path : str
        The path to the image of the power-up.

    duration : int
        The duration of the Accelerator power-up.

    Methods
    -------

    affect_player(player_car):
        Set the player's car new color to show that the power-up is active

    affect_traffic(incoming_cars, player_car, cars_size, player_car_speed):
        ...
    """
    def __init__(self):
        super().__init__('images/power_ups/mirror.png', 5)

    def affect_player(self, player_car):
        """
        Set the player's car new color to show that the power-up is active

        Parameters
        ----------

        player_car : Car
            The player's car object.
        """
        image_path = 'images/car_images/player_car/player_car_mirror.png'
        car_image = pygame.image.load(image_path).convert_alpha()
        player_car.image.blit(car_image, (0, 0))

    def affect_traffic(self, incoming_cars, player_car, cars_size, player_car_speed):
        """
        Parameters
        ----------

        incoming_cars : list
            List of incoming cars.

        player_car : Car
            The player's car object.

        cars_size : list
            List of car sizes.

        player_car_speed : int
            The speed of the player's car.
        """
        pass

    def __repr__(self):
        return 'Mirror'
