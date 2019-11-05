import pygame

#Variables
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640
WHITE = (255, 255, 255)
BASE_IMAGE = "fireworks_smaller"
BASE_IMAGE_EXTENSION = ".png"
ORIGIN = (0, 0)
REDUCTION_AMOUNT = 175

LESS_RED = 1
GREYSCALE = 2

EFFECT = { LESS_RED: "_less_red", GREYSCALE: "_total_colour_blind" } # could this be a dictionary of different effects?

#Initialising Pygame
pygame.init()
main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#Loading the image
original_image = pygame.image.load(BASE_IMAGE + BASE_IMAGE_EXTENSION).convert()

effect = None

def make_greyscale(surface, reduction_amount):
    """Function to loop through the image pixels to remove the red"""

    for x in range(0, surface.get_width()):
        for y in range(0, surface.get_height()):
            pixel_colour = surface.get_at((x, y))
            new_red = pixel_colour[0] - reduction_amount

            if new_red < 0:
                new_red = 0

            pixel_colour = (new_red, pixel_colour.g, pixel_colour.b)
            surface.set_at((x, y), pixel_colour)

    return GREYSCALE

def make_less_red(surface, reduction_amount):
    """Function to loop through the image pixels to remove the red"""

    for x in range(0, surface.get_width()):
        for y in range(0, surface.get_height()):
            pixel_colour = surface.get_at((x, y))
            new_red = pixel_colour[0] - reduction_amount

            if new_red < 0:
                new_red = 0

            pixel_colour = (new_red, pixel_colour.g, pixel_colour.b)
            surface.set_at((x, y), pixel_colour)

    return LESS_RED

effect = make_greyscale(original_image, REDUCTION_AMOUNT)

running = True
while running:

    main_window.fill(WHITE)
    main_window.blit(original_image, ORIGIN)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.image.save(original_image, BASE_IMAGE + EFFECT[effect] + BASE_IMAGE_EXTENSION)
            pygame.quit()
