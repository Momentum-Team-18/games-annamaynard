class Traveler: 
    def __init__(self, name, dob, address, email):
        self.name = name
        self.dob = dob 
        self.address = address
        self.email = email
    def __str__(self):
        return self.name

class Trip: 
    def __init__(self, destination, mode, lenght):
        self.destination = destination
        self.mode = mode
        self.length = lenght
        self.travelers = [] 

    def register (self,traveler):
        self.travelers.append(traveler)
    
    def __str__(self):
        return f'{self.destination} by {self.mode}'


matt = Traveler('Matt', '3-18-93', 'moon', 'matt@matt.com')
mars = Trip('Mars', 'rocket', '6 mo')
mars.register(matt)
print(mars)
for traveler in mars.travelers: 
    print(traveler)
        