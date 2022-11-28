import tkinter as tk
import string
import random

punctuation = "!#$%&*+-=?@^_."
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
similar = 'il1Lo0O'
chk = False
def calculate():
    result = ''
    global chk
    data_in = ''
    if var_lower.get():
        data_in += lowercase
    if var_upper.get():
        data_in += uppercase
    if var_nums.get():
        data_in += '1234567890'
    if var_punctuation.get():
        data_in += punctuation

    data_out = ''
    if var_similar.get():
        data_out += similar

    while not chk:
        frame_explain = tk.Frame(root)
        frame_explain.pack(fill='both')
        exp_left = tk.Label(frame_explain, text='parameter', bg='blue', fg='yellow', width=20)
        exp_right = tk.Label(frame_explain, text='value', bg="blue", fg='yellow')
        exp_left.pack(side=tk.LEFT)
        exp_right.pack(side=tk.RIGHT, fill='both', expand=True)

        frameA = tk.Frame(root)
        pass_len = tk.Label(frameA, text='length', width=20, fg='blue')
        pass_len_entry = tk.Entry(frameA)
        pass_len_entry.insert(0, '10')
        pass_len_entry.focus_set()

        frameB = tk.Frame(root)
        pass_include = tk.Label(frameB, text='include chars', width=20, fg='blue')
        pass_include_entry = tk.Entry(frameB)
        pass_include_entry.insert(0, data_in)

        frameC = tk.Frame(root)
        pass_exclude = tk.Label(frameC, text='exclude chars', width=20, fg='blue')
        pass_exclude_entry = tk.Entry(frameC)

        frameA.pack(fill='both')
        pass_len.pack(side=tk.LEFT)
        pass_len_entry.pack(side=tk.RIGHT, fill='both', expand=True)

        frameB.pack(fill='both')
        pass_include.pack(side=tk.LEFT)
        pass_include_entry.pack(side=tk.RIGHT, fill='both', expand=True)

        frameC.pack(fill='both')
        pass_exclude.pack(side=tk.LEFT)
        pass_exclude_entry.pack(side=tk.RIGHT, fill='both', expand=True)
        pass_exclude_entry.insert(0, similar)

        frame_Res = tk.Frame(root, bg='blue')
        frame_Res.pack(fill='both', expand=True)

        frame_Fin = tk.Frame(root, bg='blue')
        frame_Fin.pack(fill='both', expand=True)
        res_entry = tk.Entry(frame_Fin, width=30)

        res_entry.pack()
        res_entry.focus_set()
        get_pass_len = int(pass_len_entry.get())
        get_pass_include = pass_include_entry.get()
        get_pass_exclude = pass_exclude_entry.get()

        i = 0
        while (i < get_pass_len):
            char = get_pass_include[random.randint(0, len(get_pass_include) - 1)]
            if char not in get_pass_exclude:
                result += char
                i += 1
                continue
        if res_entry.get():
            res_entry.delete(0, 'end')
        res_entry.insert(0, result)
        chk=True
    else:
        print('-=-')
        list = root.pack_slaves()

        chk=False


root = tk.Tk()
root.geometry("700x220")
root.configure(bg='blue')

root.title("this is temporary title")

title = tk.Frame(root)
title.pack(fill=tk.X)
tk.Label(title, width=80, height=4, bg='blue', fg='yellow', text="this is a simple password generator").pack(fill=tk.X)

frame_checkbox = tk.Frame(root, height=3, bg='blue')
frame_checkbox.pack(fill='both')

var_lower = tk.IntVar()
var_upper = tk.IntVar()
var_nums = tk.IntVar()
var_punctuation = tk.IntVar()
var_similar = tk.IntVar()

var_lower.set(1)
var_upper.set(1)
var_nums.set(1)
var_punctuation.set(1)
var_similar.set(1)

lowercase_enable = tk.Checkbutton(frame_checkbox, text="lowercase", variable=var_lower, onvalue=1, offvalue=0,
                                  bg='blue', activebackground='blue', activeforeground='white')
lowercase_enable.pack(side=tk.LEFT)
uppercase_enable = tk.Checkbutton(frame_checkbox, text="UPPERcase", variable=var_upper, onvalue=1, offvalue=0,
                                  bg='blue', activebackground='blue', activeforeground='white')
uppercase_enable.pack(side=tk.LEFT)
nums_enable = tk.Checkbutton(frame_checkbox, text="123...90", variable=var_nums, onvalue=1, offvalue=0, bg='blue',
                             activebackground='blue', activeforeground='white')
nums_enable.pack(side=tk.LEFT)
punctuation_enable = tk.Checkbutton(frame_checkbox, text="!#$%&*+-", variable=var_punctuation, onvalue=1, offvalue=0,
                                    bg='blue', activebackground='blue', activeforeground='white')
punctuation_enable.pack(side=tk.LEFT)
similar_enable = tk.Checkbutton(frame_checkbox, text="il1Lo0O", variable=var_punctuation, onvalue=1, offvalue=0,
                                bg='blue', activebackground='blue', activeforeground='white')
similar_enable.pack(side=tk.LEFT)
checks = tk.Button(frame_checkbox, text='create password', bg='blue', fg='white', activeforeground='red',
                   command=calculate)
checks.pack()

root.mainloop()
