# Product cipher encryption function
def encrypt(text):
    cipher = ''
    for letter in text:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            cipher += chr((ord(letter) + 3 - 97) % 26 + 97)
        else:
            cipher += letter
    return cipher


# Product cipher decryption function
def decrypt(text):
    decipher = ''
    for letter in text:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            decipher += chr((ord(letter) - 3 - 97) % 26 + 97)
        else:
            decipher += letter

    return decipher
