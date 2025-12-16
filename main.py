import tkinter as tk

root = tk.Tk()
root.geometry("400x250")
root.title("QR code generator")

text_title = tk.StringVar()
text_title.set("QR CODE GENERATOR")

#collecting widget data
def get_url():
    url = entry.get()
    print(url)

label = tk.Label(root,
                 textvariable=text_title,
                 anchor=tk.CENTER,
                 )

entry_label = tk.Label(root, text="URL:  ")

entry = tk.Entry(root)
button = tk.Button(root, text="Generate", command=get_url)


#packing all widgets
label.pack(pady=20)
entry_label.pack(pady=0)
entry.pack(pady=20)
button.pack()

root.mainloop()
