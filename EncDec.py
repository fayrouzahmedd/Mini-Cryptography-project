
import tkinter as tk

def encrypt():

    plaintext = plaintext_entry.get("1.0", "end-1c")
    key = int(key_entry.get())
    m = 26 # assuming English alphabet
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            shifted = (ord(char.upper()) - 65 + key) % m
            ciphertext += chr(shifted + 65)
        else:
            ciphertext += char
    ciphertext_entry.delete("1.0", "end")
    ciphertext_entry.insert("1.0", ciphertext)

def decrypt():
    ciphertext = ciphertext_entry.get("1.0", "end-1c")
    key = int(key_entry.get())
    m = 26 # assuming English alphabet
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = (ord(char.upper()) - 65 - key) % m
            plaintext += chr(shifted + 65)
        else:
            plaintext += char
    plaintext_entry.delete("1.0", "end")
    plaintext_entry.insert("1.0", plaintext)

root = tk.Tk()
root.title("Encryption/Decryption")

plaintext_label = tk.Label(root, text="Plaintext:")
plaintext_label.grid(row=0, column=0)

plaintext_entry = tk.Text(root, height=3, width=30)
plaintext_entry.grid(row=0, column=1)

key_label = tk.Label(root, text="Key:")
key_label.grid(row=1, column=0)

key_entry = tk.Entry(root)
key_entry.grid(row=1, column=1)

ciphertext_label = tk.Label(root, text="Ciphertext:")
ciphertext_label.grid(row=2, column=0)

ciphertext_entry = tk.Text(root, height=3, width=30)
ciphertext_entry.grid(row=2, column=1)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt, width = 10 )
encrypt_button.grid(row=3, column=0)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt, width = 10)
decrypt_button.grid(row=3, column=1)

root.mainloop()
