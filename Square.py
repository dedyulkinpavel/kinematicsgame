import time

import pygame
import pymunk.pygame_util
from pygame import Color


class Square:
    def __init__(self,  color, elasticity=0.5, friction=0.8, mass=1, size=50):
        self.elasticity = elasticity
        self.friction = friction
        self.mass = mass
        self.size = size
        self.stopped = False
        self.color = color

    def create_square(self, pos, space):
        body = pymunk.Body(self.mass, pymunk.moment_for_box(self.mass, (self.size, self.size)))
        body.position = pos
        shape = pymunk.Poly.create_box(body, (self.size, self.size))
        shape.friction = self.friction
        shape.elasticity = self.elasticity
        space.add(body, shape)
        self.body = body
        self.shape = shape

        return body, shape

    def apply_force(self, body, force_x, force_y):
        self.force_x = force_x
        self.force_y = force_y
        #body.apply_force_at_world_point((force_x, force_y), body.position)

    def step_it(self):
        self.body.apply_force_at_world_point((self.force_x, self.force_y), self.body.position)
        self.shape.color = self.color
