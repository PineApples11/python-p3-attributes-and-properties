#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name="Hubo", breed="Pointer"):
        self.name = name
        self.breed = breed
    
    def get_name(self):
        print("Fetching Dog's name ...")
        return self._name
    
    def set_name(self,name):
        if type(name) == str and (1 <= len(name) <= 25):

            # print(f'Setting name to {name}.')
            # self._name = name.title()
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    name = property(get_name, set_name)

    def get_breed(self):
        print("Fetching Dog's breed")
        return self._breed
    
    def set_breed(self,breed):
        if breed in APPROVED_BREEDS:
            self._breed=breed
            # print(self._breed)
        else:
            print("Breed must be in list of approved breeds.")
            
    breed=property(get_breed,set_breed)

    pass

dog1 = Dog("")