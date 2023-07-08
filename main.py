# IMPORT AND DEPENDENCIES
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# FUNCTIONALITIES


def saving_file():
    file_location = asksaveasfilename(defaultextension="txt",
                                      filetypes=[("Text files", "*.txt"), ["All files", "*."]])
    if not file_location:
        return
    with open(file_location, "w") as f:
        text = text_edit.get(1.0, tk.END)
        f.write(text)
    root.title(f"PARAKEET: {file_location}")


def opening_file():
    file_location = askopenfilename(
        filetypes=[("Text files", "*.txt"),
                   ("All files", "*.")]
    )
    if not file_location:
        return
    text_edit.delete(1.0, tk.END)
    with open(file_location, "r") as f:
        text = f.read()
        text_edit.insert(tk.END, text)
    root.title(f"PARAKEET: {file_location}")


# ROOT WINDOW DECLARATION
root = tk.Tk()
root.title("PARAKEET NOTEPAD")
root.rowconfigure(0, minsize=800)
root.columnconfigure(1, minsize=800)

# COMPONENET ADDITION
text_edit = tk.Text(root)
text_edit.grid(row=0, column=1, sticky="nsew")

frame_button = tk.Frame(root, relief=tk.RAISED, bd=3)
frame_button.grid(row=0, column=0, sticky="ns")

button_open = tk.Button(frame_button, text="OPEN FILE", command=opening_file)
button_open.grid(row=0, column=0, padx=5, pady=5)

button_save = tk.Button(frame_button, text="SAVE AS", command=saving_file)
button_save.grid(row=1, column=0, padx=5, pady=5)

# CLOSING FILE
root.mainloop()

'''
>>> TO DO CREATE VERSION 1 EXE OUTPUT
>>> CUSTOM TKINTER INTEGRATION < VER1 >
>>> SHORTCUT INTEGRATION FOR SAVING FILE ESCAPING AND SAVING FILE < VER 1.2 >
>>> TODO CREATOR USING SPECIAL ELEMENTS < VER 2 >
'''