# GUIBasic2-Expense.py
from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime
# ttk is theme of Tk

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย ')
GUI.geometry('600x700+500+50')

######### menu #######
menubar = Menu(GUI)
GUI.config(menu=menubar)

# File menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Save')
# help menu
def About():
	messagebox.showinfo('About','นี่คือโปรแกรม \n ของคนธรรมดา \n ทดสอบเขียนโปรแกรม')
    	
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='help', menu=helpmenu)
helpmenu.add_command(label='Hand book')
helpmenu.add_command(label='About',command=About)

#########################


Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1)

icon_t1 = PhotoImage(file='add.png') #  .subsample(2) = ย่อรูป
icon_t2 = PhotoImage(file='list.png')

Tab.add(T1, text=f'{"ค่าใช้จ่าย":^{30}}',image=icon_t1,compound='top')
Tab.add(T2, text=f'{"ค่าใช้จ่ายทั้งหมด":^{30}}',image=icon_t2,compound='top')

F1 = Frame(T1)
#F1.place(x=100,y=50)
F1.pack()

days = {'Mon':'จันทร์',
		'Tue':'อังคาร',
		'Wed':'พุธ',
		'Thu':'พฤหัสบดี',
		'Fri':'ศุกร์',
		'Sat':'เสาร์',
		'Sun':'อาทิตย์'}

def Save(event=None):
	expense = v_expense.get()
	price = v_price.get()
	quantity = v_quantity.get()

	if expense == '':
		print('No Data')
		messagebox.showwarning('Error','กรุณากรอกข้อมูลค่าใช้จ่าย')
		return
	elif price == '':
		messagebox.showwarning('Error','กรุณากรอกราคา')
		return
	elif quantity == '':
		quantity = 1

	total = float(price) * float(quantity)
	try:
		total = float(price) * float(quantity)
		# .get() คือดึงค่ามาจาก v_expense = StringVar()
		print('รายการ: {} ราคา: {}'.format(expense,price))
		print('จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total))
		text = 'รายการ: {} ราคา: {}\n'.format(expense,price)
		text = text + 'จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total)
		v_result.set(text)
		# clear ข้อมูลเก่า
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')

		# บันทึกข้อมูลลง csv อย่าลืม import csv ด้วย
		today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
		print(today)
		dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		dt = days[today] + '-' + dt
		with open('savedata.csv','a',encoding='utf-8',newline='') as f:
			# with คือสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
			# 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
			# newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
			fw = csv.writer(f) #สร้างฟังชั่นสำหรับเขียนข้อมูล
			data = [dt,expense,price,quantity,total]
			fw.writerow(data)

		# ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1
		E1.focus()
		#resulttable.delete(*resulttable.get_children())
		update_table()
		update_record()
	except:
		print('ERROR')
		messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')
		#messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
		#messagebox.showinfo('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')

# ทำให้สามารถกด enter ได้
GUI.bind('<Return>',Save) #ต้องเพิ่มใน def Save(event=None) ด้วย

FONT1 = (None,20) # None เปลี่ยนเป็น 'Angsana New'

#------Image--------

main_icon = PhotoImage(file='photo4.png')

Mainicon = Label(F1,image=main_icon)
Mainicon.pack()


#------text1--------
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#-------------------

#------text2--------
L = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()
v_price = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#-------------------

#------text3--------
L = ttk.Label(F1,text='จำนวน (ชิ้น)',font=FONT1).pack()
v_quantity = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()
#-------------------

icon_b1 = PhotoImage(file='photo2.png')

B2 = ttk.Button(F1,text=f'{"Save": >{10}}',image=icon_b1,compound='left',command=Save)
B2.pack(ipadx=50,ipady=20,pady=20)

v_result = StringVar()
v_result.set('--------ผลลัพธ์--------')
result = ttk.Label(F1, textvariable=v_result,font=FONT1,foreground='blue')
# result = Label(F1, textvariable=v_result,font=FONT1,fg='green')
result.pack(pady=20)
GUI.bind('<Tab>',lambda x: E2.focus())

# TAB2

def read_csv():
	with open('savedata.csv',newline='',encoding='utf-8') as f:
		fr = csv.reader(f)
		data = list(fr)
	return data

L = ttk.Label(T2,text='ตารางแสดงค่าใช้จ่าย',font=FONT1).pack(pady=15)

header = ['Date','Detail','Price','Qty.','Amount']
resulttable = ttk.Treeview(T2, columns=header, show='headings',height=20)
resulttable.pack()

for h in header:
	resulttable.heading(h,text=h)

headerwidth = [150,170,80,80,80]
for h,W in zip(header,headerwidth):
	resulttable.column(h,width=W)

def update_table():
	resulttable.delete(*resulttable.get_children())
	data = read_csv()
	for d in data:
		resulttable.insert('',0,value=d)


update_table()

GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()
