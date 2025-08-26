import pygame
from sprites.paddle import Paddle


class Ball:
    def __init__(self, window: pygame.Surface):
        self._window = window
        self.x = window.get_width() // 2
        self.y = window.get_height() // 2
        self.radius = 8
        self.color = (255, 0, 0)
        self.speed_x = 6
        self.speed_y = 3

    def move(self, player_1: Paddle, player_2: Paddle):
        self.x += self.speed_x
        self.y += self.speed_y

        if (
            self.x - self.radius < 0
            or self.x + self.radius > self._window.get_width()
            or (
                self.y + self.radius > player_1.get_y()
                and self.y - self.radius < (player_1.get_y() + player_1.get_height())
                and self.x - self.radius < player_1.get_x() + (player_1.get_width() / 2)
                and self.x + self.radius > player_1.get_x() - (player_1.get_width() / 2)
            )
            or (
                self.y + self.radius > player_2.get_y()
                and self.y - self.radius < (player_2.get_y() + player_2.get_height())
                and self.x + self.radius > player_2.get_x() + (player_2.get_width() / 2)
                and self.x - self.radius < player_2.get_x() + (player_2.get_width() / 2)
            )
        ):
            self.speed_x *= -1
        elif (
            self.y - self.radius < 0
            or self.y + self.radius > self._window.get_height()
            or (
                self.y + self.radius > player_1.get_y()
                and self.y - self.radius < (player_1.get_y() + player_1.get_height())
                and self.x - self.radius < player_1.get_x() + (player_1.get_width() / 2)
                and self.x + self.radius > player_1.get_x() - (player_1.get_width() / 2)
            )
            or (
                self.y + self.radius > player_2.get_y()
                and self.y - self.radius < (player_2.get_y() + player_2.get_height())
                and self.x + self.radius > player_2.get_x() + (player_2.get_width() / 2)
                and self.x - self.radius < player_2.get_x() + (player_2.get_width() / 2)
            )
        ):
            self.speed_y *= -1

    def draw(self):
        pygame.draw.circle(
            self._window, self.color, (int(self.x), int(self.y)), self.radius
        )
