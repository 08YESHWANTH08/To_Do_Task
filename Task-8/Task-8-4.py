import pandas as pd
import numpy as np
result=''
statement=input("Enter The Array (Separated By \' \'):").split()
statement=np.array(statement)
s_statement=pd.Series(statement)
for i in range(len(statement)):
    result+=(" "+s_statement[i])
print(result.title())