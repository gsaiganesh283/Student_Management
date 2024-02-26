from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Student:
    def __init__(self,root1):
        self.root1=root1
        self.root1.geometry("1530x790+0+0")
        self.root1.title("Student Details")

        ############################    Variables    ############################

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        

        img11=Image.open(r"Images\11.jpg")
        img11=img11.resize((500,130))
        self.photoimage11=ImageTk.PhotoImage(img11)
        lbl11=Label(self.root1,image=self.photoimage11)
        lbl11.place(x=0,y=0,width=500,height=130)

        img12=Image.open(r"Images\12.jpg")
        img12=img12.resize((500,130))
        self.photoimage12=ImageTk.PhotoImage(img12)
        lbl12=Label(self.root1,image=self.photoimage12)
        lbl12.place(x=500,y=0,width=500,height=130)

        img13=Image.open(r"Images\13.jpg")
        img13=img13.resize((600,130))
        self.photoimage13=ImageTk.PhotoImage(img13)
        lbl13=Label(self.root1,image=self.photoimage13)
        lbl13.place(x=1000,y=0,width=550,height=130)

        bg_img1=Image.open(r"Images\background.jpg")
        bg_img1=bg_img1.resize((1530,710))
        self.bg_photoimage1=ImageTk.PhotoImage(bg_img1)


        bg_lbl=Label(self.root1,image=self.bg_photoimage1)
        bg_lbl.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg='green')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        bg_lbl1=Label(self.root1)
        bg_lbl1.place(x=10,y=185,width=1480,height=620)

        

        ###################    Left Label Frame    ###################

        l_lbl_frame=LabelFrame(bg_lbl1,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        l_lbl_frame.place(x=10,y=10,width=740,height=600)

        #Left Label Image

        left_img=Image.open(r"Images\13.jpg")
        left_img=left_img.resize((740,130))
        self.left_photoimage=ImageTk.PhotoImage(left_img)
        left_lbl=Label(l_lbl_frame,image=self.left_photoimage)
        left_lbl.place(x=5,y=0,width=720,height=130)

        #Current Cousers Imformation

        c_lbl_frame=LabelFrame(l_lbl_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Imformation",font=("times new roman",12,"bold"))
        c_lbl_frame.place(x=5,y=135,width=720,height=120)

        #Departmnet Details

        dep_lbl=Label(c_lbl_frame,text='Department',font=('times new roman',11,'bold'),bg="white")
        dep_lbl.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(c_lbl_frame,textvariable=self.var_dep,font=('times new roman',11,'bold'),width=17,state="readonly")
        dep_combo["values"]=("Select Department","CSE","ECE","EEE","AI","Other")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,sticky=W)

        #Course Details

        cou_lbl=Label(c_lbl_frame,text='Course',font=('times new roman',11,'bold'),bg="white")
        cou_lbl.grid(row=0,column=2,padx=10,sticky=W)

        cou_combo=ttk.Combobox(c_lbl_frame,textvariable=self.var_course,font=('times new roman',12,'bold'),width=17,state="readonly")
        cou_combo["values"]=("Select Course","Maths","Physics","Chemistry","Biology","Other")
        cou_combo.current(0)
        cou_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year Details

        yr_lbl=Label(c_lbl_frame,text='Year',font=('times new roman',11,'bold'),bg="white")
        yr_lbl.grid(row=1,column=0,padx=10,sticky=W)

        yr_combo=ttk.Combobox(c_lbl_frame,textvariable=self.var_year,font=('times new roman',12,'bold'),width=17,state="readonly")
        yr_combo["values"]=("Select Year","2019-2023","2020-2024","2021-2025","2022-2026","Other")
        yr_combo.current(0)
        yr_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester Details

        semi_lbl=Label(c_lbl_frame,text='Semester',font=('times new roman',11,'bold'),bg="white")
        semi_lbl.grid(row=1,column=2,padx=10,sticky=W)

        semi_combo=ttk.Combobox(c_lbl_frame,textvariable=self.var_semester,font=('times new roman',12,'bold'),width=17,state="readonly")
        semi_combo["values"]=("Select Semester","1","2")
        semi_combo.current(0)
        semi_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Imfomation

        class_lbl_frame=LabelFrame(l_lbl_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Imformation",font=("times new roman",12,"bold"))
        class_lbl_frame.place(x=5,y=260,width=720,height=300)

        #Student Id 

        stdid_lbl=Label(class_lbl_frame,text='Student ID:',font=('times new roman',11,'bold'),bg="white")
        stdid_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        stdid_entry=Entry(class_lbl_frame,width=20,textvariable=self.var_std_id,font=('times new roman',13,'bold'))
        stdid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student Name

        stdname_lbl=Label(class_lbl_frame,text='Student Name:',font=('times new roman',11,'bold'),bg="white")
        stdname_lbl.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        stdname_entry=Entry(class_lbl_frame,width=20,textvariable=self.var_std_name,font=('times new roman',13,'bold'))
        stdname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Student Class Division

        stddiv_lbl=Label(class_lbl_frame,text='Class Division:',font=('times new roman',11,'bold'),bg="white")
        stddiv_lbl.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        stddiv_entry=Entry(class_lbl_frame,width=20,textvariable=self.var_div,font=('times new roman',13,'bold'))
        stddiv_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No

        stdroll_lbl=Label(class_lbl_frame,text='Roll No:',font=('times new roman',11,'bold'),bg="white")
        stdroll_lbl.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        stdroll_entry=Entry(class_lbl_frame,width=20,textvariable=self.var_roll,font=('times new roman',13,'bold'))
        stdroll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender

        gen_lbl=Label(class_lbl_frame,text='Gender:',font=('times new roman',11,'bold'),bg="white")
        gen_lbl.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        gen_combo=ttk.Combobox(class_lbl_frame,textvariable=self.var_gender,font=('times new roman',11,'bold'),width=17,state="readonly")
        gen_combo["values"]=("Male","Female","Trans")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date of Birth

        dob_lbl=Label(class_lbl_frame,text='DOB:',font=('times new roman',11,'bold'),bg="white")
        dob_lbl.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        dob_entry=Entry(class_lbl_frame,width=20,textvariable=self.var_dob,font=('times new roman',13,'bold'))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #Student Email ID

        stdmail_lbl=Label(class_lbl_frame,text='Email ID:',font=('times new roman',11,'bold'),bg="white")
        stdmail_lbl.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        stdmail_entry=Entry(class_lbl_frame,width=20,textvariable=self.var_email,font=('times new roman',13,'bold'))
        stdmail_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Student Phone Number

        stdno_lbl=Label(class_lbl_frame,text='Moblie No:',font=('times new roman',11,'bold'),bg="white")
        stdno_lbl.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        stdno_entry=Entry(class_lbl_frame,width=20,textvariable=self.var_phone,font=('times new roman',13,'bold'))
        stdno_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Student Address

        stdadress_lbl=Label(class_lbl_frame,text='Address',font=('times new roman',11,'bold'),bg="white")
        stdadress_lbl.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        stdadress_entry=Entry(class_lbl_frame,width=20,textvariable=self.var_address,font=('times new roman',13,'bold'))
        stdadress_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Student Faculty Name

        stdfa_lbl=Label(class_lbl_frame,text='Faculty Name:',font=('times new roman',11,'bold'),bg="white")
        stdfa_lbl.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        stdfa_entry=Entry(class_lbl_frame,width=20,textvariable=self.var_teacher,font=('times new roman',13,'bold'))
        stdfa_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radio Buttons

        self.var_radio1=StringVar()
        r_b_1=ttk.Radiobutton(class_lbl_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        r_b_1.grid(row=7,column=0)
        self.var_radio2=StringVar()
        r_b_2=ttk.Radiobutton(class_lbl_frame,variable=self.var_radio2,text="No Photo Sample",value="NO")
        r_b_2.grid(row=7,column=2)

        #Buttons Frame

        b_frame1=Frame(class_lbl_frame,bd=2,relief=RIDGE,bg="white")
        b_frame1.place(x=0,y=200,width=715,height=35)

        save_b=Button(b_frame1,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_b.grid(row=0,column=0)

        update_b=Button(b_frame1,text="Update",width=17,command=self.update_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_b.grid(row=0,column=1)

        delete_b=Button(b_frame1,text="Delete",width=17,command=self.delete_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_b.grid(row=0,column=2)

        reset_b=Button(b_frame1,text="Reset",width=17,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_b.grid(row=0,column=3)

        b_frame2=Frame(class_lbl_frame,bd=2,relief=RIDGE,bg="white")
        b_frame2.place(x=0,y=235,width=715,height=35)

        take_photo_sample_b=Button(b_frame2,text="Take Photo Sample",width=35,command=self.generate_dataset,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_sample_b.grid(row=0,column=0)

        update_photo_b=Button(b_frame2,text="Update Photo",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_b.grid(row=0,column=1)



        ###################    Right Label Frame    ###################

        r_lbl_frame=LabelFrame(bg_lbl1,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        r_lbl_frame.place(x=760,y=10,width=700,height=580)

        #Right Label Image

        right_img=Image.open(r"Images\13.jpg")
        right_img=right_img.resize((740,130))
        self.right_photoimage=ImageTk.PhotoImage(right_img)
        right_lbl=Label(r_lbl_frame,image=self.right_photoimage)
        right_lbl.place(x=5,y=0,width=680,height=130)

        #Search System Frame

        search_lbl_frame=LabelFrame(r_lbl_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_lbl_frame.place(x=5,y=135,width=680,height=70)

        #Search Label

        search_lbl=Label(search_lbl_frame,text='Search By:',font=('times new roman',13,'bold'),bg="red")
        search_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #Search Combobox
        
        search_combo=ttk.Combobox(search_lbl_frame,font=('times new roman',12,'bold'),width=17,state="readonly")
        search_combo["values"]=("Select","Moblie Number","Roll No","Division")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,sticky=W)

        #Search Entry

        search_entry=Entry(search_lbl_frame,width=18,font=('times new roman',13,'bold'))
        search_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Search Button

        search_b=Button(search_lbl_frame,text="Search",width=11,font=("times new roman",11,"bold"),bg="blue",fg="white")
        search_b.grid(row=0,column=4)

        #Show All Button

        showall_b=Button(search_lbl_frame,text="Show All",width=11,font=("times new roman",11,"bold"),bg="blue",fg="white")
        showall_b.grid(row=0,column=5)

        #Table Frame

        table_frame=Frame(r_lbl_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=680,height=350)

        #Scroll Bar

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.stud_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gen","dob","email","moblie","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.stud_table.xview)
        scroll_y.config(command=self.stud_table.yview)

        self.stud_table.heading("dep",text="Department")
        self.stud_table.heading("course",text="Course")
        self.stud_table.heading("year",text="Year")
        self.stud_table.heading("sem",text="Semester")
        self.stud_table.heading("id",text="Student ID")
        self.stud_table.heading("name",text="Name")
        self.stud_table.heading("div",text="Division")
        self.stud_table.heading("roll",text="Roll No")
        self.stud_table.heading("gen",text="Gender")
        self.stud_table.heading("dob",text="DOB")
        self.stud_table.heading("email",text="Email ID")
        self.stud_table.heading("moblie",text="Moblie")
        self.stud_table.heading("address",text="Address")
        self.stud_table.heading("teacher",text="Teacher")
        self.stud_table.heading("photo",text="Photo")
        self.stud_table["show"]="headings"

        self.stud_table.column("dep",width=100)
        self.stud_table.column("course",width=100)
        self.stud_table.column("year",width=100)
        self.stud_table.column("sem",width=100)
        self.stud_table.column("id",width=100)
        self.stud_table.column("name",width=100)
        self.stud_table.column("div",width=100)
        self.stud_table.column("roll",width=100)
        self.stud_table.column("gen",width=100)
        self.stud_table.column("dob",width=100)
        self.stud_table.column("email",width=100)
        self.stud_table.column("moblie",width=100)
        self.stud_table.column("address",width=100)
        self.stud_table.column("teacher",width=100)
        self.stud_table.column("photo",width=150)


        self.stud_table.pack(fill=BOTH,expand=1)
        self.stud_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    

    ############################    Function Declaration    ############################
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root1)
        else:
        
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Daddy22@",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()

                ))

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Sucess","Saved Sucessfully",parent=self.root1)

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root1)

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root1)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this Student deatails",parent=self.root1)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Daddy22@",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                ))

                else:
                    if not update:
                        return 
                messagebox.showinfo("Success","Student Details Successfully Updated")
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root1)

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id must be required",parent=self.root1)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root1)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Daddy22@",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root1)
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root1)

    def reset_data(self):

                    self.var_dep.set("Select Department"),
                    self.var_course.set("Select Course"),
                    self.var_year.set("Select Year"),
                    self.var_semester.set("Select Semester"),
                    self.var_std_id.set(""),
                    self.var_std_name.set(""),
                    self.var_div.set(""),
                    self.var_roll.set(""),
                    self.var_gender.set("Male"),
                    self.var_dob.set(""),
                    self.var_email.set(""),
                    self.var_phone.set(""),
                    self.var_address.set(""),
                    self.var_teacher.set(""),
                    self.var_radio1.set("")

    

    #######################     Genrate data set or Take Photo Smaple     #######################
                    
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root1)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Daddy22@",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from Student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()      

                #######################     Load Predified data on face frontals from opencv     #######################
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user"+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root1)





    



    #######################     Fetching the Data     #######################
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Daddy22@",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.stud_table.delete(*self.stud_table.get_children())
            for i in data:
                self.stud_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #######################     Get Cursor     #######################
        
    def get_cursor(self,event=""):
        cursor_focus=self.stud_table.focus()
        content=self.stud_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),  
        self.var_std_name.set(data[5]),    
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        

        pass



if __name__ == "__main__":
    root1=Tk()
    obj1=Student(root1)
    root1.mainloop()