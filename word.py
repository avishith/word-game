from tkinter import *
root=Tk()
#root.geometry('2000x800')

ABC=Frame(root,bg='#000000',bd=20,relief=RIDGE)
ABC.grid()

ABC1=Frame(ABC,bd=20)
ABC1.grid()
a=1

btn=Button(ABC,text='check').grid(row=1,column=2)

btn2=Label(ABC,text='"...Find The Word..."',bg='black',fg='white').grid(row=0,column=2)

btn2=Label(ABC,text='hai',bg='black',fg='white').grid(row=0,column=3)



root.mainloop()