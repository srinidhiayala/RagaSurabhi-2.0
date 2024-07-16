class Ragam:
    def __init__(self, name, aro, ava, aroAvaFile, signatureFile, carnaticFile, carnaticSong):
        self.name = name  
        self.aro=aro
        self.ava=ava
        self.aroAvaFile=aroAvaFile
        self.signatureFile = signatureFile
        self.carnaticFile = carnaticFile
        self.carnaticSong = carnaticSong
        
    def toString(self):
        return f"Name: {self.name}, Aro: {self.aro}, Ava: {self.ava } AAfile: {self.aroAvaFile} SigFile: {self.signatureFile} CarnaticFile: {self.carnaticFile} Song: {self.carnaticSong}" + "\n"


class Parent(Ragam):
    def __init__(self, name, aro, ava, aroAvaFile, signatureFile, carnaticFile, carnaticSong, melaNumber):
        super().__init__(name, aro, ava, aroAvaFile, signatureFile, carnaticFile ,carnaticSong)
        self.melaNumber = melaNumber
        
    def toString(self):
            return f"""
            Name: {self.name}
            Aro: {self.aro}
            Ava: {self.ava}
            AAfile: {self.aroAvaFile}
            SigFile: {self.signatureFile}
            CarnaticFile: {self.carnaticFile}
            Song: {self.carnaticSong}
            Mela: {self.melaNumber}
            """

class Child(Ragam):
    def __init__(self, name, aro, ava, aroAvaFile, signatureFile, carnaticFile, carnaticSong, parent, melaNumber):
        super().__init__(name, aro, ava, aroAvaFile,signatureFile, carnaticFile, carnaticSong)  
        self.parent = parent
        self.melaNumber = melaNumber
        
    def toString(self):
                return f"""
                Name: {self.name}
                Aro: {self.aro}
                Ava: {self.ava}
                AAfile: {self.aroAvaFile}
                SigFile: {self.signatureFile}
                CarnaticFile: {self.carnaticFile}
                Song: {self.carnaticSong}
                Parent: {self.parent}
                Mela: {self.melaNumber}
                """