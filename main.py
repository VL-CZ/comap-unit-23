import tkinter as tk
from tkinter import Menu, W


def main():
    # root window
    root = tk.Tk()
    root.title('Menu Demo')

    # create a menubar
    menubar = Menu(root)
    root.config(menu=menubar)

    # create a menu
    file_menu = Menu(menubar)

    # add a menu item to the menu
    file_menu.add_command(
        label='Exit',
        command=root.destroy
    )

    # add the File menu to the menubar
    menubar.add_cascade(
        label="File",
        menu=file_menu
    )

    # this will create a label widget
    l1 = tk.Label(root, text="First:")
    l2 = tk.Label(root, text="Second:")

    # grid method to arrange labels in respective
    # rows and columns as specified
    l1.grid(row=0, column=0, sticky=W, pady=2)
    l2.grid(row=1, column=0, sticky=W, pady=2)

    # entry widgets, used to take entry from user
    e1 = tk.Entry(root)
    e2 = tk.Entry(root)

    # this will arrange entry widgets
    e1.grid(row=0, column=1, pady=2)
    e2.grid(row=1, column=1, pady=2)

    root.mainloop()


if __name__ == "__main__":
    main()
