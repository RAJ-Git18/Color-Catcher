import pygame
import math

# Colors
COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0)   # Yellow
]

class RotatingCircle:
    def __init__(self, center_x, center_y, radius, speed):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.angle = 0
        self.speed = speed

    def draw(self, screen):
        for i in range(len(COLORS)):
            start_angle = self.angle + (i * (2 * math.pi / len(COLORS)))
            end_angle = start_angle + (2 * math.pi / len(COLORS))
            color = COLORS[i]
            pygame.draw.arc(screen, color, (self.center_x - self.radius, self.center_y - self.radius, self.radius * 2, self.radius * 2), start_angle, end_angle, 10)

    def update(self):
        self.angle += self.speed

# Example usage
def main():
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Color Switch - Rotating Circle Obstacle")

    # Create the rotating circle
    circle = RotatingCircle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 100, 0.02)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        circle.update()
        circle.draw(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()