from tkinter import *
from tkinter import messagebox

def ReadFromFile():
    reader=open('a.txt','r')
    phoneBook={}

    while True:
        text=reader.readline()
        if text=='':
            break
        name=text.split(':')[0]
        phoneNumber=text.split(':')[1]
        phoneNumber=phoneNumber.split('\n')[0]
        phoneBook[name]=phoneNumber

    return phoneBook


def WriteToFile(name,phone):
    file=open('a.txt','a') 
    format=name+':'+phone+'\n'
    file.write(format)
    file.flush()
    file.close()



window = Tk()

window.title("My PhoneBook app")

window.geometry('350x200')

lblName = Label(window, text="Name")

lblName.grid(column=0, row=0)

txtName = Entry(window,width=10)

txtName.grid(column=1, row=0)


lblPhone = Label(window, text="Phone")

lblPhone.grid(column=0, row=1)

txtPhone = Entry(window,width=10)

txtPhone.grid(column=1, row=1)





def clicked():
    name=txtName.get()
    phone=txtPhone.get()
    WriteToFile(name,phone)
    messagebox.showinfo('Arshak App Says', 'Contact Added')
    

btn = Button(window, text="Add To File", command=clicked)

btn.grid(column=2, row=3)

window.mainloop()
