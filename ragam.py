class Ragam:
    def __init__(self, name, aro, ava, aroAvaFile, signatureFile, carnaticFile):
        self.name = name  
        self.aro=aro
        self.ava=ava
        self.aroAvaFile=aroAvaFile
        self.signatureFile = signatureFile
        self.carnaticFile = carnaticFile


class Parent(Ragam):
    def __init__(self, name, aro, ava, aroAvaFile, signatureFile, carnaticFile, melaNumber):
        super().__init__(name, aro, ava, aroAvaFile, signatureFile, carnaticFile)
        self.melaNumber = melaNumber

class Child(Ragam):
    def __init__(self, name, aro, ava, aroAvaFile, signatureFile, carnaticFile, parent, melaNumber):
        super().__init__(name, aro, ava, aroAvaFile,signatureFile, carnaticFile)  
        self.parent = parent
        self.melaNumber = melaNumber