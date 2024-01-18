import pygame
import sys
import time
import random
from game.snake import Snake
from game.coin import Coin
from utils.drawing import draw_snake
from pygame.locals import *
from pygame import mixer

pygame.init()
song_1 = 'music\You Make My Life 1UP - かめりあ feat. ななひら - Copy.mp3'
song_2 = 'music\ゲーミング☆Everything - かめりあ feat. ななひら.mp3'
bgsong = random.choice([song_1,song_2])
mixer.init()
mixer.music.load(bgsong)
mixer.music.play()

# Set up the screen
width, height = 600, 600
frame_width, frame_height = 600, 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Mario Game")

# Set up colors
background_color = (255, 255, 255)
top_background_color = (0, 126, 167)  # Different color for the top part
white = (255, 255, 255)
black = (0, 0, 0)
snake_color = (11, 19, 43)
coin_color = (169, 222, 249)

# Set up the font
font = pygame.font.Font(None, 36)  # You can choose the font and size

# Set up the clock
clock = pygame.time.Clock()

# Create instances of Snake and Coin
snake = Snake(20, 8, frame_width, frame_height)
coin = Coin(20, frame_width, frame_height)
# counting time
start_time = time.time()
count_time = 0.0
# Run the game loop
running = True
while running:
    # Assuming snake.score is the score you want to display
    score_text = font.render("Score: %d" % snake.score, True, (0, 0, 0))  # (0, 0, 0) is black

    # Calculate elapsed time
    elapsed_time = time.time() - start_time
    count_time = round(elapsed_time, 2)

    # timer:
    counter_text = font.render("Time  : %.2fs." % count_time, True, black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake.direction != "RIGHT":
        snake.direction = "LEFT"
    elif keys[pygame.K_RIGHT] and snake.direction != "LEFT":
        snake.direction = "RIGHT"
    elif keys[pygame.K_UP] and snake.direction != "DOWN":
        snake.direction = "UP"
    elif keys[pygame.K_DOWN] and snake.direction != "UP":
        snake.direction = "DOWN"

    # Check for collisions with the coin
    if (
        snake.body[0][0] < coin.position[0] + snake.size
        and snake.body[0][0] + snake.size > coin.position[0]
        and snake.body[0][1] < coin.position[1] + snake.size
        and snake.body[0][1] + snake.size > coin.position[1]
    ):
        # Snake eats the coin
        snake.grow()
        snake.update_score()
        snake.save_score()  # Save the score to a JSON file
        coin = Coin(20, frame_width, frame_height)  # Update coin position after eating

    # Move the body of the snake
    for i in range(len(snake.body) - 1, 0, -1):
        snake.body[i][0] = snake.body[i - 1][0]
        snake.body[i][1] = snake.body[i - 1][1]

    # Move the snake (teleportation logic)
    snake.move()

    # Fill the screen with the background color
    screen.fill(background_color)

    # Draw different background color for the top part
    top_rect = pygame.Rect(0, 0, width, frame_height)
    pygame.draw.rect(screen, top_background_color, top_rect)

    # Draw the snake on the screen
    draw_snake(screen, snake.body, snake.size, snake_color)

    # Draw the coin on the screen
    pygame.draw.rect(screen, coin_color, (coin.position[0], coin.position[1], 20, 20))

    # Draw the score on the screen
    screen.blit(score_text, (0, 500))
    screen.blit(counter_text, (0, 550))

    # Update the screen
    pygame.display.update()

    # Cap the frame rate
    clock.tick(snake.speed)

# Quit Pygame
pygame.quit()
sys.exit()
