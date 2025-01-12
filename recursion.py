#recursion is contrastto iteration
#in iteration for loop is used
#it originates from lation word recurs which means to run back /again
#factorial is calculated using LIFO methodology

def fact(n):
    if n==1:
        return n
    else:
        factorial=n*fact(n-1)
        return factorial 
  
print(fact(5))

#result:- recursion takes more time and space where as iteration takes less and 
#iteration is in place it does not give us anything new


#PERMUTATION
#when we take element and make a different variations of it 
#for eg, frm a,b,c we can take 6 variations

def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]         #current chracter
            front = string[:i]         #letter before current charcter
            back = string[i+1:]        #letter after current character
            together = front + back    
            if len(pocket) == 0 or letter != pocket[0]:
                permute(together, pocket + letter)

permute("bat")
#Overall, this code demonstrates the power of recursion in solving problems 
# that can be broken down into smaller, simpler subproblems. However, 
# it is important to note that recursive functions can be less efficient than iterative solutions, as they require more memory and can lead to stack overflow errors for large inputs.




