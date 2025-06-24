username = input("Enter your username:")
password = input("Enter your password:")

password_length = len(password)
password_replacement = "*" * password_length

print(
    f"Hi {username.capitalize()}, Your password {password_replacement} is {password_length} characters long."
)
