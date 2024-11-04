import re

email = input("Enter your email address: ".strip())

if re.search(r"^\w+@(\w+\.)?\w+\.(com|gov|net|edu)$",email):
    print("Email address is valid")

else:
    print("Email address is invalid")
