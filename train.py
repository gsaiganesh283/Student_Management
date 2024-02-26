from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root1):
        self.root1=root1
        self.root1.geometry("1530x790+0+0")
        self.root1.title("Student Details")

        title_lbl=Label(self.root1,text="TRAIN DATA SET ",font=("times new roman",35,"bold"),bg="white",fg='red')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Top Image

        left_img=Image.open(r"Images\13.jpg")
        left_img=left_img.resize((1530,325))
        self.left_photoimage_top=ImageTk.PhotoImage(left_img)
        left_lbl=Label(self.root1,image=self.left_photoimage_top)
        left_lbl.place(x=0,y=55,width=1530,height=325)

        # Down Image

        left_img=Image.open(r"Images\13.jpg")
        left_img=left_img.resize((1530,325))
        self.left_photoimage_down=ImageTk.PhotoImage(left_img)
        left_lbl=Label(self.root1,image=self.left_photoimage_down)
        left_lbl.place(x=0,y=455,width=1530,height=325)

        # Button

        b_7=Button(self.root1,text="Train Data",cursor='hand2',command=self.train_classifier,font=("times new roman",30,"bold"),bg="red",fg="white")
        b_7.place(x=0,y=380,width=1530,height=72) 

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        ######################### Train the Classifier And Save #########################
        
        clf = cv2.face.LBPHFaceRecognizer_create()  
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!")



if __name__ == "__main__":
    root1=Tk()
    obj1=Train(root1)
    root1.mainloop()