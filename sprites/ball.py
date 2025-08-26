import pygame
from constants import Config
from sprites.paddle import Paddle


class Ball:
    def __init__(self, window: pygame.Surface, player_1: Paddle, player_2: Paddle):
        self._window = window
        self._player_1 = player_1
        self._player_2 = player_2
        self.x = window.get_width() / 2
        self.y = window.get_height() / 2
        self.radius = 8
        self.color = Config.COLOR
        self.speed_x = 6
        self.speed_y = 3

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_radius(self):
        return self.radius

    def handler(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if (
            self.x - self.radius < 0
            or self.x + self.radius > self._window.get_width()
            or (
                self.y + self.radius > self._player_1.get_y()
                and self.y - self.radius
                < (self._player_1.get_y() + self._player_1.get_height())
                and self.x - self.radius
                < self._player_1.get_x() + (self._player_1.get_width() / 2)
                and self.x + self.radius
                > self._player_1.get_x() - (self._player_1.get_width() / 2)
            )
            or (
                self.y + self.radius > self._player_2.get_y()
                and self.y - self.radius
                < (self._player_2.get_y() + self._player_2.get_height())
                and self.x + self.radius
                > self._player_2.get_x() + (self._player_2.get_width() / 2)
                and self.x - self.radius
                < self._player_2.get_x() + (self._player_2.get_width() / 2)
            )
        ):
            self.speed_x *= -1
        elif (
            self.y - self.radius < 0
            or self.y + self.radius > self._window.get_height()
            or (
                self.y + self.radius > self._player_1.get_y()
                and self.y - self.radius
                < (self._player_1.get_y() + self._player_1.get_height())
                and self.x - self.radius
                < self._player_1.get_x() + (self._player_1.get_width() / 2)
                and self.x + self.radius
                > self._player_1.get_x() - (self._player_1.get_width() / 2)
            )
            or (
                self.y + self.radius > self._player_2.get_y()
                and self.y - self.radius
                < (self._player_2.get_y() + self._player_2.get_height())
                and self.x + self.radius
                > self._player_2.get_x() + (self._player_2.get_width() / 2)
                and self.x - self.radius
                < self._player_2.get_x() + (self._player_2.get_width() / 2)
            )
        ):
            self.speed_y *= -1

    def draw(self):
        pygame.draw.circle(
            self._window, self.color, (int(self.x), int(self.y)), self.radius
        )

    def reset(self):
        self.x = self._window.get_width() // 2
        self.y = self._window.get_height() // 2
