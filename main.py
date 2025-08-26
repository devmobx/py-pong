import pygame
from sprites import Paddle, Ball, Score
from constants import Config


def initPyPong():
    pygame.init()
    window = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    player_1 = Paddle(window, 1)
    player_2 = Paddle(window, 2)
    ball = Ball(window, player_1, player_2)
    score = Score(window, player_1, player_2, ball)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill((0, 0, 0))

        for sprite in [player_1, player_2, ball, score]:
            sprite.handler()
            sprite.draw()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    initPyPong()
