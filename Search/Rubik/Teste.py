from Search import *


c = Cube()
print(c.sides)
c.L()
c.R()
c.D()
c.U()
c.U()
c.L()
c.B()
c.L()
c.R()
c.U()


#state_test = {'Green': {1: 'G', 2: 'G', 3: 'R', 4: 'G', 5: 'G', 6: 'R', 7: 'B', 8: 'W', 9: 'O'},\
              #'Red': {1: 'R', 2: 'R', 3: 'R', 4: 'R', 5: 'R', 6: 'B', 7: 'B', 8: 'B', 9: 'W'},\
              #'White': {1: 'Y', 2: 'G', 3: 'B', 4: 'W', 5: 'W', 6: 'W', 7: 'B', 8: 'W', 9: 'G'},\
              #'Orange': {1: 'Y', 2: 'B', 3: 'W', 4: 'R', 5: 'O', 6: 'O', 7: 'Y', 8: 'O', 9: 'G'},\
              #'Blue': {1: 'R', 2: 'O', 3: 'O', 4: 'Y', 5: 'B', 6: 'Y', 7: 'W', 8: 'Y', 9: 'W'},\
              #'Yellow': {1: 'O', 2: 'G', 3: 'O', 4: 'Y', 5: 'Y', 6: 'B', 7: 'Y', 8: 'O', 9: 'G'}}

#c.sides = state_test

print(c)

#print(searchDFS(c))
print(searchAs(c))





