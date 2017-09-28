#!/env/bin/python

def bubbleSort(data):
    n=0
    m=0
    l=len(data)
    r1=range(l)
    s=l-1
    t=0
    r2=range(s)
    for i in r2:
        for j in r2:
            if j==s: break
            elif data[j]>data[j+1]:
                a=data[j]
                data[j]=data[j+1]
                data[j+1]=a
                n+=1
            #m+=1

        for k in reversed(r2):
            if k==t: break
            elif data[k]<data[k-1] and k<=s:
                a=data[k-1]
                data[k-1]=data[k]
                data[k]=a
                n+=1
            #m+=1 

        if t==s: break
        m+=1
        s-=1
        t+=1
    
    for i in r1:
        print(data[i])

    print 'Inside If: ',n
    print 'Iterations: ',m
    pass

if __name__=='__main__':
    File=open("words.txt","r")
    data=File.readlines()
    bubbleSort(data)
