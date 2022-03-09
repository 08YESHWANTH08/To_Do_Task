import numpy as np
start=int(input("First Number:"))
end=int(input("Last Number:"))
a1=np.array([i for i in range(start,(end+1),1)])
num=5
a2=np.zeros(len(a1)+((len(a1)-1)*num))
a2[0:len(a2):(num+1)]=a1
print(a2)