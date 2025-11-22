# Tkinter-code-

# 🖥️ Simple Tkinter App

This is a beginner-friendly Python GUI application created using the **Tkinter** library.  
The app contains a single button that prints **"hello, world!"** in the console when clicked.

---

## 📌 Features
- Graphical User Interface (GUI) with Tkinter
- Clickable button with event handling
- Lightweight and easy to understand

---

## 🧰 Requirements

- Python 3.x
- Tkinter (comes pre-installed with most Python versions)

To check if Tkinter is installed:

bash
python -m tkinter

## 🚀 How to Run

Save the script as app.py

Run the script:

python app.py


## Click the button in the window

See the output "hello, world!" in the terminal

## 📎 Source Code
- import tkinter as tk 

# create the main application window
- root = tk.Tk()
- root.title('simple tkinter app')
- root.geometry('200x100')  # set window size

- #function to print hello
- def say_hello():
-    print('hello, world!')

- #create a button that triggers the say_hello function 
- hello_button = tk.Button(root,text='Click me',command=say_hello)
- hello_button.pack(pady=20)  # pack the button 
  
- #start the tkinter event loop 
- root.mainloop()
