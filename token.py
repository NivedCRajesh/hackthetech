import pickle
char='y'
f=open("E:\\work\\token\\data.dat","rb+")
i=0
l=pickle.load(f)
print(l)
while char=='y':
    n=int(input("enter your token no"))
    ch='y'
    while ch=='y':
        while i<len(l):
        
            x=l[i]
            if n-x==10:
                print("Better reach the health centre now")
            elif n-x<10 and n-x>5:
                print("You are almost close")
            elif n-x<=5 and n-x>1:
                print("You are nearing")
            elif n-x==1:
                print("You are next")
            elif n-x==0:
                print("treatment going on")
            elif n-x<0:
                print("treatment over")
                break
            else:
                print("not yet")
            press=input("press y if treatment is over")
            if press=='y':
                i+=1
        break;
    char=input("press n for exiting")
        
    
