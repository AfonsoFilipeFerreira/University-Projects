import pygame

white = (255, 255, 255)
black = (51, 51, 51)


class Car(pygame.sprite.Sprite):
    """
    A class to represent a car.

    Attributes
    ----------

    image_path : str
        The file path to the image used for the car.

    width : int
        The width of the car sprite.

    height : int
        The height of the car sprite.

    speed : int
        The initial speed of the car (default is 0).

    lane : int
        The lane in which the car is located (default is 0).

    Methods
    -------

    move_right(pixels)
        Move the car to the right by a specified number of pixels.

    move_left(pixels)
        Move the car to the left by a specified number of pixels.

    move_up(pixels)
        Move the car upward by a specified number of pixels.

    move_down(player_car_speed)
        Move the car downward based on its speed and the player's car speed.

    incoming_cars_generator(size)
        Generate incoming cars on the specified lane.

    change_speed(new_speed)
        Change the speed of the car.
    """
    def __init__(self, image_path, width, height, speed=0, lane=0):
        """
        Constructs all the necessary attributes for the car object.

        Parameters
        ----------

        image_path : str
            The file path to the image used for the car.

        width : int
            The width of the car sprite.

        height : int
            The height of the car sprite.

        speed : int
            The initial speed of the car (default is 0).

        - lane : int
            The lane in which the car is located (default is 0).
        """
        super().__init__()

        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image.fill(black)
        self.image.set_colorkey(black)
        self.width = width
        self.height = height
        self.lane = lane

        car_image = pygame.image.load(image_path).convert_alpha()
        self.image.blit(car_image, (0, 0))

        self.rect = self.image.get_rect()
        self.speed = speed

    def move_right(self, pixels):
        """
        Move the car to the right by a specified number of pixels.

        Parameters
        ----------

        pixels : int
            The number of pixels to move the car to the right.
        """
        if 60 <= self.rect.x <= 460:
            if self.rect.x > 425:
                self.rect.x += 0
            else:
                self.rect.x += pixels
        if 660 <= self.rect.x <= 1060:
            if self.rect.x > 1025:
                self.rect.x += 0
            else:
                self.rect.x += pixels

    def move_left(self, pixels):
        """
        Move the car to the left by a specified number of pixels.

        Parameters
        ----------

        pixels : int
            The number of pixels to move the car to the left.
        """
        if 60 <= self.rect.x <= 460:
            if self.rect.x < 65:
                self.rect.x += 0
            else:
                self.rect.x -= pixels
        if 660 <= self.rect.x <= 1060:
            if self.rect.x < 665:
                self.rect.x += 0
            else:
                self.rect.x -= pixels

    def move_up(self, pixels):
        """
        Move the car upward by a specified number of pixels.

        Parameters
        ----------

        pixels : int
            The number of pixels to move the car upward.
        """
        self.rect.y -= pixels

    def move_down(self, player_car_speed):
        """
        Move the car downward based on its speed and the player's car speed.

        Parameters
        ----------

        player_car_speed : int
            The speed of the player's car.
        """
        pixels = self.speed + player_car_speed
        self.rect.y += pixels

    def incoming_cars_generator(self, size):
        """
        Generate incoming cars on the specified lane.

        Parameters
        ----------

        size : tuple
            A tuple containing the width, height, and image path for the incoming car.
        """
        width = size[0]
        height = size[1]
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        car_image = pygame.image.load(size[2]).convert_alpha()
        self.image.blit(car_image, (0, 0))
        self.rect.x = (self.lane * 100) + (20 - size[0])/2

    def change_speed(self, new_speed):
        """
        Change the speed of the car.

        Parameters
        ----------

        new_speed : int
            The new speed value.
        """
        self.speed = new_speed
