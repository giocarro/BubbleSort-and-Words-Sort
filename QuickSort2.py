a=[5000,3,20,0,51,13]
print 'a=',a

m=0 #Start
g=0 #Upper numbers
n=0 #Lower numbers

l=len(a)
last=l-1
r=range(m,last)

b=0 #swap number
c=0 #swap interval
p=0 #pivot

for i in range(3):
    for j in r:
        if a[j]<a[last]:
            b=a[m]    #swap
            a[m]=a[j]
            a[j]=b
            m=m+1
        else:
            b=a[m+g]
            a[m+g]=a[j]
            a[j]=b
            g=g+1
        print 'a=',a,'m=',m,'g=',g
    
    b=a[last]
    a[last]=a[m]
    a[m]=b

    print '-> a=',a

    if c==0:
        if m>0:
            n=n+m    #Lower numbers n=0+2=2
            p=m      #Pivot p=2
            m=p-n    #Start m=2-2=0
            last=p-1 #End   last=2-1=1
        else:
            n=n+1
            m=n
            last=l-1
        g=0
        r=range(m,last) #r=range(0,2)=[0,1]
        c=1
    else:
        last=m+g
        r=range(m+1,last)
        c=0
    print '-->a=',a,'\tr=',r,'  c=',c,'  p=',p,'  n=',n
