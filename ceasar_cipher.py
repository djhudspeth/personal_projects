
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    """Encrypts the text with a shift"""
    encrypted = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position >= 26:
            new_position -= 26
            new_letter = alphabet[new_position]
            encrypted += new_letter
        else:
            new_letter = alphabet[new_position]
            encrypted += new_letter
    
    print(f"The encoded text is {encrypted}")

def decrypt(encoded_text, shift_amount):
    """Decrypts the text"""
    decrypted = ""
    for letter in encoded_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        decrypted += new_letter

    print(f"The decrypted text is {decrypted}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))
    else:
        continue

    if direction == 'encode':
        encrypt(text, shift)
        break
    elif direction == 'decode':
        decrypt(text, shift)
        break