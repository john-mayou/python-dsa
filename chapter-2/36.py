import random

class Bear:
    pass

class Fish:
    pass

RIVER_SIZE = 100
RIVER_MOVE_PROB = 0.2

def main():
    river = [None] * RIVER_SIZE
    for _ in range(10): river[random.randint(0, RIVER_SIZE - 1)] = Bear()
    for _ in range(20): river[random.randint(0, RIVER_SIZE - 1)] = Fish()
    print(river)
    empty_idxs = set([i for i in range(len(river)) if river[i] == None])
    iterations = 0
    while empty_idxs:
        iterations += 1
        print(f'new loop iteration with: {empty_idxs}')
        for i in range(RIVER_SIZE):
            animal = river[i]
            if animal == None: continue
            if random.random() < RIVER_MOVE_PROB:
                print('moving....')
                newi = random.randint(0, RIVER_SIZE - 1)
                newianimal = river[newi]
                if newianimal == None:
                    print('new spot is none, moving')
                    river[i] = None
                    empty_idxs.add(i)
                    river[newi] = animal
                    if newi in empty_idxs:
                        empty_idxs.remove(newi)
                elif type(animal) == type(newianimal):
                    print('new spot is the same animal, creating a new animal')
                    emptyi = random.choice(list(empty_idxs))
                    river[emptyi] = Bear() if isinstance(animal, Bear) else Fish() # create new animal
                    empty_idxs.remove(emptyi)
                elif isinstance(newianimal, Bear): # bear stays
                    print('new spot is a bear, leaving bear and removing fish')
                    river[i] = None
                    empty_idxs.add(i)
                elif isinstance(newianimal, Fish): # bear eats fish
                    print('new spot is a fish, moving to override with bear')
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