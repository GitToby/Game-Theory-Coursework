>>> # SUPPORT ENUMERATION IN NASHPY
>>> A = np.array([[2, 2, -6], [6, 6, -3]])
>>> B = np.array([[4, 2, 4], [6, -1, 6]])
>>> g = nash.Game(A, B)
>>> for pairs in g.support_enumeration():
...    print('sigma_r:', pairs[0], '\t sigma_c:', pairs[1])

sigma_r: [0. 1.] 	 sigma_c: [1. 0. 0.]
sigma_r: [0. 1.] 	 sigma_c: [0. 0. 1.]
