import pygame
from constants.config import Config
from sprites.ball import Ball
from sprites.paddle import Paddle

CENTER_OFFSET = 100
POS_Y = 20


class Score:
    def __init__(
        self, window: pygame.Surface, player_1: Paddle, player_2: Paddle, ball: Ball
    ):
        self._window = window
        self._player_1 = player_1
        self._player_2 = player_2
        self._ball = ball
        self.p1_score = 0
        self.p2_score = 0

    def _reset_sprites(self):
        for sprite in [self._player_1, self._player_2, self._ball]:
            sprite.reset()

    def handler(self):
        if self._ball.get_x() - self._ball.get_radius() < 0:
            self.p2_score += 1
            self._reset_sprites()
        elif self._ball.get_x() + self._ball.get_radius() > self._window.get_width():
            self.p1_score += 1
            self._reset_sprites()

    def draw(self):
        font = pygame.font.Font(None, 36)
        txt_p1 = font.render(f"{self.p1_score}", True, Config.COLOR)
        txt_p2 = font.render(f"{self.p2_score}", True, Config.COLOR)
        self._window.blit(
            txt_p1, ((self._window.get_width() / 2) - CENTER_OFFSET, POS_Y)
        )
        self._window.blit(
            txt_p2, ((self._window.get_width() / 2) + CENTER_OFFSET, POS_Y)
        )

    def reset(self):
        self.p1_score = 0
        self.p2_score = 0
