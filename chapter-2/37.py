import random

class Animal:
    def __init__(self):
        self.gender = 'male' if random.random() < 0.5 else 'female'
        self.strength = random.randint(0, 100)

class Bear(Animal):
    pass

class Fish(Animal):
    pass

RIVER_SIZE = 100
RIVER_MOVE_PROB = 0.2

def main():
    river = [None] * RIVER_SIZE
    for _ in range(20): river[random.randint(0, RIVER_SIZE - 1)] = Bear()
    for _ in range(20): river[random.randint(0, RIVER_SIZE - 1)] = Fish()
    empty_idxs = set([i for i in range(len(river)) if river[i] == None])
    while empty_idxs:
        for i in range(RIVER_SIZE):
            animal = river[i]
            if animal == None: continue
            if random.random() < RIVER_MOVE_PROB:
                newi = random.choice([n for n in range(0, RIVER_SIZE - 1) if n != i])
                newianimal = river[newi]
                if newianimal == None:
                    river[i] = None
                    empty_idxs.add(i)
                    river[newi] = animal
                    if newi in empty_idxs:
                        empty_idxs.remove(newi)
                elif type(animal) == type(newianimal):
                    if animal.gender == newianimal.gender: # fight it out
                        river[i] = None
                        empty_idxs.add(i)
                        river[newi] = animal if animal.strength > newianimal.strength else newianimal
                    else: # create new animal
                        emptyi = random.choice(list(empty_idxs))
                        river[emptyi] = Bear() if isinstance(animal, Bear) else Fish()
                        empty_idxs.remove(emptyi)
                elif isinstance(newianimal, Bear): # bear stays
                    river[i] = None
                    empty_idxs.add(i)
                elif isinstance(newianimal, Fish): # bear eats fish
                    river[i] = None
                    empty_idxs.add(i)
                    river[newi] = animal
                else:
                    raise RuntimeError(f"Could not determine action to perform for index {i}")
            if not empty_idxs: break
    
    bear_count = 0
    fish_count = 0
    for animal in river:
        if isinstance(animal, Bear): bear_count += 1
        elif isinstance(animal, Fish): fish_count += 1
        else: raise RuntimeError(f"Invalid animal in river: {animal}")
        
    print(f"Bear: {bear_count}")
    print(f"Fish: {fish_count}")

if __name__ == "__main__": main()