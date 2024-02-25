class PartyAnimal:
    
    def party(self):
        try:
            self.x = self.x + 1
        except AttributeError:
            self.x = 1
        print('Parties bisher:', self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)
print(an.__sizeof__())