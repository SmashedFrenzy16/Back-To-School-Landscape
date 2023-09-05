import pygame

pygame.init()

# Constants for colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Create the screen
screen_width, screen_height = 800, 520
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Back to School Landscape")

# Load images (Credit to freepik for the images)
background_image = pygame.image.load("background.jpg")
school_image = pygame.image.load("school.png")

# Define the school building's position and size
school_x = 100
school_y = 150
school_width = 400
school_height = 300

# Text positioning variables
text_x = 750
text_y = 330

# Text defining
font = pygame.font.Font('freesansbold.ttf', 32)

text = font.render("Back To School 2023", True, BLACK)

text_rect = text.get_rect()

text_rect.center = (text_x // 2, text_y // 2)

# Main game loop
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            
            running = False

    screen.blit(background_image, (0, 0))

    screen.blit(school_image, (school_x, school_y))

    screen.blit(text, text_rect)

    pygame.display.update()

pygame.quit()


