from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os

class Obliged:

        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("Users Data")

                #______________________Variables_______________________
                self.var_dep=StringVar()
                self.var_name=StringVar()
                self.var_id=StringVar()
                self.var_degree=StringVar()
                self.var_email=StringVar()
                self.var_phone=StringVar()
                self.var_adress=StringVar()
                self.var_gender=StringVar()


                #first Image
                img=Image.open(r"E:\Toshibe G\Application nodeJS\Collage\Computer Vision with DL && ML\collected_images\Obliged3.jfif")
                img=img.resize((500,150),Image.ANTIALIAS)
                self.photoimg=ImageTk.PhotoImage(img)

                f_lbl=Label(self.root,image=self.photoimg)
                f_lbl.place(x=0,y=0,width=500,height=150)

                #Second Image
                img1=Image.open(r"E:\Toshibe G\Application nodeJS\Collage\Computer Vision with DL && ML\collected_images\Obliged1.jfif")
                img1=img1.resize((480,150),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                f_lbl=Label(self.root,image=self.photoimg1)
                f_lbl.place(x=500,y=0,width=480,height=150)

                #third Image
                img2=Image.open(r"E:\Toshibe G\Application nodeJS\Collage\Computer Vision with DL && ML\collected_images\Obliged2.jpg")
                img2=img2.resize((550,150),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                f_lbl=Label(self.root,image=self.photoimg2)
                f_lbl.place(x=980,y=0,width=550,height=150)        

                #Back ground Image
                img3=Image.open(r"E:\Toshibe G\Application nodeJS\Collage\Computer Vision with DL && ML\collected_images\facialrecognition-1024x592.jpg")
                img3=img3.resize((1530,700),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                bg_img=Label(self.root,image=self.photoimg3)
                bg_img.place(x=0,y=150,width=1530,height=700) 
                #Title
                title_lbl=Label(bg_img,text="Users Management System",font=("times new roman",35,"bold"),bg="white",fg="green")
                title_lbl.place(x=0,y=0,width=1530,height=55)

                main_frame=Frame(bg_img,bd=2)
                main_frame.place(x=25,y=60,width=1480,height=570)

                left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Obliged Details",font=("times new roman",12,"bold"))
                left_frame.place(x=10,y=10,width=720,height=550)
                

                img4=Image.open(r"E:\Toshibe G\Application nodeJS\Collage\Computer Vision with DL && ML\collected_images\R (1).jfif")
                img4=img4.resize((675,175),Image.ANTIALIAS)
                self.photoimg4=ImageTk.PhotoImage(img4)

                f_lbl=Label(self.root,image=self.photoimg4)
                f_lbl.place(x=60,y=245,width=675,height=150) 



                #Obliged_Informations
                Obliged_Informations=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Obliged Details",font=("times new roman",12,"bold"))
                Obliged_Informations.place(x=5,y=150,width=700,height=368)  

                dep_label=Label(Obliged_Informations,text="Department",font=("times new roman",12,"bold"))
                dep_label.grid(row=0,column=0,padx=2,pady=5)
                dep_combo=ttk.Combobox(Obliged_Informations,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
                dep_combo["values"]=("Select Department","Mechanical","Electrical","Computer and information","Civil")
                dep_combo.current(0)
                dep_combo.grid(row=0,column=1,padx=2,pady=0)

                #degree_Informations
                dep_label=Label(Obliged_Informations,text="Degree",font=("times new roman",12,"bold"))
                dep_label.grid(row=0,column=2,padx=2,pady=5,sticky=W)
                dep_combo=ttk.Combobox(Obliged_Informations,textvariable=self.var_degree,font=("times new roman",12,"bold"),state="readonly")
                dep_combo["values"]=("Select Degree","Obliged","Student","Teaching Assistant","Doctor","Profeesor")
                dep_combo.current(0)
                dep_combo.grid(row=0,column=3,padx=2,pady=0)
                

                #Right_framee
                Right_framee=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Obliged Details",font=("times new roman",12,"bold"))
                Right_framee.place(x=740,y=10,width=720,height=550)
        
                imgright=Image.open(r"E:\Toshibe G\Application nodeJS\Collage\Computer Vision with DL && ML\collected_images\OIP (1).jfif")
                imgright=imgright.resize((700,120),Image.ANTIALIAS)
                self.photoimgright=ImageTk.PhotoImage(imgright)

                f_lbl=Label(self.root,image=self.photoimgright)
                f_lbl.place(x=790,y=250,width=675,height=120) 

                #search
                Search_Frame=LabelFrame(Right_framee,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
                Search_Frame.place(x=5,y=125,width=700,height=70)          

                Search_label=Label(Search_Frame,text="Search By:",font=("times new roman",15,"bold"),bg="red")
                Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

                Search_combo=ttk.Combobox(Search_Frame,font=("times new roman",12,"bold"),state="readonly",width=15)
                Search_combo["values"]=("Select","ID","Phone_No","Department","Name")
                Search_combo.current(0)
                Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

                src_entry=ttk.Entry(Search_Frame,width=15,font=("times new roman",12,"bold"))
                src_entry.grid(row=0,column=2,padx=10,sticky=W)
                
                src_btn=Button(Search_Frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="Blue",fg="white")
                src_btn.grid(row=0,column=3,padx=1)

                showAll_btn=Button(Search_Frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="Blue",fg="white")
                showAll_btn.grid(row=0,column=4,padx=1)  

                #table frame
                table_framee=Frame(Right_framee,bd=2,bg="white",relief=RIDGE,)
                table_framee.place(x=5,y=200,width=700,height=320)        

                scroll_x=ttk.Scrollbar(table_framee,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_framee,orient=VERTICAL)

                self.Obliged_table=ttk.Treeview(table_framee,columns=("dep","degree","gender","adress","email","name","phonenumber","photo sample","id"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.Obliged_table.xview)
                scroll_y.config(command=self.Obliged_table.yview)        
                self.Obliged_table.heading("dep",text="Department")
                self.Obliged_table.heading("degree",text="Degree")
                self.Obliged_table.heading("gender",text="Gender")
                self.Obliged_table.heading("adress",text="Adress")
                self.Obliged_table.heading("email",text="Email")
                self.Obliged_table.heading("name",text="Name")
                self.Obliged_table.heading("phonenumber",text="Phone Number")
                self.Obliged_table.heading("photo sample",text="Photo Sample")

                self.Obliged_table.heading("id",text="ID")

                self.Obliged_table["show"]="headings"


                self.Obliged_table.column("dep",width=100)
                self.Obliged_table.column("degree",width=100)
                self.Obliged_table.column("gender",width=130)
                self.Obliged_table.column("adress",width=130)
                self.Obliged_table.column("email",width=130)
                self.Obliged_table.column("name",width=130)
                self.Obliged_table.column("phonenumber",width=130)
                self.Obliged_table.column("photo sample",width=130)
                self.Obliged_table.column("id",width=100)

                self.Obliged_table.pack(fill=BOTH,expand=1)
                self.Obliged_table.bind("<ButtonRelease>",self.get_cursor)
                self.fetch_data()


                #Obliged information
                class_Obliged_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="University Obliged information")
                class_Obliged_frame.place(x=10,y=240,width=690,height=270)
                #Name
                Name_label=Label(class_Obliged_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
                Name_label.grid(row=0,column=0,padx=3,pady=4,sticky=W)

                Name_entry=ttk.Entry(class_Obliged_frame,textvariable=self.var_name,width=25,font=("times new roman",12,"bold"))
                Name_entry.grid(row=0,column=1,padx=3,pady=4,sticky=W)

                #phone number
                phone_number_label=Label(class_Obliged_frame,text="Phone Number:",font=("times new roman",12,"bold"),bg="white")
                phone_number_label.grid(row=0,column=2,padx=10,sticky=W)

                ObligedID_entry=ttk.Entry(class_Obliged_frame,textvariable=self.var_phone,width=30,font=("times new roman",12,"bold"))
                ObligedID_entry.grid(row=0,column=3,padx=10,sticky=W)

                #ID
                ID_label=Label(class_Obliged_frame,text="ID:",font=("times new roman",12,"bold"),bg="white")
                ID_label.grid(row=1,column=0,padx=3,pady=10,sticky=W)

                ID_entry=ttk.Entry(class_Obliged_frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
                ID_entry.grid(row=1,column=1,padx=3,pady=10,sticky=W)


                #Email
                Email_label=Label(class_Obliged_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
                Email_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

                Email_label_entry=ttk.Entry(class_Obliged_frame,textvariable=self.var_email,width=30,font=("times new roman",12,"bold"))
                Email_label_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

                #Gender
                Gender_label=Label(Obliged_Informations,text="Gender:",font=("times new roman",12,"bold"))
                Gender_label.grid(row=1,column=0,padx=3,pady=3,sticky=W)
                Gender_combo=ttk.Combobox(Obliged_Informations,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
                Gender_combo["values"]=("Select Gender","Male","Female")
                Gender_combo.current(0)
                Gender_combo.grid(row=1,column=1,padx=2,pady=0)
                
                #Adress
                Adress_label=Label(class_Obliged_frame,text="Adress:",font=("times new roman",12,"bold"),bg="white")
                Adress_label.grid(row=2,column=0,padx=3,pady=3,sticky=W)

                Adress_label_entry=ttk.Entry(class_Obliged_frame,textvariable=self.var_adress,width=25,font=("times new roman",12,"bold"))
                Adress_label_entry.grid(row=2,column=1,padx=3,pady=3,sticky=W)        


                #radio Buttons
                self.var_radio1=StringVar()
                radiobtn1=ttk.Radiobutton(class_Obliged_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
                radiobtn1.grid(row=4,column=1,padx=10,pady=10)
                
                # self.var_radio2=StringVar()
                radiobtn2=ttk.Radiobutton(class_Obliged_frame,variable=self.var_radio1,text="No Take Photo Sample",value="No")
                radiobtn2.grid(row=4,column=2,pady=10)   

                #bbuttons frame
                btn_frame=Frame(class_Obliged_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=0,y=143,width=685,height=56)     

                save_btn=Button(btn_frame,text="save",command=self.add_data,width=18,height=2,font=("times new roman",12,"bold"),bg="Blue",fg="white")
                save_btn.grid(row=0,column=0)

                update_btn=Button(btn_frame,text="Update",command=self.update_data,width=18,height=2,font=("times new roman",12,"bold"),bg="Blue",fg="white")
                update_btn.grid(row=0,column=1,padx=1)

                delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=18,height=2,font=("times new roman",12,"bold"),bg="Blue",fg="white")
                delete_btn.grid(row=0,column=2,padx=1)

                reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,height=2,font=("times new roman",12,"bold"),bg="Blue",fg="white")
                reset_btn.grid(row=0,column=3,padx=1)        
        
        
                btn_frame1=Frame(class_Obliged_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame1.place(x=0,y=200,width=685,height=56)  


                TakePhoto_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=37,height=2,font=("times new roman",12,"bold"),bg="Blue",fg="white")
                TakePhoto_btn.grid(row=1,column=0,padx=1)

                updatee_btn=Button(btn_frame1,text="Update Photo Sample",width=37,height=2,font=("times new roman",12,"bold"),bg="Blue",fg="white")
                updatee_btn.grid(row=1,column=1,padx=1)        



        #Save Function
        def add_data(self):
                if self.var_dep.get()=="Select Department" or self.var_degree.get()=="Select Degree" or self.var_gender.get()=="Select Gender" or self.var_name.get()=="" or self.var_id.get()=="" or self.var_phone.get()==""or self.var_email.get()==""or self.var_gender.get()==""or self.var_adress.get()=="" or self.var_radio1.get()=="":
                        messagebox.showerror("Error","All Fields are required",parent=self.root)
                else:
                        try:
                                conn=mysql.connector.connect(host="localhost",username="root",password="1812",database="face_recognition")
                                my_cursor=conn.cursor()
                                my_cursor.execute("insert into obliged values(%s,%s,%s,%s,%s,%s,%s,%s,%s )",(self.var_dep.get(),self.var_degree.get(),self.var_gender.get(),self.var_adress.get(),self.var_email.get(),self.var_name.get(),self.var_phone.get(),self.var_radio1.get(),self.var_id.get()))

                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("success","Obliged details have been added successfully",parent=self.root)

                        except Exception as es:
                                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



        #================fetch data=======================
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="1812",database="face_recognition")
                my_cursor=conn.cursor()                
                my_cursor.execute("select * from obliged")
                data=my_cursor.fetchall()

                if len(data)!=0:
                        self.Obliged_table.delete(*self.Obliged_table.get_children())
                        for i in data:
                                self.Obliged_table.insert("",END,values=i)
                                conn.commit()
                conn.close()
        #=================get cursor========================
        def get_cursor(self,event=""):
                cursor_focus=self.Obliged_table.focus()
                content=self.Obliged_table.item(cursor_focus)
                data=content["values"]          
                self.var_dep.set(data[0])
                self.var_degree.set(data[1])
                self.var_gender.set(data[2])
                self.var_adress.set(data[3])
                self.var_email.set(data[4])
                self.var_name.set(data[5])
                self.var_phone.set(data[6])    
                self.var_radio1.set(data[7])
                self.var_id.set(data[8])



        #Update Function
        def update_data(self):
                if self.var_dep.get()=="Select Department" or self.var_degree.get()=="Select Degree" or self.var_gender.get()=="Select Gender" or self.var_name.get()=="" or self.var_id.get()=="" or self.var_phone.get()==""or self.var_email.get()==""or self.var_adress.get()=="" or self.var_radio1.get()=="":
                        messagebox.showerror("Error","All Fields are required",parent=self.root)
                else:        
                        try: 
                                Upadate=messagebox.askyesno("Update","Do you want to update this obliged details",parent=self.root)
                                if Upadate>0:
                                        conn=mysql.connector.connect(host="localhost",username="root",password="1812",database="face_recognition")
                                        my_cursor=conn.cursor()
                                        my_cursor.execute("Update obliged set dep=%s,degree=%s,name=%s,phone=%s,gender=%s,email=%s,adress=%s,photosample=%s where id=%s",(self.var_dep.get(),self.var_degree.get(),self.var_name.get(),self.var_phone.get(),self.var_gender.get(),self.var_email.get(),self.var_adress.get(),self.var_radio1.get(),self.var_id.get(),))
                                else:
                                        if not Upadate:
                                                return
                                messagebox.showinfo("success","Student details successfully updated completly")
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                        except Exception as es:
                                messagebox.showerror("Error",f"Duo To:{str(es)}",parent=self.root)


        #Delete Function
        def delete_data(self):
                if self.var_id.get()=="":
                        messagebox.showerror("Error","obliged id must be required",parent=self.root)
                else:
                        try:
                                delete=messagebox.askyesno("obliged Delete Page","Do you want to delete this student",parent=self.root)
                                if delete>0:
                                        conn=mysql.connector.connect(host="localhost",username="root",password="1812",database="face_recognition")
                                        my_cursor=conn.cursor()
                                        sql="delete from obliged where id=%s"
                                        val=(self.var_id.get(),)
                                        my_cursor.execute(sql,val)
                                        
                                else:
                                        if not delete:
                                                return
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Delete","Successfully delete obliged details",parent=self.root)
                        except Exception as es:
                                messagebox.showerror("Error",f"Duo To:{str(es)}",parent=self.root)                        


        #ٌٌReset Function
        def reset_data(self):
                self.var_dep.set("Select Department")
                self.var_degree.set("Select Degree")
                self.var_gender.set("Select Gender")
                self.var_adress.set("")
                self.var_email.set("")
                self.var_name.set("")
                self.var_phone.set("")    
                self.var_radio1.set("")
                self.var_id.set("")

        
        #Generate Data Set or Take photo samples 
        def generate_dataset(self):
                if self.var_dep.get()=="Select Department" or self.var_degree.get()=="Select Degree" or self.var_gender.get()=="Select Gender" or self.var_name.get()=="" or self.var_id.get()=="" or self.var_phone.get()==""or self.var_email.get()==""or self.var_adress.get()==""or self.var_radio1.get()=="":
                        messagebox.showerror("Error","All Fields are required",parent=self.root)
                else:        
                        try: 
                                conn=mysql.connector.connect(host="localhost",username="root",password="1812",database="face_recognition")
                                my_cursor=conn.cursor()
                                my_cursor.execute("select * from Obliged")
                                myresult=my_cursor.fetchall()
                                id=0
                                for x in myresult:
                                        id+=1
                                my_cursor.execute("Update Obliged set dep=%s,degree=%s,name=%s,phone=%s,gender=%s,email=%s,adress=%s,photosample=%s where id=%s",(self.var_dep.get(),self.var_degree.get(),self.var_name.get(),self.var_phone.get(),self.var_gender.get(),self.var_email.get(),self.var_adress.get(),self.var_radio1.get(),self.var_id.get()==id+1))
                                conn.commit()
                                self.fetch_data()

                                #===========load predifiend data on face frontal with open cv============
                                face_classifier = cv2.CascadeClassifier(r'E:\Toshibe G\Application nodeJS\Collage\Computer Vision with DL && ML\haarcascade_frontalface_default.xml')
                                def face_cropped(img):
                                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                        faces=face_classifier.detectMultiScale(gray,1.3,5)


                                        for(x,y,w,h) in faces:
                                                face_cropped=img[y:y+h,x:x+w]
                                                return face_cropped

                                cap=cv2.VideoCapture(0)
                                img_id=0
                                while True :
                                        ret,my_frame=cap.read()
                                        if face_cropped(my_frame) is not None:
                                                img_id+=1
                                                face=cv2.resize(face_cropped(my_frame),(450,450))
                                                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)                                     
                                                os.chdir(r"E:\Toshibe G\Application nodeJS\Collage\Computer Vision with DL && ML\dataset")
                                                file_name_path=str(self.var_name.get())+".jpg"
                                                cv2.imwrite(file_name_path,face)
                                                cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
                                                cv2.imshow("Cropped Face",face)
                                                self.reset_data()
                                                conn.close()
                        

                                        if cv2.waitKey(1)==13 or int(img_id)==1:
                                                break
                                cap.release()
                                cv2.destroyAllWindows()
                                messagebox.showinfo("Result","Generation Data sets Completed Successfuly !!!")
                        except Exception as es:
                                messagebox.showerror("Error",f"Duo To:{str(es)}",parent=self.root)                        



if __name__ == "__main__":
        root=Tk()
        obj=Obliged(root)
        root.mainloop()
