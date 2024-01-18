import pygame

def draw_snake(screen, snake, size, color):
    for segment in snake:
        pygame.draw.rect(screen, color, (segment[0], segment[1], size, size))
