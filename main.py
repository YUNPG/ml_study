# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        # set title
        self.master.title('Machine Learning Test')
        # set window variable
        self.master.resizable(width=True, height=True)
        # open file
        data_in_entry = tk.Entry(self)
        data_in_entry.grid(row=0, column=0, columnspan=3, padx=1, pady=1, sticky=tk.NSEW)
        def open_file(entry):
            fname = filedialog.askopenfilename(title='打开S2文件', filetypes=[('txt', '*.txt'), ('All Files', '*')])
            entry.delete(0, tk.END)
            entry.insert(tk.END, fname)

        ttk.Button(self, text='Choose Train Data X', command=lambda: open_file(data_in_entry)).grid(row=0, column=3,
                                                                                                   padx=1, pady=1,
                                                                                                   sticky=tk.NSEW)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()