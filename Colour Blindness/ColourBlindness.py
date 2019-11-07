import pygame

# Variables
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640
WHITE = (255, 255, 255)
BASE_IMAGE = "fireworks"
BASE_IMAGE_EXTENSION = ".png"
ORIGIN = (0, 0)
# Variables for colour reduction
REDUCTION_AMOUNT = 100
RED_REDUCTION_AMOUNT = 175
GREEN_REDUCTION_AMOUNT = 100
BLUE_REDUCTION_AMOUNT = 100

LESS_RED = 1
LESS_BLUE_GREEN = 2
GREYSCALE = 3
# could this be a dictionary of different effects?
EFFECT = {LESS_RED: "_less_red", LESS_BLUE_GREEN: "_less_blue_green", GREYSCALE: "_total_colour_blind"}

# Initialising PyGame
pygame.init()
main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Loading the original image
original_image = pygame.image.load(BASE_IMAGE + BASE_IMAGE_EXTENSION).convert()


def main():
    main_window.fill(WHITE)
    main_window.blit(original_image, ORIGIN)

    effect = make_less_red(original_image, RED_REDUCTION_AMOUNT)
    # Saving the make_less_red image under a new name
    pygame.image.save(original_image, BASE_IMAGE + EFFECT[effect] + BASE_IMAGE_EXTENSION)

    effect = make_less_blue_green(original_image, GREEN_REDUCTION_AMOUNT, BLUE_REDUCTION_AMOUNT)
    # Saving the make_less_blue_green image under a new name
    pygame.image.save(original_image, BASE_IMAGE + EFFECT[effect] + BASE_IMAGE_EXTENSION)

    effect = make_greyscale(original_image, REDUCTION_AMOUNT)
    # Saving the greyscale image under a new name
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
    """Function to loop through the image pixels to remove red colouring"""

    for x in range(0, surface.get_width()):
        for y in range(0, surface.get_height()):
            pixel_colour = surface.get_at((x, y))
            new_red = pixel_colour[0] - red_reduction_amount

            if new_red < 0:
                new_red = 0

            pixel_colour = (new_red, pixel_colour.g, pixel_colour.b)
            surface.set_at((x, y), pixel_colour)

    return LESS_RED


def make_less_blue_green(surface, green_reduction_amount, blue_reduction_amount):
    """Function to loop through the image pixels to remove blue and green colouring"""

    for x in range(0, surface.get_width()):
        for y in range(0, surface.get_height()):
            pixel_colour = surface.get_at((x, y))
            new_green = pixel_colour.g - green_reduction_amount
            new_blue = pixel_colour.b - blue_reduction_amount

            if new_green < 0:
                new_green = 0

            if new_blue < 0:
                new_blue = 0

            pixel_colour = (pixel_colour.r, new_green, new_blue)
            surface.set_at((x, y), pixel_colour)

    return LESS_BLUE_GREEN


def make_greyscale(surface, reduction_amount):
    """Function to loop through the image pixels to remove colour"""

    for x in range(0, surface.get_width()):
        for y in range(0, surface.get_height()):
            pixel_colour = surface.get_at((x, y))
            new_red = pixel_colour.r - reduction_amount
            new_green = pixel_colour.g - reduction_amount
            new_blue = pixel_colour.b - reduction_amount

            if new_red < 0:
                new_red = 0

            if new_green < 0:
                new_green = 0

            if new_blue < 0:
                new_blue = 0

            pixel_colour = (new_red, new_green, new_blue)
            surface.set_at((x, y), pixel_colour)

    return GREYSCALE


if __name__ == '__main__':
    main()
