import tkinter as tk
import random
global list 




class Test():
	def __init__(self):
		self.root = tk.Tk()
		self.text= tk.StringVar()
		self.ans=tk.StringVar()
		
		
		self.list=("FO_R",'BO_K','MOB_LE')
		self.qus=self.list[random.randint(0,2)]
		self.text.set(self.qus)
		self.ABC=tk.Frame(self.root,bg='#000000',bd=20,)
		self.ABC.pack()
		
		self.ABC1=tk.Frame(self.ABC,bd=20)
		self.ABC1.pack()
		
		self.btn2=tk.Label(self.ABC,text='"...Find The Word..."',bg='black',fg='white',font=("arial",19,"bold")).pack()
		
		self.label=tk.Label(self.ABC,bg='black',textvariable=self.text,fg='green',font=("arial",13,'bold')).pack()
		
		self.Entry=tk.Entry(self.ABC,textvariable=self.ans).pack()
		
		self.btn3=tk.Button(self.ABC,text='check',command=self.change).pack()
		self.root.mainloop()
	def change(self):
		a=self.ans.get()
		a=a.upper()
		if a in self.list:
			self.text.set('wow')
		else :
			self.text.set('bad move')
		
		
app=Test()
