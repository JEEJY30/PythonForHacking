class samezoblo:

    def __init__(self,firstName,lastName,disabilities,hairColor,inteligenceLvl):
        self.firstName = firstName
        self.lasNname = lastName 
        self.disabilities = disabilities
        self.hairColor = hairColor
        self.inteligenceLvl = inteligenceLvl

    @property
    def about_neigbour(self):
        return f"Fullname is {self.firstName} {self.lasNname}, About disabilities {self.disabilities}, haircolor has {self.hairColor}, inteligenceLvl {self.inteligenceLvl}"



neigbour1 = samezoblo("Mariam","Sharvadze","None","Brown","110IQ min")
neigbour2 = samezoblo("Ana","Sharvadze","None","Brown","110IQ")
neigbour3 = samezoblo("Giorgi","Mamaci","ALL","Black","100IQ")
neigbour4 = samezoblo("Nino","Bebo","None","Brown","110IQ min")
neigbour5 = samezoblo("Nazi","Bebo","None","Black","110IQ")

print(neigbour1.about_neigbour())
