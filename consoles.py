import pdb

from models.animal import Animal
from models.owner import Owner

import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository


owner1 = Owner("Bob")
owner2 = Owner("Sue")
owner3 = Owner("Jim")

owner_repository.save(owner1)
owner_repository.save(owner2)
owner_repository.save(owner3)

animal = Animal("Rover", "Dog", owner1)
animal1 = Animal("Tom", "Cat", owner2)
animal2 = Animal("Harry", "Mouse", owner3)
animal_repository.save(animal)
animal_repository.save(animal1)
animal_repository.save(animal2)



# res = animal_repository.select_all()
# for pets in res:
#     print(pets.__dict__)

# animal_repository.delete(1)

# res = animal_repository.select_all()
# for pets in res:
#     print(pets.__dict__)
