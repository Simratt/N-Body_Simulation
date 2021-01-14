import sys, pygame
from particle import Particle

background_color = (0,0,0)
(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Abhay is a samosa')
screen.fill(background_color)

p = Particle(150, 50, 15)
p.display(screen)

pygame.display.flip() # this puts all the stuff on the screen 

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False