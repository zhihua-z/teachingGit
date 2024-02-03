import tkinter as tk

def cipher_text():
    plaintext = text.get('1.0', tk.END)
    ciphertext = ''.join(chr(ord(char) + 3) for char in plaintext)
    result_label.config(text=f"Ciphered Text: {ciphertext}")
def decipher_text():
    ciphertext = text.get('1.0', tk.END)
    plaintext = ''.join(chr(ord(char) - 3) for char in ciphertext)
    result_label.config(text=f"Deciphered Text: {plaintext}")

# Create the main window
root = tk.Tk()
root.title("Cipher Program")

# Create and place widgets
label = tk.Label(root, text="Enter Text:")
label.pack(pady=10)

text = tk.Text(root, width=30)
text.pack(pady=10)

cipher_button = tk.Button(root, text="Cipher", command=cipher_text)
cipher_button.pack(pady=5)

decipher_button = tk.Button(root, text="Decipher", command=decipher_text)
decipher_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the main loop
root.mainloop()
