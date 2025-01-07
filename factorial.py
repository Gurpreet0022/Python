#Write a program to find a factorial of a number .

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
n=int(input('Enter a number:'))   

print('Factorial of',n,'is',factorial(n))  