import pygame
from sprites import Ball, Paddle
from constants import Config


def main():
    pygame.init()
    window = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    player_1 = Paddle(window, 1)
    player_2 = Paddle(window, 2)
    ball = Ball(window)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player_1.keydown_handler()
        player_2.keydown_handler()
        ball.move(player_1, player_2)

        window.fill((0, 0, 0))
        player_1.draw()
        player_2.draw()
        ball.draw()
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
