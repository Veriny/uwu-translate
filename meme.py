from tkinter import *
def uwu():
    tx = content.get()
    lst = list(tx)
    for i in range (len(lst)):
        if lst[i] == '{':
            replace(lst, i, '{ \n   ')
        elif lst[i] == '}':
            replace(lst, i, '} \n \n')
        elif lst[i] == ';' and lst[i + 1] != '}':
            replace(lst, i, '; \n   ')
        elif lst[i] == ';':
            replace(lst, i, '; \n')

    res.set(''.join(lst))

def replace(arr, index, replace):
    arr[index] = "{}".format(replace)



root = Tk()
label_1 = Label(root, text = "Wewcome to UWU translate!")
label_2 = Label(root, text = "Result:")
content = StringVar()
res = StringVar()
entry_1 = Entry(root, textvariable = content)
entry_2 = Entry(root, textvariable = res)

button1 = Button(root, text="Twanswate", command = uwu, fg = "blue")



entry_1.grid(row = 1)
entry_2.grid(row = 1, column = 1)

label_1.grid(row = 0)
label_2.grid(row = 0, column = 1)
button1.grid(columnspan = 1)
root.mainloop()



