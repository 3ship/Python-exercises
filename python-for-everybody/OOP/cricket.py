from party import PartyAnimal

class CricketFan(PartyAnimal):
    
    def __init__(self, nam):
        super().__init__(nam) # super() ruft die init der Basisklasse
                              # PartyAnimal auf. CricketFan erbt PartyAnimal
        self.points = 0
        
    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, 'hat', self.points, 'Punkte')

s = PartyAnimal('Sally')
s.party()
j = CricketFan('Jim')
j.six()