import pygame
import random

pygame.init()

# Screen width and height
WIDTH = 900
HEIGHT = 500

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
pygame.display.update()


clock = pygame.time.Clock()
FPS = 30
# 55 is size and None is for default system font
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


# For plotting snake
def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233, 210, 229))
        text_screen("Welcome to Snakes", BLACK, 260, 250)
        text_screen("Press Space Bar To Play", BLACK, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(FPS)


def gameloop():
    # Game specific variables
    score = 0
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 45
    snake_size = 50
    food_x = random.randint(0, WIDTH)
    food_y = random.randint(0, HEIGHT)
    velocity_x = 5
    velocity_y = 0
    init_velocity = 5
    snk_length = 1
    snk_list = []
    step_up_allow = False
    step_down_allow = True

    # Game Loop
    while not exit_game:
        if game_over:
            gameWindow.fill(WHITE)
            text_screen("Game Over! Press Enter to Continue",
                        RED, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        step_allow = True
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        step_allow = False
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:

                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            # Calcualting if snake is very close to food or not
            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                food_y = random.randint(20, WIDTH/2)
                food_x = random.randint(20, HEIGHT/2)
                score += 10
                snk_length += 5

            gameWindow.fill(WHITE)
            # Displaying score on screen
            text_screen("Score: " + str(score), RED, 5, 5)
            # pygame.draw.rect(gameWindow, BLACK, [
            #     snake_x, snake_y, snake_size, snake_size])
            pygame.draw.rect(gameWindow, RED, [
                food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > WIDTH or snake_y < 0 or snake_y > WIDTH:
                game_over = True
            plot_snake(gameWindow, BLACK, snk_list, snake_size)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


if __name__ == '__main__':
    welcome()
