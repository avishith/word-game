import tkinter as tk
import random
global list 




class Test():
	def __init__(self):
		self.root = tk.Tk()
		self.text= tk.StringVar()
		self.ans=tk.StringVar()
		
		
		self.list=["FO_R",'BO_K','MOB_LE']
		self.answer=['FOUR','BOOK','MOBILE']
		self.qus=self.list[random.randint(0,2)]
		self.list.remove(self.qus)
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
		if a=='':
			self.text.set('Try again')
			self.ans.set('')
		elif a in self.answer:
			self.text.set('wow correct')
			self.ans.set('')
			
		elif a not in self.answer:
			self.text.set('bad move')
			self.ans.set('')
		
		
app=Test()
