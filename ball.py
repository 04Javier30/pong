import pygame
from random import randint

black = (0,0,0)

val1 = randint(4,8)
val2 = randint(-8,8)

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        
        pygame.draw.rect(self.image, color, [0,0,width,height])
        
        self.velocity = [val1 , val2]
        
        print(self.velocity)
        
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def bouncing(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = self.velocity[1]