import pygame
import random
from src.blocks import Block


class BlockGroup():
    def __init__(self):
        self.all_blocks = pygame.sprite.Group()

    def create(self, n):
        self.num_blocks = n
        bias = 1
        prev_x = 0
        for i in range(n):
            if random.randint(0, 8) == 0:
                bias = random.randint(0, 1) * 2 - 1
            b = Block(
                prev_x,
                -(i * (70) + random.randint(-10, 10)) + 800,
                random.randint(10, 150),
                random.randint(10, 100))
            prev_x += bias * random.randint(100, 300) + random.randint(-50, 50)
            self.all_blocks.add(b)
        b = Block(0, 750, 1000, 50)
        self.all_blocks.add(b)
