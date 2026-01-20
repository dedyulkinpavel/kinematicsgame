import pymunk.pygame_util
from Square import Square
from PGParameters import PGParameters
import ColorUtils

class PymunkSimulation():
    def __init__(self, pgParameters, pmObjects):
        self.space = pymunk.Space()
        self.fps = pgParameters.fps
        self.space.gravity = 0, pgParameters.g
        segment_shape = pymunk.Segment(self.space.static_body, (1, pgParameters.h), (pgParameters.w, pgParameters.h), 26)
        self.space.add(segment_shape)
        segment_shape.elasticity = 0.5
        segment_shape.friction = pgParameters.f
        self.pmObjects = []
        for elem in pmObjects:

            figure = Square(ColorUtils.int_to_rgb(elem.color))
            Square.create_square(figure, (elem.x, elem.y), self.space)
            figure.apply_force(figure.body, elem.fx, elem.fy)
            self.pmObjects.append(figure)

    def step(self):
        for elem in self.pmObjects:
            elem.step_it()

        self.space.step(1 / self.fps)

