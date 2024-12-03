from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import MySQLdb
from tkinter import messagebox

class EmployeeManagement:
    def _init_(self,root):
        self.root=root
        self.root.geometry("1535x790+0+0")
        self.root.title('Sinox Employees')

        ''' ********************* Variables **********************'''
        self.var_department=StringVar()

        menu_bar = Frame(bg="#039BA1",height=100)
        menu_bar.place(relx=0, rely=0, relwidth=0.18, relheight=1)

        navbar = Frame(bg="#039BA1")
        navbar.place(relx=0.18, rely=0, relwidth=0.82, relheight=0.06)

        lbl_title=Label(navbar,text='SINOX  EMPLOYEES',font=('calibri',37,'bold'),fg='white',bg='#039BA1')
        lbl_title.place(x=0,y=0,relwidth=0.82,height=50)

        ''' ****************** Logo *******************'''
        #1st Image
        '''img_logo=Image.open('E:\BCA\Anand\SEM6\Python Project\Final Project\icon1.png')
        img_logo=img_logo.resize((50,50),Image.Resampling.NEAREST)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(menu_bar,image=self.photo_logo)
        self.logo.place(x=5,y=10,width=50,height=50)'''

        #img_frame=Frame(self.root,bd=0,relief=RIDGE)
        #img_frame.place(x=50,y=65,width=1430,height=50)

        home_btn=Button(menu_bar,text="HOME",command=self.home_page,width=15,font=('calibri',17,'bold'),bg='#3FB3BB',fg='white',bd=2)
        home_btn.place(relx=0.1, rely=0.07, relwidth=0.8, relheight=0.05)
        #home_btn.grid(row=0,column=0,padx=20,pady=11)

        dashboard_btn=Button(menu_bar,text="DASHBOARD",width=15,font=('calibri',17,'bold'),bg='#3FB3BB',fg='white',bd=2)
        dashboard_btn.place(relx=0.1, rely=0.14, relwidth=0.8, relheight=0.05)
        
        department_btn=Button(menu_bar,text="DEPARTMENT",command=self.department_details,width=15,font=('calibri',17,'bold'),bg='#3FB3BB',fg='white',bd=2)
        department_btn.place(relx=0.1, rely=0.21, relwidth=0.8, relheight=0.05)
        #department_btn.grid(row=1,column=0,padx=20,pady=11)

        employee_btn=Button(menu_bar,text="EMPLOYEE",command=self.employee_details,width=15,font=('calibri',17,'bold'),bg='#3FB3BB',fg='white',bd=2)
        employee_btn.place(relx=0.1, rely=0.28, relwidth=0.8, relheight=0.05)
        #employee_btn.grid(row=2,column=0,padx=20,pady=11)

        salary_btn=Button(menu_bar,text="SALARY",width=15,font=('calibri',17,'bold'),bg='#3FB3BB',fg='white',bd=2)
        salary_btn.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.05)
        #salary_btn.grid(row=3,column=0,padx=20,pady=11)

        leave_btn=Button(menu_bar,text="LEAVE",width=15,font=('calibri',17,'bold'),bg='#3FB3BB',fg='white',bd=2)
        leave_btn.place(relx=0.1, rely=0.42, relwidth=0.8, relheight=0.05)
        #leave_btn.grid(row=4,column=0,padx=20,pady=11)

        logout_btn=Button(menu_bar,text="LOGOUT",width=15,font=('calibri',17,'bold'),bg='RED',fg='black',bd=2)
        logout_btn.place(relx=0.1, rely=0.93, relwidth=0.8, relheight=0.05)
        #logout_btn.grid(row=5,column=0,padx=20,pady=300)
        
        ''' ****************** Main Frame *******************'''
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(relx=0.18, rely=0.06, relwidth=0.82, relheight=0.94)
        #main_frame.place(x=0,y=120,width=800,height=600)

        img_emp=Image.open('E:\BCA\Anand\SEM6\Python Project\Final Project\employee.png')
        img_emp=img_emp.resize((1245,775),Image.Resampling.NEAREST)
        self.photo_emp=ImageTk.PhotoImage(img_emp)

        self.logo=Label(main_frame,image=self.photo_emp)
        self.logo.place(x=5,y=5,width=1245,height=775)

    def home_page(self):
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(relx=0.18, rely=0.06, relwidth=0.82, relheight=0.94)

        img_emp=Image.open('E:\BCA\Anand\SEM6\Python Project\Final Project\employee.png')
        img_emp=img_emp.resize((1245,775),Image.Resampling.NEAREST)
        self.photo_emp=ImageTk.PhotoImage(img_emp)

        self.logo=Label(main_frame,image=self.photo_emp)
        self.logo.place(x=5,y=5,width=1245,height=775)

    def department_details(self):
        main_frame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        main_frame.place(relx=0.18, rely=0.06, relwidth=0.82, relheight=0.94)

        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Department Details',font=('calibri',17,'bold'),fg='#096A6E')
        upper_frame.place(relx=0.01, rely=0.001, relwidth=0.98, relheight=0.39)

        imge_frame=LabelFrame(upper_frame,bd=0,relief=RIDGE,bg='white')
        imge_frame.place(relx=0.30, rely=0.001, relwidth=0.70, relheight=0.99)

        img_depdetails=Image.open('E:\BCA\Anand\SEM6\Python Project\Final Project\emp.jpg')
        img_depdetails=img_depdetails.resize((900,900),Image.Resampling.NEAREST)
        self.photo_depdetails=ImageTk.PhotoImage(img_depdetails)

        self.logo=Label(imge_frame,image=self.photo_depdetails,bg='gray')
        self.logo.place(relx=0.001, rely=0.001, relwidth=0.99, relheight=0.99)
        
        lbl_department=Label(upper_frame,font=('arial',18,'bold'),text='Department Name:',bg='white',fg='#039BA1')
        lbl_department.place(relx=0.01, rely=0.05, relwidth=0.26, relheight=0.20)
        txt_department=ttk.Entry(upper_frame,textvariable=self.var_department,width=30,font=('arial',15,'bold'))
        txt_department.place(relx=0.01, rely=0.22, relwidth=0.26, relheight=0.20)

        btn_frame=LabelFrame(upper_frame,bd=0,relief=RIDGE,bg='white')
        btn_frame.place(relx=0.01, rely=0.50, relwidth=0.27, relheight=0.50)

        save_btn=Button(btn_frame,text="SAVE",width=12,command=self.insertdepartment_table,font=('Arial',15,'bold'),bg='#3FB3BB',fg='white',bd=2)
        save_btn.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        update_btn=Button(btn_frame,text="EDIT",width=12,font=('Arial',15,'bold'),bg='#3FB3BB',fg='white',bd=2)
        update_btn.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        delete_btn=Button(btn_frame,text="DELETE",width=12,font=('Arial',15,'bold'),bg='#3FB3BB',fg='white',bd=2)
        delete_btn.grid(row=1,column=0,padx=2,pady=5,sticky=W)

        cancel_btn=Button(btn_frame,text="RESET",width=12,font=('Arial',15,'bold'),bg='#3FB3BB',fg='white',bd=2)
        cancel_btn.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        down_frame=LabelFrame(main_frame,bd=3,relief=RIDGE,bg='white',text='Department Table Records',font=('calibri',17,'bold'),fg='#096A6E')
        down_frame.place(relx=0.01, rely=0.40, relwidth=0.98, relheight=0.59)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white')
        search_frame.place(x=0,y=2,width=1218,height=60)


        '''************************ Departments Table *************************'''
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0, y=65, width=1218, height=362)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("id","department",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        
        self.employee_table.heading('id',text='id')
        self.employee_table.heading('department',text='department_name')

        self.employee_table['show']='headings'
        
        self.employee_table.column('id',width=200)
        self.employee_table.column('department',width=200)

        self.employee_table.pack(fill=BOTH,expand=1)

    def insertdepartment_table(self):
        if self.var_department.get()=="":
            messagebox.showinfo("No Data Available")
        else:
            try:
                conn=MySQLdb.connect(user='root',passwd='',db='sinoxemployees',host='127.0.0.1')
                mysql_cursor=conn.cursor()
                str="insert into department values(%s)",(self.var_department.get())

                mysql_cursor.execute(str)
                conn.commit()
                mysql_cursor.close()
                conn.close()
                messagebox.showinfo("1 Record Inserted in Table")
            except:
                messagebox.showinfo("Error")
                


    def employee_details(self):
        main_frame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        main_frame.place(relx=0.18, rely=0.06, relwidth=0.82, relheight=0.94)

        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Details',font=('calibri',17,'bold'),fg='#096A6E')
        upper_frame.place(relx=0.01, rely=0.001, relwidth=0.98, relheight=0.48)

        '''***************** Labels and Entry Fields *******************'''
        lbl_dep=Label(upper_frame,text="Department",font=('arial',13,'bold'),bg='white',fg='#039BA1')
        #lbl_dep.place(relx=0.01, rely=0.01, relwidth=0.82, relheight=0.94,sticky=W)
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,font=('arial',13,'bold'),width=20,state='readonly')
        combo_dep['value']=('Select Department','HR','Killen','Policing','Store','Quality Engineer')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        lbl_Name=Label(upper_frame,font=('arial',13,'bold'),text='Name:',bg='white',fg='#039BA1')
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)
        txt_Name=ttk.Entry(upper_frame,width=22,font=('arial',13,'bold'))
        txt_Name.grid(row=0,column=3,padx=2,pady=7)

        lbl_Designition=Label(upper_frame,font=('arial',13,'bold'),text='Designition:',bg='white',fg='#039BA1')
        lbl_Designition.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        txt_Designition=ttk.Entry(upper_frame,width=22,font=('arial',13,'bold'))
        txt_Designition.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        lbl_Email=Label(upper_frame,font=('arial',13,'bold'),text='Email ID:',bg='white',fg='#039BA1')
        lbl_Email.grid(row=1,column=2,sticky=W,padx=2,pady=7)
        txt_Email=ttk.Entry(upper_frame,width=22,font=('arial',13,'bold'))
        txt_Email.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        lbl_Address=Label(upper_frame,font=('arial',13,'bold'),text='Address:',bg='white',fg='#039BA1')
        lbl_Address.grid(row=2,column=0,sticky=W,padx=2,pady=7)
        txt_Address=ttk.Entry(upper_frame,width=22,font=('arial',13,'bold'))
        txt_Address.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        lbl_married=Label(upper_frame,text="Married Status",font=('arial',13,'bold'),bg='white',fg='#039BA1')
        lbl_married.grid(row=2,column=2,padx=2,sticky=W)

        combo_married=ttk.Combobox(upper_frame,font=('arial',13,'bold'),width=20,state='readonly')
        combo_married['value']=('Select','Married','UnMarried')
        combo_married.current(0)
        combo_married.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        lbl_doj=Label(upper_frame,font=('arial',13,'bold'),text='Date of Join:',bg='white',fg='#039BA1')
        lbl_doj.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        txt_doj=ttk.Entry(upper_frame,width=22,font=('arial',13,'bold'))
        txt_doj.grid(row=3,column=1,sticky=W,padx=2,pady=7)

        lbl_dob=Label(upper_frame,font=('arial',13,'bold'),text='Date of Birth:',bg='white',fg='#039BA1')
        lbl_dob.grid(row=3,column=2,sticky=W,padx=2,pady=7)
        txt_dob=ttk.Entry(upper_frame,width=22,font=('arial',13,'bold'))
        txt_dob.grid(row=3,column=3,sticky=W,padx=2,pady=7)

        lbl_identity=Label(upper_frame,text="Identity Type",font=('arial',13,'bold'),bg='white',fg='#039BA1')
        lbl_identity.grid(row=4,column=0,padx=2,sticky=W)

        combo_identity=ttk.Combobox(upper_frame,font=('arial',13,'bold'),width=20,state='readonly')
        combo_identity['value']=('Select Identity','Adhar Card','Pan Card','Driving Licence','Passport','Ration Card')
        combo_identity.current(0)
        combo_identity.grid(row=4,column=1,padx=2,pady=10,sticky=W)

        lbl_identitynum=Label(upper_frame,font=('arial',13,'bold'),text='Identity Number:',bg='white',fg='#039BA1')
        lbl_identitynum.grid(row=4,column=2,sticky=W,padx=2,pady=7)
        txt_identitynum=ttk.Entry(upper_frame,width=22,font=('arial',13,'bold'))
        txt_identitynum.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        lbl_gender=Label(upper_frame,text="Gender",font=('arial',13,'bold'),bg='white',fg='#039BA1')
        lbl_gender.grid(row=5,column=0,padx=2,sticky=W)

        combo_gender=ttk.Combobox(upper_frame,font=('arial',13,'bold'),width=20,state='readonly')
        combo_gender['value']=('Select Gender','Male','Female','Transe Gender')
        combo_gender.current(0)
        combo_gender.grid(row=5,column=1,padx=2,pady=10,sticky=W)

        lbl_phone=Label(upper_frame,font=('arial',13,'bold'),text='Contact Number:',bg='white',fg='#039BA1')
        lbl_phone.grid(row=5,column=2,sticky=W,padx=2,pady=7)
        txt_phone=ttk.Entry(upper_frame,width=22,font=('arial',13,'bold'))
        txt_phone.grid(row=5,column=3,sticky=W,padx=2,pady=7)

        lbl_country=Label(upper_frame,font=('arial',13,'bold'),text='Country:',bg='white',fg='#039BA1')
        lbl_country.grid(row=6,column=0,sticky=W,padx=2,pady=7)
        txt_country=ttk.Entry(upper_frame,width=22,font=('arial',13,'bold'))
        txt_country.grid(row=6,column=1,sticky=W,padx=2,pady=7)

        lbl_pincode=Label(upper_frame,font=('arial',13,'bold'),text='PIN Code:',bg='white',fg='#039BA1')
        lbl_pincode.grid(row=6,column=2,sticky=W,padx=2,pady=7)
        txt_pincode=ttk.Entry(upper_frame,width=22,font=('arial',13,'bold'))
        txt_pincode.grid(row=6,column=3,sticky=W,padx=2,pady=7)

        imge_frame=LabelFrame(upper_frame,bd=0,relief=RIDGE,bg='white')
        imge_frame.place(relx=0.79, rely=0.01, relwidth=0.20, relheight=0.94)

        img_empdetails=Image.open('E:\BCA\Anand\SEM6\Python Project\Final Project\images.png')
        img_empdetails=img_empdetails.resize((320,320),Image.Resampling.NEAREST)
        self.photo_empdetails=ImageTk.PhotoImage(img_empdetails)

        self.logo=Label(imge_frame,image=self.photo_empdetails,bg='white')
        self.logo.place(relx=0.001, rely=0.001, relwidth=0.99, relheight=0.99)

        down_frame=LabelFrame(main_frame,bd=3,relief=RIDGE,bg='white',text='Employee Table Records',font=('calibri',17,'bold'),fg='#096A6E')
        down_frame.place(relx=0.01, rely=0.49, relwidth=0.98, relheight=0.50)
        
root = Tk()
obj=EmployeeManagement(root)
root.state('zoomed')
root.resizable(False, False)
root.mainloop()