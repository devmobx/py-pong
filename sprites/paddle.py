import pygame
from typing import Literal
from constants import Config


PADDLE_X_OFFSET = 50
PADDLE_HEIGHT = 50
PADDLE_WIDTH = 10


class Paddle:
    def __init__(self, window: pygame.Surface, player: Literal[1, 2]):
        self._window = window
        self._player = player
        self.height = PADDLE_HEIGHT
        self.width = PADDLE_WIDTH
        self.speed = 8
        self.color = Config.COLOR
        self.x = (
            PADDLE_X_OFFSET
            if player == 1
            else window.get_width() - (PADDLE_X_OFFSET + (PADDLE_WIDTH / 2))
        )
        self.y = (window.get_height() / 2) - PADDLE_HEIGHT / 2

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def handler(self):
        keys = pygame.key.get_pressed()
        if (
            keys[pygame.K_UP] if self._player == 2 else keys[pygame.K_z]
        ) and self.y > 0:
            self.y -= self.speed
        elif (
            keys[pygame.K_DOWN] if self._player == 2 else keys[pygame.K_s]
        ) and self.y < self._window.get_height() - self.height:
            self.y += self.speed

    def draw(self):
        pygame.draw.rect(
            self._window,
            self.color,
            pygame.Rect(int(self.x), int(self.y), self.width, self.height),
        )

    def reset(self):
        self.x = (
            PADDLE_X_OFFSET
            if self._player == 1
            else self._window.get_width() - (PADDLE_X_OFFSET + (PADDLE_WIDTH / 2))
        )
        self.y = (self._window.get_height() / 2) - PADDLE_HEIGHT / 2
