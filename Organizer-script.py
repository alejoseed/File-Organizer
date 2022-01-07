"""
==========================================================
= Date: 09/2021                                          =
= Written: Alejandro Palmar                              =
==========================================================
"""


import shutil, tkinter, os, time, sys, setuptools, base64
from tkinter import *
from tkinter import filedialog as fd



class GUI(Tk):
    # Initialize the init passing the self argument
    # Also I put my name and set a predetermined size for the windows"


    def __init__(self):
        super().__init__()
        self.geometry("330x330")
        self.title('Organizer === Alejandro Palmar')

    # set a path to the icons so that it can be used in any computer
        def get_path(filename):
            if hasattr(sys, "_MEIPASS"):
                return os.path.join(sys._MEIPASS, filename)
            else:
                return filename
        self.iconbitmap(get_path('icon.ico'))

    # Self-Explanatory, but I also limit the filetype
    # to what is relevant in my project
    # while still being able to modify it in case I consider it necessary
    def findPath(self):
        count = 0
        filetypes = (('Exported Scans', '*.cxpxp'), ('All files', '*.*'))
        self.partialPath = fd.askopenfilename(title='Select the folder', filetypes=filetypes)
        self.path = os.path.dirname(self.partialPath)

        # Close the program in case of no file selected, and prompt an error message to inform the user"

        while (self.path == ''):
            self.partialPath = fd.askopenfilename(title='Select the folder', filetypes=filetypes)
            self.path = os.path.dirname(self.partialPath)
            count += 1
            if count == 3:
                tkinter.messagebox.showerror(title="EXITING", message="You did not select a folder")
                sys.exit(1)
        return self.path

    def startOp(self, path_value):
        self.button_Frame = Frame(self)
        self.button_Frame.pack(expand=True)
        self.start_Button = Button(self.button_Frame, text='Organize files', command=lambda: self.startOperation(
            path_value)).grid(row=0, column=0)

    def startOperation(self, path_value):
        os.chdir(path_value)
        self.file_list = os.listdir()
        no_of_files = len(self.file_list)
        if len(self.file_list) == 0:
            self.error_label = Label(text="The folder you selected is empty.").pack()
            sys.exit(1)

        # I decided to organize the files in a date basis to make it easier to find them in a time period
        for file in self.file_list:
            if file.endswith(".cxpxp"):
                self.dir_name = time.strftime("%m%d%Y")
                self.new_path = os.path.join(path_value, self.dir_name)
                self.file_list = os.listdir()
                if self.dir_name not in self.file_list:
                    os.mkdir(self.new_path)
                shutil.move(file, self.new_path)

        # In case of error, a message will be display, to avoid a hard crash
        if (no_of_files != 0):
            success = Label(text="Operation was Successful!").pack()
            successTwo = Label(text="Thanks for Using my Program.").pack()
        else:
            opError = Label(text="The Operation Failed. Try again").pack()

if __name__ == '__main__':
    object = GUI()
    path = object.findPath()
    object.startOp(path)
    object.mainloop()
