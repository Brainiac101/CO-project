x=float(input("no"))
b=0
a=round(x,0)
i=0
while a>0:
    b=b+(a%2)*10**i
    a=a//2
    i+=1

n=0
r=x-x//1
while r!=0 :
    n+=1
    r=r*10
    r=r-r//1

x2=x-x//1
for j in range(7):#n
    x2=x2*2
    b=b+(x2//1)*10**(-j-1)
    x2=x2-x2//1
print(b)
