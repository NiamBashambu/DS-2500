#Day 1
"""
def prime(n):
    is_prime = True
    for i in range(2,n):
        if n % i ==0:
            is_prime = False
    if is_prime:
        print("prime")
    else:
        print("not prime")


n = int(input("number"))

print(prime(n))

    """
'''

def main():
    z= input("do you want a number or a list")
    if z == "number":
        prime()
    elif z == "list":
        primelst()
    else:
        print("give either a list or a number")
    

def prime():
    try:
        name = int(input("give a number"))
    except ValueError:
        print("give a number")
    for i in range(2,name):
        if name%i == 0:
            prime = False
        else:
            prime = True
    if prime == True:
        print(f"{name} is prime!")
    else:
        print(f"{name} is not prime :(")
# Determine if every number in a list of nubmers is prime
       
    
    
def primelst():
    n = int(input("Enter number of elements : "))
 
# Below line read inputs from user using map() function
    name = list(map(int, 
    input("\nEnter the numbers : ").strip().split()))[:n]
    for i in name:
        prime= True
        for j in range(2,i):

            if i%j== 0:
                prime= False
        if prime:
            print(f'{i} is prime')
main()
    

'''


