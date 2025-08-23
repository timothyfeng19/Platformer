import pygame
import time
from src.player import Player


class Scoreboard:
    def __init__(self):
        self.height = 0
        self.font = pygame.font.SysFont("Arial", 30)
        self.start_time = time.time()
        self.total_time = 0
        self.player = Player()

    def update_score(self, height):
        self.height = height
        current_time = time.time()
        self.total_time = self.start_time - current_time

    def draw(self, screen):
        score_txt = self.font.render(
            f"Height: {self.height}", True, (255, 255, 255)
        )
        screen.blit(score_txt, (0, 0))
