# write a program to Check whether the entered number is even or odd
#Creating  function name called evenodd which accept a single int value  
def evenodd(n): 
    print(f"n = {n} is even" if n%2==0 else f"n = {n} is odd")

#taking input from user 
n=int(input("Enter n Value "))
#Function calling 
evenodd(n)
