import re

email= input("Enter your email id:")
pattern=re.compile(r'[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]')
if pattern.match(email):
    print('Valid Email Id')
else:
    print("Oops! Email is not valid")    