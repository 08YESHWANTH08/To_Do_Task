import numpy as np
a1=input("Enter The Array(separated by \' \'):").split() #Example a1= 1 2 3 4 5
a1=np.array(list(map(int,a1)))
a2=input("Enter The Array(separated by \' \'):").split() #Example a2= 1 2 3 4 5
a2=np.array(list(map(int,a2)))
comparison = (a1 == a2)
Condition= comparison.all()
if(Condition is True):
    print(True)
else:
    print(False)