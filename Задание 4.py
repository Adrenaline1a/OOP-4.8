#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import Tk, Canvas, ARC


if __name__ == '__main__':
    root = Tk()
    root.title('Рисунок')
    root.geometry('900x500')

    c = Canvas(root, width=900, height=500, bg='white')
    c.pack()

    c.create_oval(683, 18, 750, 84, fill="#FFFF00")
    c.create_rectangle(529, 143, 640, 360, fill='orange')
    c.create_polygon(580, 30, 490, 144, 675, 143, fill='#804040')

    c.create_rectangle(540, 160, 630, 227, fill='white')
    c.create_rectangle(580, 250, 630, 350, fill='#231111')

    c.create_arc(220,454, 400,180, fill="#c6dcdf", outline="#313939", width=3, start=-48, extent=90)
    c.create_polygon(120,420, 170,50, 220,130, 270,130, 320,50, 370,420, outline="#313939", width=3, fill='#a3bcbf')
    c.create_oval(175,160, 245, 230, fill="#fff", outline="#313939", width=3)
    c.create_oval(245,160, 315,230, fill="#fff", outline="#313939", width=3 )
    c.create_oval(213,192, 223,202, fill="#000")
    c.create_oval(264,192, 274,202, fill="#000")
    c.create_oval(235,212, 255,232, fill="#e4aaaa", outline="#313939", width=3)
    c.create_line(245,232, 245, 285, width=3)
    c.create_arc(210,285, 280,245, start=-10, extent=-160, style=ARC, width=3)
    c.create_oval(185,390, 245, 430, fill='#a3bcbf', outline="#313939", width=3 )
    c.create_oval(245,390, 305, 430, fill='#a3bcbf', outline="#313939", width=3 )

    x = 0
    while x < 900:
        c.create_arc(x, 555, x+90, 450, start=180, extent=-80, style=ARC, width=3, outline='green')
        x += 15

    root.mainloop()
