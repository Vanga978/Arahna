import numpy as np
def get_unique_loto(num):
    a=np.arange(1,101)
    d=[]
    for i in range(num):
        b=np.random.choice(a,size=(5,5),replace=False)
        d.append(b)        
    d=np.array(d)
    return d
        

print(get_unique_loto(3))
#get_unique_loto(3)