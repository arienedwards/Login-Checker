username = ""

while True: 
    username = input("Enter username: ")

    if len(username) < 7: 
        print("Try Again: Username too short")  

    elif len(username) > 15:
        print("Try Again: Username too long") 

    else:    
        print("Strong Username")
        break
    
    
password = ""

while True:   
    password = input("Enter password: ")

    if len(password) < 8:
        print("Try Again: Password too short")

    elif len(password) > 20:
        print("Try Again: Password length is too long")

    else:
        print("Strong Password")
        break
      

