import pygame
import ball


def gameLoop():
    background_colour = (234, 212, 252)

    screen = pygame.display.set_mode((1550, 800), pygame.RESIZABLE)

    pygame.display.set_caption("Color Balls")

    ball_position_x = 400
    ball_position_y = 500

    # objects of the ball
    ball_purple = ball.Ball(screen, background_colour, 25)

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
        if ball_up:
            if ball_position_y > 300:
                ball_position_y -= 0.2
            else:
                ball_up = False
        elif ball_position_y <= 500:
            ball_up = False
            ball_position_y += 0.2

        # drawing the purple ball
        ball_purple.draw_ball(ball_position_x, ball_position_y)

        pygame.display.update()
