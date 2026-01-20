import ColorUtils

class PMObject:
    def __init__(self,id,x,y,fx,fy, color):
        self.id = id
        self.x = x
        self.y = y
        self.fx = fx
        self.fy = fy
        self.color = color

class PMStorage:
    def __init__(self, pm_objects=None):
        if pm_objects is None:
           self.listOjects = []
        else:
            self.listOjects = pm_objects

    def reset(self, pm_objects=None):
        if pm_objects is None:
           self.listOjects = []
        else:
            self.listOjects = pm_objects

    def add_pm_oject(self,pmObject):
        self.listOjects.append(pmObject)

    def delete_pm_oject(self, id):
        found = None
        for elem in self.listOjects:
            if elem.id == id:
                found = elem
                break
        self.listOjects.remove(found)


