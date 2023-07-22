email = input("Enter Your Email: ").strip()

username = email[:email.index('@')]
firstname = email[:email.index('.')]
lastname = email[email.index('.')+1:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"Your username is {firstname.title()} {lastname.title()} & domain is {domain}")