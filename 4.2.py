def caesar_encrypt(text, k=7):
    result = ""
    for char in text:
        if char.isalpha(): 
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + k) % 26 + base)
            result += new_char
        else:
            result += char
    return result

plaintext = "Nguyen Thi Bao Ngoc"
ciphertext = caesar_encrypt(plaintext, k=7)
print("Plaintext: ", plaintext)
print("Ciphertext:", ciphertext)


