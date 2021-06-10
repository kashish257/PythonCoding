num = int(input("the enter value"))


def star(num):
    for i in range(0,num):
        for j in range(i+1):
            print("*",end==" ")
        print("\n")
------------------------------------------

def star():
    for i in range(5,0,-1):
        for z in range(1,i+1) :
            print("*",end=" ")
        for j in range(1,6-i):
            print(" ",end=" ")

        print("\n")



