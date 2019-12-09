# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import threading
import numpy as np
import time
import ml_linear_regression

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
        choose_panel = tk.LabelFrame(self)
        choose_panel.grid(row=0, column=0, padx=1, pady=1, sticky=tk.NSEW)
        x_in_entry = tk.Entry(choose_panel)
        x_in_entry.grid(row=0, column=0, columnspan=3, padx=1, pady=1, sticky=tk.NSEW)
        y_in_entry = tk.Entry(choose_panel)
        y_in_entry.grid(row=1, column=0, columnspan=3, padx=1, pady=1, sticky=tk.NSEW)
        x_out_entry = tk.Entry(choose_panel)
        x_out_entry.grid(row=2, column=0, columnspan=3, padx=1, pady=1, sticky=tk.NSEW)
        y_out_entry = tk.Entry(choose_panel)
        y_out_entry.grid(row=3, column=0, columnspan=3, padx=1, pady=1, sticky=tk.NSEW)
        def open_file(entry, tit_name):
            fname = filedialog.askopenfilename(title=tit_name, filetypes=[('txt', '*.txt'), ('All Files', '*')])
            entry.delete(0, tk.END)
            entry.insert(tk.END, fname)

        ttk.Button(choose_panel, text='Choose Train X', command=lambda: open_file(x_in_entry, 'Open Train X Data')).grid(row=0, column=3,
                    padx=1, pady=1, sticky=tk.NSEW)
        ttk.Button(choose_panel, text='Choose Train Y', command=lambda: open_file(y_in_entry, 'Open Train Y Data')).grid(row=1, column=3,
                    padx=1, pady=1, sticky=tk.NSEW)
        ttk.Button(choose_panel, text='Choose Test X', command=lambda: open_file(x_out_entry, 'Open Test X Data')).grid(row=2, column=3,
                    padx=1, pady=1, sticky=tk.NSEW)
        ttk.Button(choose_panel, text='Choose Test Y', command=lambda: open_file(y_out_entry, 'Open Test Y Data')).grid(row=3, column=3,
                    padx=1, pady=1, sticky=tk.NSEW)

        # train way
        train_way = ttk.Combobox(choose_panel)
        train_way.grid(row=4, column=0, columnspan=3, padx=1, pady=1, sticky=tk.NSEW)
        train_way['value'] = ['Linear Regression', 'Logistic Regression']
        train_way.current(0)
        ttk.Button(choose_panel, text='Setting', command=lambda: self.train_setting(train_way.get(), x_in_entry.get(), y_in_entry.get(),
                    x_out_entry.get(), y_out_entry.get())).grid(row=4, column=3, padx=1, pady=1, sticky=tk.NSEW)

    def train_setting(self, mode, x_in_file, y_in_file, x_out_file, y_out_file):
        if mode == 'Linear Regression':
            myPanel = tk.Toplevel(self)
            myPanel.title('Linear Regression Setting')
            tk.Label(myPanel, text='Hypothesis Func').grid(row=0, column=0, padx=1, pady=1, sticky=tk.NSEW)
            tk.Label(myPanel, text='Cost Func').grid(row=1, column=0, padx=1, pady=1, sticky=tk.NSEW)
            hf = ttk.Combobox(myPanel)
            hf.grid(row=0, column=1, columnspan=3, padx=1, pady=1, sticky=tk.NSEW)
            hf['value'] = ['Theta.T * X']
            hf.current(0)
            cf = ttk.Combobox(myPanel)
            cf.grid(row=1, column=1, columnspan=3, padx=1, pady=1, sticky=tk.NSEW)
            cf['value'] = ['2 norm', '1 norm']
            cf.current(0)
            def train_start():
                threading.Thread(target=self.linear_regression_start, args=(x_in_file, y_in_file, x_out_file, y_out_file)).start()

            ttk.Button(myPanel, text='Start', command=train_start).grid(row=2, column=3, padx=1, pady=1, sticky=tk.NSEW)
        elif mode == 'Logistic Regression':
            myPanel = tk.Toplevel(self)
            myPanel.title('Logistic Regression Setting')
            tk.Label(myPanel, text='Hypothesis Func').grid(row=0, column=0, padx=1, pady=1, sticky=tk.NSEW)
            tk.Label(myPanel, text='Cost Func').grid(row=1, column=0, padx=1, pady=1, sticky=tk.NSEW)
            hf = ttk.Combobox(myPanel)
            hf.grid(row=0, column=1, columnspan=3, padx=1, pady=1, sticky=tk.NSEW)
            hf['value'] = ['1/(1+exp(-Theta.T * X))']
            hf.current(0)
            cf = ttk.Combobox(myPanel)
            cf.grid(row=1, column=1, columnspan=3, padx=1, pady=1, sticky=tk.NSEW)
            cf['value'] = ['y*log(-h(x))+(1-y)log(1-h(x))']
            cf.current(0)
        else:
            pass

    def linear_regression_start(self, *args):
        print('Start linear regression')
        print('Extract the data...')
        x_in = self.data_extract(args[0])
        y_in = self.data_extract(args[1])
        x_out = self.data_extract(args[2])
        y_out = self.data_extract(args[3])
        m = x_in.shape[0]
        print('Extract the data successful')
        time_start = time.time()
        print('Start. ', time.asctime(time.localtime(time_start)))
        mode = 'BGD'
        #(m, x_in, y_in) = ml_linear_regression.data_creat()
        res_j_theta, res_theta = ml_linear_regression.linear_regression(mode, x_in, y_in)
        ml_linear_regression.data_analysis(m, x_in, y_in, res_j_theta, res_theta)
        print('End. time use: ' , (time.time()-time_start)*1000, ' ms')

    def data_extract(self, file):
        if not file:
            return None
        f=open(file, 'r')
        data_lists = f.readlines()
        dataset= []
        for data in data_lists:
            dataset.append(list(map(float, data.strip('\n').split())))
        dataset = np.array(dataset)
        f.close()
        print(dataset)
        return dataset


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()