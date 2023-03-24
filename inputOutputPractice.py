# This will be a basic input/output project. Four buttons will take input and display different outputs.

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

# Set some basic window parameters
root.title('Practice Project')
root.geometry('600x500')

label = tk.Label(root, text='Welcome to my first project!')

# Define Main()


def main():

    # Create a label
    label = tk.Label(
        root, text='Welcome to my practice project! Each button performs a different action.')
    label.pack()

    # Create top left button, which outputs a messagebox by calling message()
    topLeftButton = tk.Button(root, text='Output Message', command=message)
    topLeftButton.place(x=0, y=0, height=50, width=100)

    # Create top right button, which outputs a messagebox/question by calling askQuestion()
    topRightButton = tk.Button(root, text='Trivia', command=askQuestion)
    topRightButton.place(x=500, y=0, height=50, width=100)

    # Create bottom left button, which prints a message by calling printMessage()
    bottomLeftButton = tk.Button(
        root, text='Print Message', command=printMessage)
    bottomLeftButton.place(x=0, y=450, height=50, width=100)

    # Create bottom left button, which exits the program by calling onClose()
    bottomRightButton = tk.Button(root, text='Exit', command=onClose)
    bottomRightButton.place(x=500, y=450, height=50, width=100)

    # Protocol to call onClose() when the window is exited
    root.protocol('WM_DELETE_WINDOW', onClose)

    # Run mainloop()
    root.mainloop()

# First button which outputs a messagebox


def message():

    messagebox.showinfo(title='Output Message', message='Hey!')

# Second button which outputs a question


def askQuestion():

    answer = messagebox.askyesno(
        title='Output Message', message='Is an orange orange?')

    if answer:
        messagebox.showinfo(
            title='Correct!', message='Your answer is correct!')
    else:
        messagebox.showinfo(title='Incorrect',
                            message='Your answer is incorrect.')

# Third button which prints a message to console


def printMessage():

    print('Nice! You printed to the console.')

# Fourth button which verifies user wants to quit


def onClose():

    # If we click yes, this will return 1
    if messagebox.askyesno(title='Quit?', message='Do you really want to quit?'):
        root.destroy()


# Call main()
main()
