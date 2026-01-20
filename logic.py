
from DataProvider import DataProvider
from PMStorage import PMStorage
from PygameRender import PygameRender
from PymunkSimulation import PymunkSimulation


class Logic:
    def __init__(self):
      self.pmStorage = PMStorage(DataProvider().load_pm_objects())


    def load(self):
      self.pmStorage.reset(DataProvider().load_pm_objects())

    def save(self, pgParameters):
        DataProvider().save(self.pmStorage.listOjects, pgParameters)


    def run_pygame(self, pgParameters):
        pymunk = PymunkSimulation(pgParameters, self.pmStorage.listOjects)
        pygameRender = PygameRender()
        pygameRender.run(pgParameters,pymunk)

#runPGame(600,800,120,1200,0.8)
logic = Logic()