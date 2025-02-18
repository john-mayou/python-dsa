class Range:
    def __init__(self, start, stop = None, step = 1):
        if step == 0:
            raise ValueError('step cannot be 0')
        
        if stop is None:
            start, stop = 0, start
            
        self._length = max(0, (stop - start + step - 1) // step)
        self._start = start
        self._stop = stop
        self._step = step
        
    def __len__(self):
        return self._length
    
    def __getitem__(self, k):
        if k < 0:
            k += len(self)
            
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        
        return self._start + k * self._step
    
    def __in__(self, k):
        if not self._start <= k < self._stop:
            return False
        return (k - self._start) % self._step == 0
            
    
def test_range_in():
    r = Range(11)
    assert(-1 not in r)
    assert(0 in r)
    assert(5 in r)
    assert(10 in r)
    assert(11 not in r)
    
    r = Range(0, 11, 2)
    assert(-1 not in r)
    assert(0 in r)
    assert(5 not in r)
    assert(10 in r)
    assert(11 not in r)