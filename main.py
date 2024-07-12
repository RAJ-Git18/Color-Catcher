import pygame
import game


# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 1550
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Color-Switch Menu")

# Load the background image
background_image = pygame.image.load("background_img.jpg").convert()

# load the background music
background_music = pygame.mixer.music.load("sounds/bgmusic.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)

whiteColor = (255, 255, 255)


# Game text to be displayed on the screen
font1 = pygame.font.Font("font/myfont.ttf", 60)
gameName = font1.render("COLOR-SWITCH GAME", True, whiteColor)

# start text to be displayed on the screen
font2 = pygame.font.Font("font/myfont.ttf", 48)
start_text = font2.render("START", True, whiteColor)
start_box = start_text.get_rect(center=(800, 250))

# exit text to be displayed on the screen
font3 = pygame.font.Font("font/myfont.ttf", 48)
exit_text = font3.render("EXIT", True, whiteColor)
exit_box = exit_text.get_rect(center=(800, 350))

# Scale the background image to fit the screen
background_image = pygame.transform.scale(
    background_image, (screen.get_width(), screen.get_height())
)


# Main game loop
running = True
while running:

    screen.blit(background_image, (0, 0))

    screen.blit(gameName, (500, 100))
    screen.blit(start_text, start_box)
    screen.blit(exit_text, exit_box)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if exit_box.collidepoint(event.pos):
                running = False
            if start_box.collidepoint(event.pos):
                game.gameLoop()

    # Update display
    pygame.display.update()

