import tkinter as tk 

# create the main application window
root = tk.Tk()
root.title('simple tkinter app')
root.geometry('200x100')  # set window size

#function to print hello
def say_hello():
    print('hello, world!')

#create a button that triggers the say_hello function 
hello_button = tk.Button(root,text='Click me',command=say_hello)
hello_button.pack(pady=20)  # pack the button 

#start the tkinter event loop 
root.mainloop()