import threading

import pygame as pg
import pymunk.pygame_util

from PymunkSimulation import PymunkSimulation

pymunk.pygame_util.positive_y_is_up = False



class PygameRender():
    def run(self, pgParameters, pymunksim=PymunkSimulation):
        self.witdh = pgParameters.w
        self.height = pgParameters.h
        self.fps = pgParameters.fps
        RES = self.witdh, self.height
        pg.init()
        self.surface = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.draw_options = pymunk.pygame_util.DrawOptions(self.surface)

        self.pymunkSim = pymunksim
        self.timer = threading.Timer(1 / self.fps, lambda: self.on_render_step())
        self.timer.start()



    def on_render_step(self):
       self.surface.fill(pg.Color('black'))
       for i in pg.event.get():
           if i.type == pg.QUIT:
               pg.quit()
               return
       self.pymunkSim.step()
       self.pymunkSim.space.debug_draw(self.draw_options)
       pg.display.flip()
       self.clock.tick(self.fps)
       self.timer = threading.Timer(1 / self.fps, lambda: self.on_render_step())
       self.timer.start()


