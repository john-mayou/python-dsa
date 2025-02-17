from typing import Sequence

class ReversedSequenceIterator:
    def __init__(self, sequence: Sequence):
        self._seq = sequence
        self._i = 0
        
    def __next__(self):
        self._i -= 1
        if abs(self._i) <= len(self._seq):
            return self._seq[self._i]
        raise StopIteration()
    
    def __iter__(self):
        return self
    
def test_reversed_sequence_iterator():
    assert([val for val in ReversedSequenceIterator([1, 2, 3])] == [3, 2, 1])