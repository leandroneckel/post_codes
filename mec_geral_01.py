import sympy as sp
import numpy as np
tab, tac, tad = sp.symbols('tab tac tad')
P = np.array([0,-1600,0])
AB = np.array([-36,60,-27])
TAB = tab * AB / np.linalg.norm(AB)
AC = np.array([0,60,32])
TAC = tac * AC / np.linalg.norm(AC)
AD = np.array([40,60,-27])
TAD = tad * AD / np.linalg.norm(AD)
eq1 = sp.Eq(P[0]+TAB[0]+TAC[0]+TAD[0],0)
eq2 = sp.Eq(P[1]+TAB[1]+TAC[1]+TAD[1],0)
eq3 = sp.Eq(P[2]+TAB[2]+TAC[2]+TAD[2],0)
display(eq1)
display(eq2)
display(eq3)
sol = sp.solve( (eq1,eq2,eq3) , (tab,tac,tad) )
print(sol)
