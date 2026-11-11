```python
from Tkinter import *
root = Tk()
w = Label(root, text="Hello Tkinter!")
w.pack()
root.mainloop()
```

```python
from Tkinter import *

root = Tk()

Label(root,
    text="Red Text in Times Font",
    fg = "red",
    font = "Times").pack()
Label(root,
    text="Green Text in Helvetica Font",
    fg = "light green",
    bg = "dark green",
    font = "Helvetica 16 bold italic").pack()
Label(root,
    text="Blue Text in Verdana bold",
    fg = "blue",
    bg = "yellow",
    font = "Verdana 10 bold").pack()

root.mainloop()
```

## IMAGE

```python
from Tkinter import *
root = Tk()
img = PhotoImage(file='python.gif')
my_image = Label(root, image=img)
```

```python
import Tkinter
import tkinter.Tk()

top = Tkinter.Tk()

def helloCallBack():
    tkinterEF.showinfo( "Hello Python", "Hello World")
B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
B.pack()
top.mainloop()
```

```python
root = tk.Tk()
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Quit", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)
root.mainloop()
```

## RADIO BUTTON

```python
root = tk.Tk()
v = tk.IntVar()
tk.Label(root,
    text=""Choose a
programming language:"",
    justify = tk.LEFT,
    padx = 20).pack()
tk.Radiobutton(root,
        text="Python",
        padx = 20,
        variable=v,
        value=1).pack(anchor Republic)
tk.Radiobutton(root,
        text="Perl",
        padx = 20,
        variable=v,
        value=2).pack(anchor Republic)
root.mainloop()
```

```python
import Tkinter as tk

root = tk.Tk()
var1 = tk.IntVar()
tk.Checkbutton(root, text="male", variable=var1).grid(row=0, sticky(tk.W)
var2 = tk.IntVar()
tk.Checkbutton(root, text="female", variable=var2).grid(row=1, sticky(tk.W)
root.mainloop()
```

```python
import Tkinter as tk

def show_values():
    print (w1.get(), w2.get())

root = tk.Tk()
w1 = tk.Scale(root, from_=0, to=42)
w1.pack()
w2 = tk.Scale(root, from_=0, to=200, orient=tk.HORIZONTAL)
w2.pack()
tk.Button(root, text='Show', command=show_values).pack()

root.mainloop()
```

```python
import Tkinter as tk

def show_entries():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
root = tk.Tk()
tk.Label(root, text="First Name").grid(row=0)
tk.Label(root, text="Last Name").grid(row=1)

e1 = tk.Entry(root)
e2 = tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(root, text='Quit', command=root.quit).grid(row=3, column=0, sticky(tk.W, pady=4)
tk.Button(root, text='Show', command=show_entries).grid(row=3, column=1, sticky(tk.W, pady=4)
root.mainloop( )
```

```python
import Tkinter as tk

def show_text():
    print(T.get('1.0', tk.END))

root = tk.Tk()

T = tk.Text(root, height=2, width=30)
T.pack()
T.insert(tk.END, "Just a text Widget\nin two lines\n")
B = tk.Button(root, text='Show', command=show_text)
B.pack()
root.mainloop()
```