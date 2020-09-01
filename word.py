import tkinter as tk
global list 




class Test():
	def __init__(self):
		self.root = tk.Tk()
		self.text = tk.StringVar()
		self.text.set("Test")
		list=["hai","hello"]
		
		self.ABC=tk.Frame(self.root,bg='#000000',bd=20,)
		self.ABC.pack()
		
		self.ABC1=tk.Frame(self.ABC,bd=20)
		self.ABC1.pack()
		
		self.btn2=tk.Label(self.ABC,text='"...Find The Word..."',bg='black',fg='white',font=("arial",19,"bold")).pack()
		
		self.label=tk.Label(self.ABC,bg='black',textvariable=self.text,fg='green',font=("arial",13,'bold')).pack()
		
		self.btn=tk.Entry(self.ABC,).pack()
		
		self.btn3=tk.Button(self.ABC,text='check',command=self.change).pack()
		self.root.mainloop()
	def change(self):
		self.text.set("hai")
		
		
app=Test()
