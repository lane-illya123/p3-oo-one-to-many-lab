class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self,name,pet_type,owner = None):
        self.name = name
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise ValueError("Invalid pet type.")
        self.owner = owner
        self.all.append(self)
        

class Owner:

    def __init__(self, name):
        self.name = name
        

    def pets(self):
      return [pet for pet in Pet.all]     
    
    def add_pet(self, pet):

        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise ValueError("Invalid pet type.")
        
    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets    