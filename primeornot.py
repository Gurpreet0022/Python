# find out whether a number is prime or not

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    if prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")