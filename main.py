import tkinter as tk
import segno
from tkinter import PhotoImage

root = tk.Tk()
root.title("QR code generator")
root.minsize(400, 200)


text_title = tk.StringVar(value="QR CODE GENERATOR")

title_label = tk.Label(root, textvariable=text_title, font=("Arial", 16))
title_label.pack(pady=20)

entry_label = tk.Label(root, text="Paste URL here:")
entry_label.pack()

entry = tk.Entry(root, width=40)
entry.pack(pady=10)


qr_frame = tk.Frame(root)
qr_frame.pack(pady=20)

qr_label = tk.Label(qr_frame)
qr_label.pack()

save_button = tk.Button(qr_frame, text="Save to files")


error_label = tk.Label(root, fg="red")

def save_to_files(qr):
    qr.save("your_qr_url.png", scale=8)

def get_url():
    url = entry.get().strip()

    if  url[:8] != 'https://':
        error_label.config(text="Please paste a URL")
        error_label.pack()
        return

    error_label.pack_forget()
    create_QR(url)

def create_QR(url):
    try:
        qr = segno.make_qr(url)
        qr.save("your_qr_url.png", scale=8)
        img = PhotoImage(file="your_qr_url.png")
        qr_label.config(image=img)
        qr_label.image = img  
        save_button.config(command=lambda: save_to_files(qr))
        save_button.pack(pady=10)

    except Exception as e:
        error_label.config(text=f"ERROR: {e}")
        error_label.pack()


generate_button = tk.Button(root, text="Generate", command=get_url)
generate_button.pack(pady=10)

root.mainloop()