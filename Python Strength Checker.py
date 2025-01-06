## Python Strength Checker

#Enter your Password
password= input('Enter you Password:')
if len(password)<8:
      print('Password must contain atleast one upper case letter , lower case case letter and one special character')
else:
    def check_password_strength(password):
       if not re.search(r'[A-Z]',password):
        return "Weak:Include atleast one upper case letter"
       if not re.search(r'[a-z]',password):
        return "Weak: Include atleast one lower case letter"
       if not re.search(r'[0-9]',password):
        return "Weak: Include atleast one number"
       if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password) :
        return "Weak: Include atleast one special character"
       else:
      check_password_strength(password)



    