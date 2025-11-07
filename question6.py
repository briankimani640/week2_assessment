stored_email = "user@example.com"
stored_password = "12345"

input_email = input("Enter your email: ")
input_password = input("Enter your password: ")
if input_email == stored_email and input_password == stored_password:
    print("Login successful!")
else:
    print("Invalid credentials.")

    
