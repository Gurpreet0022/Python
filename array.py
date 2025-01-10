#array
#in python , list is a dynamic array
#array stores data at a contiguous mem loc 
'''
stock_prices=[298,305,320,292,105]
print(stock_prices[0]) #day1                index strts frm 0
print(stock_prices[2])  #day3                memory refers to RAM
print(id(stock_prices[0]))
# complexity o(1) i.e const time


#o() to find a particulr value in an array is o(n) i.e worst time because we hve to iterate all the time
for i in range(len(stock_prices)):
    if stock_prices[i]==320:
        print(i)
        
#print all prices - again we hve to iterate all the items so complexity is o(n)
for price in stock_prices :              #array traversal
    print(price)        

#insert a value at prticulr index
stock_prices[2]=521
print(stock_prices)
stock_prices.insert(1,620)     #insert(index,vlue)
print(stock_prices)

#delete a value - o(n)
stock_prices.remove(521)
print(stock_prices)
print(stock_prices.pop(2))         #remove() only removes but pop()all tells which element is removed
                                   #pop() removes last element if no index is specified
'''                                   
#static array - size is fixed but in dynamic it is not like that
#whn dynamic array grows there is a overhead of memory allocation
#in java , c++ array has a fixed data type like int  or string
#in python you can store any datatype in the same array

#yearly expenses
expense=[2200,2350,2600,2130,2190]

#in feb how many xtra dollars u spent than jan
print(expense[1]-expense[0])   

#total expense in 1st quarter(3months)
print(expense[0]+expense[1]+expense[2])

#did u spent xactly 2000 dollars in any month
print(2000 in expense)   #use in keyword to check a particlar value in an array

        
#add june expense 1980 to the end of array

june=expense.append(1980)  
print(june)      
print(expense)

'''
june_exp=expense.insert(5,1980)
print(june_exp)
print(expense)
'''


#u got a refund of 200 in month of april
#april=print(expense[3])
new_april=expense[3]+200            # calculate thecorrect value by adding refund 200
print("corrected exp of april is",new_april)
#rep=expense.insert(3,new_april)     #assign the corrected value & print the array
expense[3]=new_april
print(expense)


heros=['spider man','thor','hulk','iron man','captain america']
#length of the list
print("len of list is",len(heros))

#add black panther at the end of the list
heros.append("black panther")
print(heros)

#remove black panther from last and add it after hulk
heros.pop()
print(heros)
heros.insert(3,'black panther')
print(heros)

#sort in alphabetical order - alphabetical order is bydefault
heros.sort()
print(heros)


#list of odd numbrs b/w 1 and max_num where max num is iven by the user
max_num=int(input("enter a max number:"))
odd_numbers=[]
for i in range(1,max_num):
    if i%2!=0:
        odd_numbers.append(i)
        print(odd_numbers)
        
      

#issues with array - array insertion complexity o(n)
#overhead during swapping and memory allocation        
        



               
                 
                                   