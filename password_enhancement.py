character_replace = {'a':'@', 'e':'3', 'i':'!', 'l':'/', 'o': '0', ' ':'_', 's':'$'}

while True:
    print("\nThis program will enhance your password strength!")
    password = input("Enter a password or 'q' to quit: ")
    secure_password = ''

    if password == 'q':
        break
    if len(password) < 8:
        print("Password should be longer than 8 characters.")
        continue
    else:
        for character in password:
            if character in character_replace:
                secure_password += character_replace[character]
            else:
                secure_password += character
    

    print(f"\nSuggested Password: {secure_password}\n")