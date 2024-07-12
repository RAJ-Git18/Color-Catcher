import pygame


# class to create a ball
class Ball:
    def __init__(self, screen, color, radius):
        self.screen = screen
        self.color = color
        self.radius = radius

    def draw_ball(self, x, y):
        self.x = x
        self.y = y
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)