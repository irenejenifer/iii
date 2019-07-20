n=int(input())
if(n==0):
    for i in range(0,5):
        print(0,end=" ")
else:        
    for j in range(1,(n*5)+1):
        if(j%n==0):
            print(j,end=" ")
