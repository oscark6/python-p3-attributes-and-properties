class Dog:
    approved_breeds = [ 
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name="Default Name", breed="Corgi"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = None

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in Dog.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = None

# Example usage:
dog1 = Dog("Buddy", "Beagle")
print(dog1.name)  
print(dog1.breed)  

dog2 = Dog("", "Corgi")  
print(dog2.name)  
print(dog2.breed)  

dog3 = Dog("Fido", "Wolf")  
print(dog3.name)  
print(dog3.breed) 

dog4 = Dog(123, "Pug")  
print(dog4.name)  
print(dog4.breed)  