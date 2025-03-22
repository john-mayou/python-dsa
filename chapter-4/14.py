from enum import Enum

type Step = tuple[Peg, Peg, Disk] # from, to, disk
type Disk = int
class Peg(Enum):
    A = 1
    B = 2
    C = 3

def hanoi(n: int):
    """
    This solution only works for n = 1 and n = 2.
    
    Time: ?
    Space: ?
    Recursive Depth: ?
    """
    solution: list[Step] = None
    
    def hanoi_solver(pegs: dict[Peg, list[Disk]], curr_steps: list[Step] = []):
        nonlocal solution
        if solution and len(curr_steps) >= len(solution):
            return
        
        for peg in pegs.keys():
            if len(pegs[peg]) == 0: continue
            top_disk = pegs[peg][-1]
            for other_peg in pegs.keys():
                if other_peg == peg: continue
                if len(curr_steps) > 0 and curr_steps[-1] == (other_peg, peg, top_disk): continue
                if (len(pegs[other_peg]) > 0 and pegs[other_peg][-1] < top_disk): continue
                
                pegs[peg].pop()
                pegs[other_peg].append(top_disk)
                curr_steps.append((peg, other_peg, top_disk))
                
                if len(pegs[Peg.C]) == n:
                    solution = curr_steps.copy()
                else:
                    hanoi_solver(pegs, curr_steps)

                pegs[peg].append(top_disk)
                pegs[other_peg].pop()
                curr_steps.pop()
    
    pegs = {
        Peg.A: list(range(n, 0, -1)),
        Peg.B: [],
        Peg.C: []
    }
    hanoi_solver(pegs)
    
    return solution