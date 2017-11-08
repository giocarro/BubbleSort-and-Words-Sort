#!/env/bin/python

#def factorial(i):
#    if i!=0: return  i*factorial(i-1)
#    else: return 1

def Merge(a,lft,m,rgt,zum,counter):
    Mergelft(a,lft,m,zum) #Merge since lftmark to m (lft -> m)
    print 'a[lft:m]=',a[lft:m]
    Mergergt(a,m,rgt,zum) #Merge since m to rgtmark (m -> rgt)
    print 'a[m:rgt]=',a[m:rgt]
    if counter <= 2:
        counter = counter + 1
        Merge(a,lft,m,rgt,zum,counter)

def Mergelft(a,lft,m,zum):
    lft=0 #left mark
    rgt=m #right mark
    m=(rgt-lft)/2
    #rgtrst=rgt-m
    #zum=rgtrst+m

def Mergergt(a,m,rgt,zum):
    lft=m
    rgt=zum
    m=m+(rgt-lft)/2
    #rgtrst=rgt-m
    #zum=rgtrst+m

if __name__=='__main__':

    a=[5,7,2,3,8,9,1]
    l=len(a)
    lft=0 #left mark
    rgt=l #right mark
    m=(rgt-lft)/2 #pivot
    rgtrst=rgt-m #right rest = right mark - pivot / Numero de elementos del lado derecho
    zum=rgtrst+m #variable right mark
    counter=0
    #print 'm=(rgt-lft)/2= (',rgt,'-',lft,')/2 = ',m
    Merge(a,lft,m,rgt,zum,counter) 
   
    #i=6
    #factorial(i)
    #print(i*factorial(i-1))
