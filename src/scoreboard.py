import pygame
import time


class Scoreboard():
    def __init__(self):
        self.height = 0
        self.font = pygame.font.SysFont("Arial", 30)
        self.start_time = time.time()
        self.total_time = 0
        self.x = 0
        self.y = 0
        self.color = (255, 255, 255)

    def update_score(self, height):
        self.height = height
        current_time = time.time()
        self.total_time = current_time - self.start_time

    def draw(self, screen):
        score_txt = self.font.render(
            f"Height: {self.height}  Time Elapsed: {int(self.total_time)}",
            True,
            self.color
        )
        screen.blit(score_txt, (self.x, self.y))
