import tkinter as tk
root = tk.Tk()
f = tk.Frame(root)
f.pack()

l2 = tk.Label(f, text='Quizzup', fg='#030A1C', justify='left')
l2.pack()

f1 = tk.Frame(f, height=400, width=400, bg='#2E4C94')
f1.pack()

b = tk.Button(root, text='start challenge')
b.pack()

def start_challenge():
    print('start challenge')
terms_and_conditions_var = tk.BooleanVar()
b1 = tk.Button(f, text='Submit', command= start_challenge, fg = '#030A1C', state='disabled')
b1.pack()

b = tk.Button(root, text="Themes!")
b.pack()
b['bg'] = '#2E4C94'
def terms_and_conditions_clicked ():
    print("you aggreed to terms and conditions")
    if terms_and_conditions_var.get()==True:
        b1.config(state=tk.NORMAL)
        b['bg'] = '#51b536'
    else:
        b1.config(state=tk.DISABLED)
        b['bg'] = '#e01f1f'
    print(terms_and_conditions_var.get())
cb1 = tk.Checkbutton(f, text='Agree', command= terms_and_conditions_clicked, fg= '#030A1C', state='normal', variable=terms_and_conditions_var)
cb1.pack()

release = tk.StringVar(value=0)
ra = tk.Radiobutton(root, text="Option A - Space", variable=release, value=0)
rb = tk.Radiobutton(root, text="Option B - Ground", variable=release, value=1)
rc = tk.Radiobutton(root, text="Option C - EathCore", variable=release, value=2)
ra.pack()
rb.pack()
rc.pack()

textbox = tk.StringVar()
entrybox = tk.Entry(root, textvariable= textbox)
entrybox.pack()


root.mainloop()