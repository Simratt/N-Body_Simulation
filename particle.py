import pygame 

class Particle:
    ''' This is a representation of a particle in space

    === Attributes ===
    - _x: the x position of the particle 
    - _y: the y position of the particle 
    - coords: the coordinates of the particle on the screen
    - size: the radius of the particle 
    - color: the color of the particle 
    - thickness: the thickness of the particle, this is for the pygame window

    === Representaion Invariants === 
    #TODO 

    _x: int 
    _y: int 
    coords: tuple(int, int)
    size: [int, float]
    color: tuple(int,int,int) 
    thickness: int 
    '''

    def __init__(self, x: int ,y: int, size: int) -> None:
        ''' the constructor for the particle class'''
        
        self._x = x
        self._y = y
        self.coords = (self._x, self._y) 
        self.size = size
        self.color = (255,255,255)
        self.thickness = 1

    def display(self, screen: pygame.display) -> None:
        ''' this function draws the particle onto a paygame window'''
        
        pygame.draw.circle(screen, self.color, self.coords, self.size, self.thickness)

