num = int(input("the enter value"))


def star(num):
    for i in range(0,num):
        for j in range(i+1):
            print("*",end==" ")
        print("\n")
