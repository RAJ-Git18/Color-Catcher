import pygame
import ball
from obstacles import RotatingCircle


def gameLoop():
    red_color = (255, 0, 0)
    blue_color = (0, 0, 255)
    green_color = (0, 255, 0)
    yellow_color = (255, 255, 0)
    background_colour = (234, 212, 252)

    screen = pygame.display.set_mode((1550, 800), pygame.RESIZABLE)

    pygame.display.set_caption("Color Balls")

    ball_position_x = 775
    ball_position_y = 500

    # Create the rotating circle
    circle = RotatingCircle(1550 // 2, 800 // 2, 200, 0.003)

    # objects of the ball
    ball_red = ball.Ball(screen, red_color, 20)

    # to make the window run
    running = True

    ball_up = True

    # game loop
    while running:
        screen.fill(color="black")
        # for loop through the event queue
        for event in pygame.event.get():

            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_UP:
            #         while ball_position_y != 300:
            #             ball_position_y -= 1
            #             ball_purple = ball.Ball(
            #                 screen, background_colour, ball_position_x, ball_position_y, 25
            #             )

            #             print(ball_position_y)

        # Update and draw the rotating circle
        circle.update()
        circle.draw(screen)

        if ball_up:
            if ball_position_y > 300:
                ball_position_y -= 0.5
            else:
                ball_up = False
        elif ball_position_y <= 500:
            ball_up = False
            ball_position_y += 0.5

        # drawing the purple ball
        ball_red.draw_ball(ball_position_x, ball_position_y)

        pygame.display.update()