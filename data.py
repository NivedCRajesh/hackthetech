import pickle
l=[]
f=open("E:\\work\\token\\data.dat","wb")
ch='y'
while ch=='y':
    n=int(input("enter token no"))
    l.append(n)
    ch=input("press y to continue")
pickle.dump(l,f)
f.close()


    
    
