import pygame
import random

pygame.init()

# PART 1: SETTINGS

GAME_TITLE = "Juan's Snake"
CELL_SIZE = 25
GRID_WIDTH = 24
GRID_HEIGHT = 18
SPEED = 8
START_LENGTH = 3
POINTS_PER_FOOD = 10
WALLS_KILL = True

SNAKE_COLOR = (90, 200, 120)
BG_COLOR = (25, 25, 25)

WIDTH = GRID_WIDTH * CELL_SIZE
HEIGHT = GRID_HEIGHT * CELL_SIZE


# PART 2: SETUP

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_TITLE)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

# PART 3: FUNCTIONS

def place_food(snake):
    while True:
        food = (random.randint(0, GRID_WIDTH - 1),
                random.randint(0, GRID_HEIGHT - 1))

        if food not in snake:
            food_type = random.choice(
                ["normal", "speed", "multiplier", "confusion"]
            )
            return food, food_type


def new_game():
    snake = []
    start_x = GRID_WIDTH // 2
    start_y = GRID_HEIGHT // 2

    for i in range(START_LENGTH):
        snake.append((start_x - i, start_y))

    direction = (1, 0)
    food, food_type = place_food(snake)

    return snake, direction, food, food_type


def draw_game(snake, food, food_type, score, best_score,
              level, apples_eaten, next_multiplier,
              current_time, rgb_end_time, game_over):

    screen.fill(BG_COLOR)

    # Draw food
    if food_type == "normal":
        food_color = (255, 0, 0)
    elif food_type == "speed":
        food_color = (255, 215, 0)
    elif food_type == "multiplier":
        food_color = (180, 0, 255)
    else:
        food_color = (0, 150, 255)

    food_center = (food[0] * CELL_SIZE + CELL_SIZE // 2,
                   food[1] * CELL_SIZE + CELL_SIZE // 2)

    pygame.draw.circle(screen, food_color, food_center, CELL_SIZE // 2)

    # Draw snake
    rgb_colors = [
        (255, 0, 0), (255, 127, 0), (255, 255, 0),
        (0, 255, 0), (0, 0, 255), (148, 0, 211)
    ]

    for i in range(len(snake)):
        color = SNAKE_COLOR

        if current_time < rgb_end_time:
            color = rgb_colors[(current_time // 100 + i) % 6]

        rect = pygame.Rect(
            snake[i][0] * CELL_SIZE,
            snake[i][1] * CELL_SIZE,
            CELL_SIZE - 2,
            CELL_SIZE - 2
        )

        pygame.draw.rect(screen, color, rect)

    # Display information
    level_multiplier = 1 + (level - 1) * 0.2

    texts = [
        ("Score: " + str(score), 5, 5),
        ("Best: " + str(best_score), 120, 5),
        ("Level: " + str(level), 240, 5),
        ("Multiplier: " + str(round(level_multiplier, 1)) + "x", 5, 30),
        ("Next Apple: " + str(next_multiplier) + "x", 190, 30)
    ]

    if level < 10:
        texts.append(("Apples: " + str(apples_eaten % 10) + "/10", 350, 30))
    else:
        texts.append(("MAX LEVEL", 350, 30))

    for text, x, y in texts:
        image = font.render(text, True, (255, 255, 255))
        screen.blit(image, (x, y))

    if game_over:
        image = font.render("GAME OVER - R to Restart - Q to Quit",
                            True, (255, 255, 255))
        screen.blit(image, (WIDTH // 2 - 170, HEIGHT // 2))

    pygame.display.update()


# PART 4: GAME LOOP

snake, direction, food, food_type = new_game()

score = 0
best_score = 0
apples_eaten = 0
level = 1
next_multiplier = 1

game_over = False
running = True

last_move = pygame.time.get_ticks()

speed_end_time = 0
confusion_end_time = 0
rgb_end_time = 0

while running:

    current_time = pygame.time.get_ticks()

    # EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                running = False

            if game_over and event.key == pygame.K_r:
                snake, direction, food, food_type = new_game()

                score = 0
                apples_eaten = 0
                level = 1
                next_multiplier = 1

                speed_end_time = 0
                confusion_end_time = 0
                rgb_end_time = 0
                last_move = current_time
                game_over = False

            elif not game_over:

                if event.key in (pygame.K_UP, pygame.K_w):
                    if direction != (0, 1):
                        direction = (0, -1)

                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    if direction != (0, -1):
                        direction = (0, 1)

                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    if direction != (1, 0):
                        direction = (-1, 0)

                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    if direction != (-1, 0):
                        direction = (1, 0)

    # UPDATE
    current_speed = SPEED + apples_eaten

    if current_time < speed_end_time:
        current_speed = current_speed * 1.5

    move_delay = 1000 / current_speed

    if not game_over and current_time - last_move >= move_delay:

        last_move = current_time

        # Confusion apple effect
        if current_time < confusion_end_time:

            choices = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            opposite = (-direction[0], -direction[1])
            choices.remove(opposite)

            direction = random.choice(choices)

        new_head = (
            snake[0][0] + direction[0],
            snake[0][1] + direction[1]
        )

        # Wall collision
        if WALLS_KILL:
            if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH
                    or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
                game_over = True

        else:
            new_head = (
                new_head[0] % GRID_WIDTH,
                new_head[1] % GRID_HEIGHT
            )

        eating = new_head == food

        # Snake collision
        if not game_over:
            if eating:
                if new_head in snake:
                    game_over = True
            else:
                if new_head in snake[:-1]:
                    game_over = True

        if not game_over:

            snake.insert(0, new_head)

            if eating:

                # Calculate score
                level_multiplier = 1 + (level - 1) * 0.2
                points = POINTS_PER_FOOD * level_multiplier * next_multiplier

                score = score + int(points)
                next_multiplier = 1
                apples_eaten = apples_eaten + 1

                # Level up every 10 apples
                if apples_eaten % 10 == 0 and level < 10:
                    level = level + 1
                    rgb_end_time = current_time + 1500

                # Special apple effects
                if food_type == "speed":
                    speed_end_time = current_time + 5000

                elif food_type == "multiplier":
                    next_multiplier = random.randint(2, 5)

                elif food_type == "confusion":
                    confusion_end_time = current_time + 1500

                food, food_type = place_food(snake)

            else:
                snake.pop()

    # DRAW
    if score > best_score:
        best_score = score

    draw_game(
        snake, food, food_type, score, best_score,
        level, apples_eaten, next_multiplier,
        current_time, rgb_end_time, game_over
    )

    clock.tick(60)

pygame.quit()
