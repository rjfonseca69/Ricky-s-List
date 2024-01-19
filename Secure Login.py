#Secure Login

def check_credentials():
    # Hardcoded valid username and password (modify these)
    valid_username = "nicksaban"
    valid_password = "rolltide"

    # Get user input for username and password
    username = input("Enter your username here")
    password = input("Enter your password here")

    # Convert the entered username to lowercase for case-insensitive comparison
   
    # Check if the entered username and password match the valid credentials
    

    if username == valid_username.lower() and password == valid_password():
        print("Succesfully logged in")
  
    if username != valid_username.lower() or password != valid_password:
        print("Unsuccessful login. Try Again")
# Call the function to check credentials
check_credentials()
