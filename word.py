from tkinter import *
root=Tk()
#root.geometry('2000x800')

ABC=Frame(root,bg='#000000',bd=20,relief=RIDGE)
ABC.grid()

ABC1=Frame(ABC,bd=20)
ABC1.grid()
a=1

btn2=Label(ABC,text='"...Find The Word..."',bg='black',fg='white',font=("arial",19,"bold")).grid(row=0,column=2)

label=Label(ABC,text='hai',bg='black',fg'green',font=("arial",13,'bold')).grid(row=1,column=2)

btn=Entry(ABC,text='check').grid(row=2,column=2)

btn=Button(ABC,text='check').grid(row=3,column=2)



#btn2=Label(ABC,bg='black',fg='white').grid(row=0,column=3)



root.mainloop()