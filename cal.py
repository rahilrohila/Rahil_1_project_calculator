import tkinter as tk

def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except:
            entry_var.set("Enter Number only")
    elif text == "Clear":
        entry_var.set("")
    elif text == "%":
        try:
            current = entry_var.get()
            result = str(eval(current) / 100)
            entry_var.set(result)
        except:
            entry_var.set("Error")
    else:
        entry_var.set(entry_var.get() + text)

#  main window
root = tk.Tk()
root.title("Rahil Calculator")
root.geometry("400x500")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
entry.pack(pady=20)

# Button layout
buttons = [
    ["1", "2", "3", "+"],
    ["4", "5", "6", "-"],
    ["7", "8", "9", "*"],
    ["%", "0", "=", "/"],
    ["Clear"]
]


for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        button = tk.Button(frame, text=btn_text, font=("Arial", 18), padx=20, pady=20)
        button.pack(side="left", expand=True, fill="both")
        button.bind("<Button-1>", button_click)


root.mainloop()
