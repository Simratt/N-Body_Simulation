import sys, pygame, pygame_menu
from particle import *

# some preliminary functions 
def randomize(_range:tuple) -> tuple:
    ''' returns a random set of coordinates within <range>'''
    coords = (random.randint(0, _range[0]), random.randint(0,_range[1]))
    return coords


particles = []

background_color = (0,0,0)
(width, height) = (600, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('N Body Simulation')
screen.fill(background_color)

#creating the particles 

for i in range(7):
    coords = randomize((width, height))
    p = Particle(coords[0], coords[1], random.randint(10, 30))
    p.display(screen)
    particles.append(p)

p.display(screen)
pygame.display.flip() # this puts all the stuff on the screen 

running = True 
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(background_color)
    for p_i in particles:
        for p_f in particles:
            p_i.gravitaional_force(p_f)
            p_i.check_bounds([width, height])
            p_i.display(screen)
    pygame.display.flip()


