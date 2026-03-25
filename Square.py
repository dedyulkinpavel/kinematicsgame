import pymunk.pygame_util


class Square:
    def __init__(self, color, elasticity=10, friction=0.8, mass=1, size=50):
        self.elasticity = elasticity
        self.friction = friction
        self.mass = mass
        self.size = size
        self.stopped = False
        self.color = color

    def create_circle(self, pos, space):
        radius = self.size // 2
        body = pymunk.Body(self.mass, pymunk.moment_for_circle(self.mass, 0, radius))
        body.position = pos
        shape = pymunk.Circle(body, radius)
        shape.friction = self.friction
        shape.elasticity = self.elasticity
        space.add(body, shape)
        self.body = body
        self.shape = shape
        return body, shape

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

    def create_triangle(self, pos, space):
        height = self.size * (3 ** 0.5) / 2
        vertices = [
            (0, -height / 2),  # верхняя вершина
            (-self.size / 2, height / 2),  # левая нижняя
            (self.size / 2, height / 2)  # правая нижняя
        ]

        moment = pymunk.moment_for_poly(self.mass, vertices)
        body = pymunk.Body(self.mass, moment)
        body.position = pos
        shape = pymunk.Poly(body, vertices)
        shape.friction = self.friction
        shape.elasticity = self.elasticity
        space.add(body, shape)
        self.body = body
        self.shape = shape
        return body, shape

    def apply_force(self, body, force_x, force_y):
        self.force_x = force_x
        self.force_y = force_y

    def step_it(self):
        self.body.apply_force_at_world_point((self.force_x, self.force_y), self.body.position)
        speed = self.body.velocity.length
        self.shape.color = self.color
