"""
Algorithm PuzzleSolve(k,S,U):
    Input: An integer k, sequence S, and set U
    Output: An enumeration of all k-length extensions to S using elements in U without repetitions
    
    for each e in U do
        Add e to the end of S
        Remove e from U {e is now being used}
        if k == 1 then
            Test whether S is a configuration that solves the puzzle
            if S solves the puzzle then
                return “Solution found: ” S
        else
            PuzzleSolve(k−1,S,U) {a recursive call}
        Remove e from the end of S
        Add e back to U
        
PuzzleSolve(3, [], {a, b, c, d})
- PuzzleSolve(2, [a], {b, c, d})
  - PuzzleSolve(1, [a, b], {c, d})
  - PuzzleSolve(1, [a, c], {b, d})
  - PuzzleSolve(1, [a, d], {b, c})
- PuzzleSolve(2, [b], {a, c, d})
  - PuzzleSolve(1, [b, a], {c, d})
  - PuzzleSolve(1, [b, c], {a, d})
  - PuzzleSolve(1, [b, d], {a, c})
- PuzzleSolve(2, [c], {a, b, d})
  - PuzzleSolve(1, [c, a], {b, d})
  - PuzzleSolve(1, [c, b], {a, d})
  - PuzzleSolve(1, [c, d], {a, b})
- PuzzleSolve(2, [d], {a, b, c})
  - PuzzleSolve(1, [d, a], {b, c})
  - PuzzleSolve(1, [d, b], {a, c})
  - PuzzleSolve(1, [d, c], {a, b})
"""