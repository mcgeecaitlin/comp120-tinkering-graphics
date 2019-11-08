import pygame

__author__ = "Caitlin McGee"
__copyright__ = "MIT License Copyright (c) 2019"
__license__ = "MIT"
__url__ = "https://github.com/mcgeecaitlin/comp120-tinkering-graphics"

"""
This program is designed to remove colour from an image, relevant to a type of colour blindness.
After the image has been processed it is saved under a new name.

The image fireworks.png is an image I own the rights to.
"""

# Variables for pop up window
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640
WHITE = (255, 255, 255)

# Variables for base image of fireworks
BASE_IMAGE = "fireworks"
BASE_IMAGE_EXTENSION = ".png"
ORIGIN = (0, 0)

# Variables for colour reduction
REDUCTION_AMOUNT = 100
RED_REDUCTION_AMOUNT = 200
BLUE_REDUCTION_AMOUNT = 125

# Dictionary variables and dictionary
LESS_RED = 1
LESS_BLUE = 2
GREYSCALE = 3
EFFECT = {LESS_RED: "_less_red", LESS_BLUE: "_less_blue", GREYSCALE: "_total_colour_blind"}

# Initialising PyGame
pygame.init()
main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Loading the original image
original_image = pygame.image.load(BASE_IMAGE + BASE_IMAGE_EXTENSION).convert()


def main():
    """
    This function saves three new images for the three types of colour blindness.
    It contains a loop which updates the program every frame.
    """
    main_window.fill(WHITE)

    # Saving the make_less_red image under a new name
    effect = make_less_red(original_image, RED_REDUCTION_AMOUNT)
    pygame.image.save(original_image, BASE_IMAGE + EFFECT[effect] + BASE_IMAGE_EXTENSION)

    # Saving the make_less_blue_green image under a new name
    effect = make_less_blue(original_image, BLUE_REDUCTION_AMOUNT)
    pygame.image.save(original_image, BASE_IMAGE + EFFECT[effect] + BASE_IMAGE_EXTENSION)

    # Saving the greyscale image under a new name
    effect = make_greyscale(original_image)
    pygame.image.save(original_image, BASE_IMAGE + EFFECT[effect] + BASE_IMAGE_EXTENSION)

    main_window.blit(original_image, ORIGIN)

    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

                pygame.quit()


def make_less_red(surface, red_reduction_amount):
    """
    This function is to replicate an image of the colour blindness protanopia.
    The function will loop through the image pixels to remove red colouring.
    """

    for x in range(0, surface.get_width()):
        for y in range(0, surface.get_height()):
            pixel_colour = surface.get_at((x, y))
            new_red = pixel_colour[0] - red_reduction_amount

            if new_red < 0:
                new_red = 0

            pixel_colour = (new_red, pixel_colour.g, pixel_colour.b)
            surface.set_at((x, y), pixel_colour)

    return LESS_RED


def make_less_blue(surface, blue_reduction_amount):
    """
    This function is to replicate an image of colour blindness tritanopia.
    The function will loop through the image pixels to remove blue colouring.
    """

    for x in range(0, surface.get_width()):
        for y in range(0, surface.get_height()):
            pixel_colour = surface.get_at((x, y))
            new_blue = pixel_colour.b - blue_reduction_amount

            if new_blue < 0:
                new_blue = 0

            pixel_colour = (pixel_colour.r, pixel_colour.g, new_blue)
            surface.set_at((x, y), pixel_colour)

    return LESS_BLUE


def make_greyscale(surface):
    """
    This function is to replicate an image of colour blindness monochromacy.
    Function to loop through the image pixels to remove colour.
    """

    for x in range(0, surface.get_width()):
        for y in range(0, surface.get_height()):
            pixel_colour = surface.get_at((x, y))
            new_red = pixel_colour.r
            new_green = pixel_colour.g
            new_blue = pixel_colour.b

            if new_red < 0:
                new_red = 0

            if new_green < 0:
                new_green = 0

            if new_blue < 0:
                new_blue = 0

            greyscale_pixel_value = (new_red + new_green + new_blue)/3

            pixel_colour = (greyscale_pixel_value, greyscale_pixel_value, greyscale_pixel_value)
            surface.set_at((x, y), pixel_colour)

    return GREYSCALE


if __name__ == '__main__':
    main()
