#To print all the divisors of a number
def div():
    a=int(input("Enter a number="))
    d=a+1
    print("The divisors of",a,"are:")
    for b in range(1,d):
        if(a%b==0):
            print(b)
    return()
div()   
