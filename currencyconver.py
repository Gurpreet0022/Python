#Curreny Converter : US Dollars -> Indian Rupees

def main():
    print("Converter: US Dollars to Indian Rupees")
    print()
    
    dollars=eval(input("Enter amount in dollars:$"))
    
    rupees=convert_to_rupees(dollars)
    
    print("That is ",rupees ,"Indian rupees.")
    
convert_to_rupees=lambda dollars :dollars*83.60

main()    