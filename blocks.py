import pygame
import random

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y