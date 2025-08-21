import pygame
from constants import Config


class Ball:
    def __init__(self):
        self.x = Config.SCREEN_WIDTH // 2
        self.y = Config.SCREEN_HEIGHT // 2
        self.radius = 8
        self.color = (255, 0, 0)
        self.speed_x = 5
        self.speed_y = 3

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off walls
        if self.x - self.radius < 0 or self.x + self.radius > Config.SCREEN_WIDTH:
            self.speed_x *= -1
        if self.y - self.radius < 0 or self.y + self.radius > Config.SCREEN_HEIGHT:
            self.speed_y *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
