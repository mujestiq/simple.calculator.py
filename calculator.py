import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        if entry_value.get().isdigit():
            value = int(entry_value.get())
        else:
            try:
                value = eval(entry_value.get())
            except Exception as e:
                value = "Error"

        entry_value.set(value)
        entry.update()
    elif text == "C":
        entry_value.set("")
        entry.update()
    else:
        entry_value.set(entry_value.get() + text)
        entry.update()

root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")

entry_value = tk.StringVar()
entry = tk.Entry(root, textvar=entry_value, font="lucida 20 bold")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

frame = tk.Frame(root)
frame.pack()

buttons = [
    "9", "8", "7", "6", "5", "4", "3", "2", "1", "0", ".", "=", "+", "-", "*", "/", "C"
]

row, col = 0, 0
for button in buttons:
    btn = tk.Button(frame, text=button, font="lucida 15 bold", padx=20, pady=20)
    btn.grid(row=row, column=col)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 2:
        col = 0
        row += 1

root.mainloop()
