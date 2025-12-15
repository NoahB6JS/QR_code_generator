import tkinter as tk

root = tk.Tk()
root.geometry("400x250")
root.title("QR code generator")


text_title = tk.StringVar()
text_title.set("QR CODE GENERATOR")

label = tk.Label(root,
                 textvariable=text_title,
                 anchor=tk.CENTER,
                 )

entry_label = tk.Label(root, textvariable="URL:  ")
entry = tk.Entry(root)

label.pack(pady=20)
entry_label.pack(pady=0)
entry.pack(pady=20)

root.mainloop()
