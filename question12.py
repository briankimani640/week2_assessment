correct_password = "pass123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter your password: ")
    
    if user_input == correct_password:
        print("Access granted.")
        break
    else:
        attempts += 1
        print("Wrong password, try again")
        
    if attempts == max_attempts:
        print("Account locked.")
