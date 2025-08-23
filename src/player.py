import pygame


def check_collision(self, block):
    return (
        ((self.y + self.height) > block.rect.y and
         self.y < (block.rect.y + block.rect.height)) and
        (self.x < (block.rect.x + block.rect.width) and
         (self.x + self.width) > block.rect.x)
    )


class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.width = 20
        self.height = 20

        self.yvel = 0
        self.speed = 0.4
        self.jump_vel = 0.8
        self.fall = 0.002

        self.pushback = 0.1
        self.jumps = 0

        self.image = pygame.Rect(self.x, self.y, self.width, self.height)

    def left(self, all_blocks):
        self.x -= self.speed
        for block in all_blocks:
            if check_collision(self, block):
                while self.x < (block.rect.x + block.rect.width):
                    self.x += self.pushback
        self.image = pygame.Rect(self.x, self.y, self.width, self.height)

    def right(self, all_blocks):
        self.x += self.speed
        for block in all_blocks:
            if check_collision(self, block):
                while (self.x + self.width) > block.rect.x:
                    self.x -= self.pushback
        self.image = pygame.Rect(self.x, self.y, self.width, self.height)

    def jump(self):
        if self.jumps > 0:
            self.yvel = -self.jump_vel
            self.jumps -= 1

    def gravity(self, all_blocks):
        self.y += self.yvel
        self.yvel += self.fall
        for block in all_blocks:
            if check_collision(self, block):
                if self.yvel < 0:  # if the player is under the block
                    self.yvel = 0
                    while self.y < (block.rect.y + block.rect.height):  # while the player's head is still in the block
                        self.y += self.pushback
                else:  # if the player is above the block
                    self.yvel = 0
                    self.jumps = 2
                    while (
                        self.y + self.height
                    ) > block.rect.y:  # while the player's bottom is still in the block
                        self.y -= self.pushback
        self.image = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.image)


    
        