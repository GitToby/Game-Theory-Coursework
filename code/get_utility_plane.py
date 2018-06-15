def get_utility_plane(x,y,M):
    '''Generates the utility plane using sympy and labdafy evaluation'''
    a, b = sym.symbols('a, b')
    A = sym.Matrix(M)
    # Define mixed strategies 
    sigma_r, sigma_c = sym.Matrix([[a, 1-a]]), sym.Matrix([b, 1-b])
    # Use sympy to evaluate and lambdafy
    result = (sigma_r * A *  sigma_c)[0]
    return sym.lambdify((a,b), result)(x,y)