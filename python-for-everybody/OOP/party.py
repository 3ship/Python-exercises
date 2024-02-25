class PartyAnimal:
    
    def __init__(self, nam):
        self.x = 0
        self.name = nam
    
    def party(self):
        self.x = self.x + 1
        print(self.name, 'hat', self.x, 'Party(s) besucht')