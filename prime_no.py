user_in=int(input("enter the no"))
def prime(user_in):
    for i in range(2,user_in):
        if (user_in%i)==0:
            print('no is not prime')
            break

        else:
            print("prime",user_in)



prime(user_in)