import tkinter as tk
from tkinter import font as tkfont
from tkinter import Menu, W, S


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        l1 = tk.Label(self, text="First:")
        l2 = tk.Label(self, text="Second:")
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        # grid method to arrange labels in respective
        # rows and columns as specified
        l1.grid(row=1, column=0, sticky=W, pady=2)
        l2.grid(row=2, column=0, sticky=W, pady=2)
        label.grid(row=0, column=0, sticky=W, pady=2)

        # entry widgets, used to take entry from user
        e1 = tk.Entry(self)
        e2 = tk.Entry(self)

        # this will arrange entry widgets
        e1.grid(row=1, column=1, pady=2)
        e2.grid(row=2, column=1, pady=2)

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=3, column=1, sticky=S, pady=2)


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
