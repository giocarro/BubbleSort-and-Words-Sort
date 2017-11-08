a=[7,4,13,11,28,1]

l=len(a)
ctr=0
n=0

while(ctr<l):
    ctr=2**n + ctr
    n=n+1

n=n-1
print 'l=',l,'\tctr=',ctr,'\tn=',n

#Hijos
#2*2+1=5
#2*2+2=6
#i*2+1=hi1
#i*2+2=hi2

#Padre:
#ceil(4/2.0)-1=1
#ceil(3/2.0)-1=1
#ceil(5/2.0)-1=2
#ceil(i/2.0)-1=Padre i 

m=1

while(m>=n):
    m=2**x+m
