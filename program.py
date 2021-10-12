import math
import numpy as np
num_citys = 5

c0 = [0,0]
for i in range(num_citys):
    i +=1
    tmp = f"input('enter pos c{i}:').split(' ')"
    exec(f"tmp = {tmp}")
    tmp2 = []
    for j in tmp:
        b = j.replace(",",".")
        a = float(b)
        tmp2.append(a)
    del tmp
    exec(f"c{i} = {tmp2}")
    c2 = [4,0]
    del tmp2

c0p=0
for i in range(num_citys):
    i +=1
    tmp = f"input('enter p c{i}:')"
    exec(f"c{i}p = float({tmp})")    



def count_d_of_pos(A:list,B:list):
    xA = A[0] ; yA = A[1]
    xB = B[0] ; yB = B[1]

    d = math.sqrt((xA - xB)**2 + (yA - yB)**2)
    return d

d_ij_list = []
for i in range(num_citys):
    i+=1
    for j in range(num_citys):
        j+=1
        exec(f"A = c{i}")
        exec(f"B = c{j}")        
        d = count_d_of_pos(A,B)
        d_ij_list.append(d)
        
        
np_arr = np.array(d_ij_list)
np_arr = np_arr.reshape( num_citys, num_citys )

print(np_arr)



###############################
for i in range(1,num_citys+1):
    j = i - 1
    exec(f"P{j} = c{i}p")
    
    

n = -1
for i in range(num_citys):
    for j in range(num_citys):
        n+=1
        exec(f"d{i}{j} =  d_ij_list[{n}]")
        

E_lr_str = ""

blue_str = ""

n=0
for i in range(1,num_citys):
    j=0
    n+=1
    if n == 1 :
        txet = f"P{i} * d0{i} "
        blue_str += txet
    elif n > 1:
        txet = f"+ P{i} * d0{i} "
        for i in range(n-1):
            j +=1
            txet2 = f"*(1 - P{j}) "
            txet += txet2

        blue_str += txet


red_str = ""


n=0
c=0
for i in range(1,num_citys):
    n+=1
    c +=1
    if n == 1 :
        k=0             #2
        for j in range(n+1,num_citys):
            k+=1
            v=c
            
            if k == 1:
                txet = f"P{i} * P{j} * d{i}{j} "
                red_str += txet
            elif k > 1:
                txet = f"+ P{i} * P{j} * d{i}{j} "

                for _ in range(k-1):
                    v +=1
                    txet2 = f"*(1 - P{v}) "
                    txet += txet2
                red_str += txet
    elif n > 1:
        k=0
        for j in range(n+1,num_citys):
            k+=1
            v=c
            
            if k == 1:
                txet = f"+ P{i} * P{j} * d{i}{j} "
                red_str += txet
            elif k > 1:
                txet = f"+ P{i} * P{j} * d{i}{j} "

                for _ in range(k-1):
                    v +=1
                    txet2 = f"*(1 - P{v}) "
                    txet += txet2
                red_str += txet
                
black_str = ""
n=0
for i in range(num_citys -1 ,0,-1):
    j=num_citys
    n+=1
    if n == 1 :
        txet = f"P{i} * d0{i} "
        black_str += txet
    elif n > 1:
        txet = f"+ P{i} * d0{i} "
        for i in range(n-1):
            j -=1
            txet2 = f"*(1 - P{j}) "
            txet += txet2

        black_str += txet

E_lr_str = blue_str + "+" +red_str+ "+" +black_str

exec(f"E_lr = {E_lr_str}")
print("E_lr =",E_lr)
###############################################
