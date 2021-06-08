user_in=input("enter the no")
def prime(user_in):
    for i in range(1,11):
        if user_in % i==1:
            print("no is prime")

        else:
            print("no. is not prime")
prime(6)
