import numpy as np
#4.Array datatype conversion
a1=np.array([1,2,3,4,5])
print("Data Type Is \'int32\':",a1)
a1=a1.astype('float64')
print("Data Type Is \'",a1.dtype,"\':",a1)
#3.Identity Matrix
ord=int(input("Enter The Order Of The Required Identity Matrix:"))
I=np.identity(ord,dtype='int32')
print(I)