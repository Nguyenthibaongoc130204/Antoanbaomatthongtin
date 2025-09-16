def caesar_encrypt(text, k):
    ketqua = ""
    for char in text:
        if char.isalpha():  
            base = ord('A') if char.isupper() else ord('a')
            ketqua += chr((ord(char) - base + k) % 26 + base)
        else:
            ketqua += char  
    return ketqua
plaintext = "Nguyen Thi Bao Ngoc"
k = 7
ciphertext = caesar_encrypt(plaintext, k)
print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)
