class Ragam:
    def __init__(self, name, aro, ava, aroAvaFile):
        self.name = name  
        self.aro=aro
        self.ava=ava
        self.aroAvaFile=aroAvaFile


class Parent(Ragam):
    def __init__(self, name, aro, ava, aroAvaFile, melaNumber):
        super().__init__(name, aro, ava, aroAvaFile)
        self.melaNumber = melaNumber

class Child(Ragam):
    def __init__(self, name, aro, ava, aroAvaFile, parent, melaNumber):
        super().__init__(name, aro, ava, aroAvaFile)  
        self.parent = parent
        self.melaNumber = melaNumber