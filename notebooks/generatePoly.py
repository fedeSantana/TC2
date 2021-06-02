import sympy as sp

def generatePoly (n):
    
    symbols = []
    for i in range(n+1):
      symbols.append(sp.symbols(f"a_{i}", positive = True, real = True))
    
    s = sp.symbols('s')
    result = sp.poly(0, s)
    for x in range(n+1):
        result = result.add(sp.poly(symbols[x]*s**x,s))
    return result, symbols