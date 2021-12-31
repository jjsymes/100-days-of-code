ALPHABET_LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET_UPPER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(text, shift):
    encrypted_text = ""
    shift = shift % len(ALPHABET_LOWER)
    for letter in text:
        if letter in ALPHABET_LOWER:
            index = ALPHABET_LOWER.index(letter)
            if index + shift > len(ALPHABET_LOWER) - 1:
                encrypted_text += ALPHABET_LOWER[(index + shift - len(ALPHABET_LOWER))]
            else:
                encrypted_text += ALPHABET_LOWER[index + shift]
        elif letter in ALPHABET_UPPER:
            index = ALPHABET_UPPER.index(letter)
            if index + shift > len(ALPHABET_UPPER) - 1:
                encrypted_text += ALPHABET_UPPER[(index + shift - len(ALPHABET_UPPER))]
            else:
                encrypted_text += ALPHABET_UPPER[index + shift]
        else:
            encrypted_text += letter
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    shift = shift % len(ALPHABET_LOWER)
    for letter in text:
        if letter in ALPHABET_LOWER:
            index = ALPHABET_LOWER.index(letter)
            if index - shift < 0:
                decrypted_text += ALPHABET_LOWER[(index - shift + len(ALPHABET_LOWER))]
            else:
                decrypted_text += ALPHABET_LOWER[index - shift]
        elif letter in ALPHABET_UPPER:
            index = ALPHABET_UPPER.index(letter)
            if index - shift < 0:
                decrypted_text += ALPHABET_UPPER[(index - shift + len(ALPHABET_UPPER))]
            else:
                decrypted_text += ALPHABET_UPPER[index - shift]
        else:
            decrypted_text += letter
    return decrypted_text

mode = input("Would you like to 'encrypt' or 'decrypt'? ")

if mode != "encrypt" and mode != "decrypt":
    raise Exception("Not a valid mode")

user_input = input(f"What would you like to {mode}? ")
shift = int(input("What is your shift register? "))

if mode == "encrypt":
    encrypted = encrypt(user_input, shift)
    print(f"Encrypted text: {encrypted}")
else:
    decrypted = decrypt(user_input, shift)
    print(f"Decrypted text: {decrypted}")
