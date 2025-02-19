users = {"bob": "password","joe": "ABCDE","dave": "12345"}

username = input("Enter your username: ")

if username in users:
  password = input("Enter your password: ")
  if password == users[username]:
    print("You are successfully logged in.")
  else:
    print("Incorrect password!")

else:
    print("Username not found.")
   



    
