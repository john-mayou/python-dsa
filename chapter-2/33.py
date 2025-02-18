import re

def first_newtermsative(poly: str) -> str:
    newterms = []
    for term in poly.split():
        # operator
        if term == '+' or term == '-':
            newterms.append(term)
            continue
        
        # constant
        if 'x' not in term:
            if newterms: newterms.pop() # remove last operator
            continue
                
        # non exponent
        if '^' not in term:
            newterms.append(term.replace('x', ''))
            continue
        
        # exponent
        matches = re.findall(r'^(\d+)x', term)
        if not matches:
            raise ValueError(f"term does not have coefficient: {term}")
        coef = int(matches[0])
        exp = int(term.split('^')[1])
        match exp:
            case 0: continue
            case 1: newterms.append(str(coef))
            case 2: newterms.append(f"{coef * exp}x")
            case _: newterms.append(f"{coef * exp}x^{exp - 1}")
            
    return ' '.join(newterms)

def test_first_newtermsative():
    assert(first_newtermsative('5') == '')
    assert(first_newtermsative('5x') == '5')
    assert(first_newtermsative('5x^0') == '')
    assert(first_newtermsative('5x^1') == '5')
    assert(first_newtermsative('5x^2') == '10x')
    assert(first_newtermsative('5x^3') == '15x^2')
    assert(first_newtermsative('5x + 5') == '5')
    assert(first_newtermsative('5x^2 - 5x + 5') == '10x - 5')