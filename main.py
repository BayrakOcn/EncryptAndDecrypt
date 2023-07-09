import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
from cryptography.fernet import Fernet

window = tkinter.Tk()
window.geometry("400x800")
window.title("Encrypt Your Note")
window.config(bg="white")

key = "123"


# Image object
img = Image.open("logo.jpg")
img = ImageTk.PhotoImage(img)
# Image Label
image_label = tkinter.Label(window, image=img)
image_label.pack()

key_fernet = b'5JKanU4xkYj6yemC8Pv2yNe2ydJKI6A7f7iHnS9LjFw='
f = Fernet(key_fernet)

print(type(f))


def save_encrypt():
    global f
    if not key_entry.get() == key:
        messagebox.showerror("Wrong Key", "Please enter the key!")
    else:
        encrypted_string = str(f.encrypt(note_entry.get("1.0", tkinter.END).encode()))
        with open('Notes.txt', 'a') as file:
            file.write(title_entry.get())
            file.write("\n")
            file.write(encrypted_string)
            file.write("\n")


def decrypt_note():
    global f
    if not key_entry.get() == key:
        messagebox.showerror("Wrong Key", "Please enter the key!")
    else:
        encrypted_string = note_entry.get("1.2", tkinter.END+"-2c")
        encrypted_data = encrypted_string.encode()
        decrypted_data = f.decrypt(encrypted_data).decode()
        note_entry.delete("1.0", tkinter.END)
        note_entry.insert(tkinter.END, decrypted_data)


# Title Label
title_label = tkinter.Label(text="Title")
title_label.config(padx=40, pady=5, bg="white")
title_label.pack()
# Title Entry
title_entry = tkinter.Entry()
title_entry.pack()

# Note label
note_label = tkinter.Label(text="Enter Your Note")
note_label.config(bg="white")
note_label.pack()
# Note Entry
note_entry = tkinter.Text()
note_entry.pack()

# Key Label
key_label = tkinter.Label(text="Your Key")
key_label.config(bg="white")
key_label.pack()
# Key Entry
key_entry = tkinter.Entry()
key_entry.pack()

# Save and Encrypt
save_encrypt = tkinter.Button(text="Save & Encrypt", command=save_encrypt)
save_encrypt.pack()
# Decrypt
decrypt = tkinter.Button(text="Decrypt", command=decrypt_note)
decrypt.pack()

window.mainloop()
