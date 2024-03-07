from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from face import Face
import os
from train import Train


class Face_Recog:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"Images\1.jpg")
        img=img.resize((500,130))
        self.photoimage=ImageTk.PhotoImage(img)
        lbl=Label(self.root,image=self.photoimage)
        lbl.place(x=0,y=0,width=500,height=130)

        img2=Image.open(r"Images\2.jpg")
        img2=img2.resize((500,130))
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbl2=Label(self.root,image=self.photoimage2)
        lbl2.place(x=500,y=0,width=500,height=130)

        img3=Image.open(r"Images\3.jpg")
        img3=img3.resize((600,130))
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl3=Label(self.root,image=self.photoimage3)
        lbl3.place(x=1000,y=0,width=550,height=130)

        bg_img=Image.open(r"Images\background.jpg")
        bg_img=bg_img.resize((1530,710))
        self.bg_photoimage=ImageTk.PhotoImage(bg_img)
        bg_lbl=Label(self.root,image=self.bg_photoimage)
        bg_lbl.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg='green')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Student Button

        img4=Image.open(r"Images\4.jpg")
        img4=img4.resize((220,220))
        self.photoimage4=ImageTk.PhotoImage(img4)
        b_4=Button(self.root,image=self.photoimage4,command=self.student_details,cursor='hand2')
        b_4.place(x=200,y=200,width=220,height=220)
        bb_4=Button(self.root,text="Student Registration",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bb_4.place(x=200,y=400,width=220,height=40)

        # Face Detector

        img5=Image.open(r"Images\5.jpg")
        img5=img5.resize((220,220))
        self.photoimage5=ImageTk.PhotoImage(img5)
        b_5=Button(self.root,image=self.photoimage5,command=self.face,cursor='hand2')
        b_5.place(x=500,y=200,width=220,height=220)
        bb_5=Button(self.root,text="Course Details",command=self.face,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bb_5.place(x=500,y=400,width=220,height=40)

        # Attendance

        img6=Image.open(r"Images\61.jpg")
        img6=img6.resize((220,220))
        self.photoimage6=ImageTk.PhotoImage(img6)
        b_6=Button(self.root,image=self.photoimage6,cursor='hand2')
        b_6.place(x=800,y=200,width=220,height=220)
        bb_6=Button(self.root,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bb_6.place(x=800,y=400,width=220,height=40)

        #ChatBot

        img7=Image.open(r"Images\6.jpg")
        img7=img7.resize((220,220))
        self.photoimage7=ImageTk.PhotoImage(img7)
        b_7=Button(self.root,image=self.photoimage7,cursor='hand2')
        b_7.place(x=1100,y=200,width=220,height=220)
        bb_7=Button(self.root,text="ChatBot",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bb_7.place(x=1100,y=400,width=220,height=40)

        #Train Data

        img8=Image.open(r"Images\7.jpg")
        img8=img8.resize((220,220))
        self.photoimage8=ImageTk.PhotoImage(img8)
        b_8=Button(self.root,image=self.photoimage8,cursor='hand2',command=self.train_dataset)
        b_8.place(x=200,y=500,width=220,height=220)
        bb_8=Button(self.root,text="Grades",cursor="hand2",command=self.train_dataset,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bb_8.place(x=200,y=700,width=220,height=40)

        #Photos

        img9=Image.open(r"Images\8.jpg")
        img9=img9.resize((220,220))
        self.photoimage9=ImageTk.PhotoImage(img9)
        b_9=Button(self.root,image=self.photoimage9,cursor='hand2',command=self.open_img)
        b_9.place(x=500,y=500,width=220,height=220)
        bb_9=Button(self.root,text="Notice Board",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bb_9.place(x=500,y=700,width=220,height=40)

        #Developer

        img10=Image.open(r"Images\9.jpg")
        img10=img10.resize((220,220))
        self.photoimage10=ImageTk.PhotoImage(img10)
        b_10=Button(self.root,image=self.photoimage10,cursor='hand2')
        b_10.place(x=800,y=500,width=220,height=220)
        bb_10=Button(self.root,text="Teacher Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bb_10.place(x=800,y=700,width=220,height=40)

        #Exit

        img11=Image.open(r"Images\10.jpg")
        img11=img11.resize((220,220))
        self.photoimage11=ImageTk.PhotoImage(img11)
        b_11=Button(self.root,image=self.photoimage11,command=self.exit,cursor='hand2')
        b_11.place(x=1100,y=500,width=220,height=220)
        bb_11=Button(self.root,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bb_11.place(x=1100,y=700,width=220,height=40)

    


    ############################    Funtion Buttons    ############################

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def face(self):
        self.new_window=Toplevel(self.root)
        self.app=Face(self.new_window)

    def train_dataset(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def open_img(self):
        os.startfile("data")
    
    def exit(self):
        root.destroy()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recog(root)
    root.mainloop()