import pygame

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 1400
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Color-Switch Menu")

# Load the background image
background_image = pygame.image.load("background_img.jpg").convert()

whiteColor = (255, 255, 255)


# Game text to be displayed on the screen
font1 = pygame.font.Font("font/myfont.ttf", 60)
gameName = font1.render("COLOR-SWITCH GAME", True, whiteColor)

# start text to be displayed on the screen
font2 = pygame.font.Font("font/myfont.ttf", 48)
start_text = font2.render("START", True, whiteColor)
start_box = start_text.get_rect(center=(700, 250))

# exit text to be displayed on the screen
font3 = pygame.font.Font("font/myfont.ttf", 48)
exit_text = font3.render("EXIT", True, whiteColor)
exit_box = exit_text.get_rect(center=(700, 350))

# Scale the background image to fit the screen
background_image = pygame.transform.scale(
    background_image, (screen_width, screen_height)
)

# Main game loop
running = True
while running:

    new_width = screen.get_width()
    new_height = screen.get_height()

    screen.blit(background_image, (0, 0))

    screen.blit(gameName, (450, 100))
    screen.blit(start_text, start_box)
    screen.blit(exit_text, exit_box)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if exit_box.collidepoint(event.pos):
                running = False

    # Update display
    pygame.display.update()
