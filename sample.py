n=5
sum=1
for i in range(n):
    for j in range(0,i+1):
        print(format(sum,"<3"),end=" ")
        sum+=1
         #if i==n-1 or j==0 or i>=j:
         #    print(i,end=" ")
        # else:
        #     print(" ",end=" ")
    print()