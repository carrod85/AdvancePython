import tkinter
from tkinter import messagebox
from triangle_carrod import area_triangle as at


def clicked():
    """function to obtain result from input"""
    txtResult.delete(0, 'end')
    base = float(txt.get())
    height = float(txt2.get())
    result = at.calculate_area(base, height)
    if base > 0 and height > 0:
        txtResult.insert(0, round(result, 5))
    else:
        messagebox.showerror(
            "error", "negative values not possible for triangle")
        txt.delete(0, 'end')
        txt2.delete(0, 'end')


def closing():
    """function to exit main window"""
    window.destroy()


window = tkinter.Tk()
window.title("homework 1 ICS0019")
window.geometry('500x500')

tkinter.Label(
    window,
    text="Area of triangle",
    font=(
        "Arial Bold",
        15)).grid(
    column=0,
    columnspan=2,
    row=0)
tkinter.Label(window, text='Base').grid(row=1)
tkinter.Label(window, text='Height').grid(row=2)
tkinter.Label(window, text='Area').grid(row=4)

txt = tkinter.Entry(window, width=15)
txt.grid(column=1, row=1)
txt2 = tkinter.Entry(window, width=15)
txt2.grid(column=1, row=2)
btn = tkinter.Button(window, text="Calculate", command=clicked)
btn.grid(column=0, row=3)
txtResult = tkinter.Entry(window, width=15)
txtResult.grid(column=1, row=4)

close = tkinter.Button(window, text="Quit", command=closing, width=5)
close.grid(column=4, row=5)

window.mainloop()
