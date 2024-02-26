from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import cv2
import mysql.connector

class Face:
    def __init__(self,root) -> None:
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg='green')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        face_img=Image.open(r"Images\3.jpg")
        face_img=face_img.resize((650,800))
        self.face_photoimage_top=ImageTk.PhotoImage(face_img)
        face_lbl=Label(self.root,image=self.face_photoimage_top)
        face_lbl.place(x=0,y=55,width=650,height=800)

        face_img=Image.open(r"Images\5.jpg")
        face_img=face_img.resize((950,800))
        self.face_photoimage_down=ImageTk.PhotoImage(face_img)
        face_lbl=Label(self.root,image=self.face_photoimage_down)
        face_lbl.place(x=650,y=55,width=950,height=800)

        face_b=Button(face_lbl,text="Face Recognition",cursor='hand2',command=self.face_reco,font=("times new roman",15,"bold"),bg="blue",fg="white")
        face_b.place(x=350,y=600,width=200,height=40) 
        

        ###############  Face Recognition  ###############

    def face_reco(self):
            def draw_bound(img,classifier,scaleFactor,minNeighbors,color,text,clf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

                coord=[]
                for(x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                    confidence=int((100*(1-predict/300)))

                    conn=mysql.connector.connect(host="localhost",user="root",password="Daddy22@",database="face_recognizer")
                    my_cursor=conn.cursor()

                    my_cursor.execute("select Name from student where Student_id="+str(id))
                    n=my_cursor.fetchone()
                    n="+".join(n)

                    my_cursor.execute("select Roll from student where Student_id="+str(id))
                    r=my_cursor.fetchone()
                    r='+'.join(r)

                    my_cursor.execute("select Dep from student where Student_id="+str(id))
                    d=my_cursor.fetchone()
                    d='+'.join(d)



                    if confidence>77:
                        cv2.putText(img,f"Roll:{r1}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{n1}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Department:{d1}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unknow Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    

                    coord=[x,y,w,y]
                return coord
            def recognize(img,clf,faceCascade):
                coord=draw_bound(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                return img
            
            faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap=cv2.VideoCapture(0)

            while True:
                ret,img=video_cap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Welcomw To Face Recognition",img)

                if cv2.waitKey(1)==13:
                    break
            video_cap.release()
            cv2.destroyAllWindows()



if __name__ == "__main__":
    root=Tk()
    obj=Face(root)
    root.mainloop()