import pygame
from player import Player
from block_group import BlockGroup
from scoreboard import Scoreboard

class Platformer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((1000, 800))
        self.player = Player()
        self.blocks = BlockGroup()
        self.blocks.create(10)
        self.all_blocks = (self.blocks.all_blocks)
        self.scoreboard = Scoreboard()
        self.camera_x = 0
        self.camera_y = 0

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player.jump()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.player.left(self.all_blocks)
            if keys[pygame.K_d]:
                self.player.right(self.all_blocks)

            self.player.gravity(self.all_blocks)

            self.screen.fill((0, 0, 0))

            self.player.draw(self.screen)

            self.all_blocks.draw(self.screen)

            self.scoreboard.update_score(750 - self.player.y)

            self.scoreboard.draw(self.screen)

            pygame.display.flip()