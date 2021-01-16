import pygame 
import math
import random
import numpy as np
GRAVITY = 0.001

class Particle:
    ''' This is a representation of a particle in space

    === Attributes ===
    - x: the x position of the particle 
    - y: the y position of the particle 
    - coords: the coordinates of the particle on the screen
    - size: the radius of the particle 
    - color: the color of the particle 
    - mass: the mass of the particle, we use this to also determine the sizes
            of the particle for the pygame window
    - velocity: the velocity of the partilce, starts off with [0,0] and then 
                addys the velocity to <x> <y>
    - dv: the change in velocity
    - thickness: used by pygame to determine how thick the stroke of the drawn 
                  circle should be

    x: int 
    y: int 
    coords: numpy array
    size: [int, float]
    color: tuple(int,int,int) 
    mass: int 
    velocity: numpy array
    rot: float
    dv: numpy array
    thickness: int
    '''

    def __init__(self, x: int ,y: int, mass:float) -> None:
        ''' the constructor for the particle class'''
        
        self.x = x
        self.y = y
        self.coords = np.array([self.x,self.y], dtype= float)
        self.velocity = np.array([0,0], dtype=float)
        self.mass = mass
        self.size = (self.mass/math.pi)**(1/2)
        self.FG = 0
        self.color = [255,255,255]
        self.thickness = 100
        
    def display(self, screen: pygame.display) -> None:
        ''' this function draws the particle onto a paygame window'''
        pygame.draw.circle(screen, self.color, self.coords, self.size, self.thickness)


    def gravitaional_force(self, other):

        if self == other:
            self.dv = np.array([0,0], dtype = float)
        else:
            dist = math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
            if dist == 0:
                self.dv = 0 #acceleration is zero if the distance between the two objects is 0
            else:
                self.FG = (-GRAVITY*(self.mass*other.mass)/dist**2) * ((self.coords-other.coords)/dist)
                self.dv = self.FG / self.mass #Fnet = ma therfore a = Fnet/m
                # to preserve the quality of inelastic collisions we change <self.dv> to reverse if it 
                # becomes too close to another particle
                if dist < self.size  + other.size: 
                    self.dv *= -0.5
    
        self.velocity += self.dv #add the force vector to the velocity 
        self._displace(self.velocity)

    def _displace(self, vec:tuple) -> None:
        '''moves the particle by <vec> distance'''
        self.x += vec[0]
        self.y += vec[1]   
        self.coords = np.array([self.x, self.y], dtype= float) 
    
    def check_bounds(self, screen:list) -> None:
        ''' this function flips the direction of this particle'''
        if 0 < self.x < screen[0] and 0 < self.y < screen[1] :
            pass 
        else:
            self.velocity *= -0.5
            self._displace(self.velocity)
