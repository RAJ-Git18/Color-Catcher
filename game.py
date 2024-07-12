import pygame
import ball

pygame.init()


def gameLoop():

    background_colour = (234, 212, 252)
    screen = pygame.display.set_mode((1550, 800), pygame.RESIZABLE)
    pygame.display.set_caption("Color Balls")

    ball_position_x = 770
    ball_position_y = 650

    # Object of the ball
    ball_purple = ball.Ball(screen, background_colour, 25)

    # To make the window run
    running = True

    # To make the ball move up
    up_position = False
    down_position = False

    # Game loop
    while running:
        screen.fill(color="black")

        # For loop through the event queue
        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    up_position = True

        if up_position:
            if ball_position_y > 300:
                ball_position_y -= 0.8
            else:
                up_position = False
                down_position = True
        if down_position:
            if ball_position_y < 650:
                ball_position_y += 0.8
            else:
                down_position = False

        # Drawing the purple ball
        ball_purple.draw_ball(ball_position_x, ball_position_y)

        pygame.display.update()


gameLoop()
