from tkinter import *

from datetime import  datetime
import time
import cv2
import torch

from keras_facenet import FaceNet
import os
from PIL import Image, ImageTk
from numpy import *
import numpy as np


model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

cropedFaces = []
facenet_model = FaceNet()

bestMatchName = None
bestMatchScore = 0

folderDataset = r'E:\Toshibe G\Application nodeJS\Collage\Computer Vision with DL && ML\dataset'

images = []  
datasets={}

for cl in os.listdir(folderDataset):
        name = os.path.splitext(cl)[0]
        path = os.path.join(folderDataset,cl)
        curPerson = Image.open(path)
        curPerson = curPerson.convert('RGB')
        curPerson = asarray(curPerson)
        curPerson = cv2.resize(curPerson,(160,160))
        curPerson = expand_dims(curPerson, axis=0)
        embedding = facenet_model.embeddings(curPerson)[0]
        datasets[name] = (embedding,path)



class Face_Recognition:
        
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Users Data") 

        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=55)    

        #================Image Top====================
        img_top=Image.open(r"E:\Toshibe G\Application nodeJS\Collage\Computer Vision with DL && ML\collected_images\shutterstock_589267595.jpg")
        img_top=img_top.resize((772,745),Image.ANTIALIAS)
        self.photoimgtop=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimgtop)
        f_lbl.place(x=0,y=55,width=772,height=745)

        

        img_left=Image.open(r"E:\Toshibe G\Application nodeJS\Collage\Computer Vision with DL && ML\collected_images\what-is-face-recognition-ai-for-big-brother-1024x683.jpg")
        img_left=img_left.resize((772,745),Image.ANTIALIAS)
        self.photoimgleft=ImageTk.PhotoImage(img_left)
        f_lb2=Label(self.root,image=self.photoimgleft)
        f_lb2.place(x=774,y=55,width=772,height=745)
        btn_frame=Button(self.root,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",35,"bold"),bg="darkblue",fg="white")
        btn_frame.place(x=774,y=725,width=772,height=65) 

    def mark_attendance(self,name):
        os.chdir(r"E:\Toshibe G\Application nodeJS\Collage\Computer Vision with DL && ML\Attendance")
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if(name not in name_list):
                now=datetime.now()
                d1=now.strftime("%d/%B/%Y")
                dtString=now.strftime("%I:%M:%S")
                f.writelines(f"\n{name},{dtString},{d1},Present")         


    def detect_faces(self,frame):
        results = model(frame)  # Perform detection
        faces = results.xyxy[0]  # Extract face bounding boxes
        return faces


#=========================Face Recognition
    def face_recog(self):
        cap = cv2.VideoCapture(0)
        ptime=0

        while True:
            success, frame = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            # Convert the frame to RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Detect faces in the frame
            faces =self.detect_faces(frame)

            # Display the bounding boxes on the frame
            for detection in faces:
                hamde = False
                x1, y1, x2, y2, confidence, class_id = detection.tolist()
                x1,x2,y1,y2 = int(x1),int(x2),int(y1),int(y2)


                if confidence > 0.6:
                    face_img = frame[int(y1):int(y2), int(x1):int(x2)]
                    face_img = cv2.cvtColor(face_img, cv2.COLOR_RGB2BGR)
                    face_img = cv2.resize(face_img, (160, 160))
                    face_img = cv2.convertScaleAbs(face_img)
                    cropedFaces.append(face_img)

                # Perform face recognition for all the cropped faces
                for face in cropedFaces:
                    bestMatchName = None
                    bestMatchScore = 0
                    face1 = cv2.resize(face, (160, 160))
                    mean = [0.5, 0.5, 0.5]
                    std = [0.5, 0.5, 0.5]
                    face = (face1 - mean) / std
                    face = np.expand_dims(face, axis=0)
                    embedding = facenet_model.embeddings(face)[0]

                    print(f" In Reco")
                    for name, (knownEmbedding, _) in datasets.items():
                        score = np.dot(knownEmbedding, embedding) / (np.linalg.norm(knownEmbedding) * np.linalg.norm(embedding))
                        if score > bestMatchScore:
                            bestMatchName = name
                            bestMatchScore = score
                    
                    if bestMatchScore > 0.5 and bestMatchName is not None:
                        print(f"best match name in loop {bestMatchName}")
                        print(f"best match score in loop {bestMatchScore}")
                        hamde = True

                if hamde == True:
                    label = f"{bestMatchName}:{bestMatchScore:.0%}"
                    t=6
                    cv2.putText(frame, f"{label}", (x1, y1-8), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    cv2.rectangle(frame,(x1-3,y2+8),(x2-6,y2+35),(0,0,0),cv2.FILLED)
                    cv2.putText(frame,"Successfuly !!",(x1+5,y2+30),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)   
                    now=datetime.now()
                    d1=now.strftime("%d/%B/%Y")
                    dtString=now.strftime("%I:%M:%S")
                    cv2.putText(frame,f"At:{dtString}",(x1+5,y2+59),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2) 
                    cv2.line(frame,(x1,y1),(x1+30,y1),(0,0,0),t)
                    cv2.line(frame,(x1,y1),(x1,y1+30),(0,0,0),t)
                    cv2.line(frame,(x2,y2),(x2-30,y2),(0,0,0),t)
                    cv2.line(frame,(x2,y2),(x2,y2-30),(0,0,0),t)

                    cv2.line(frame,(x2,y1),(x2-30,y1),(0,0,0),t)
                    cv2.line(frame,(x2,y1),(x2,y1+30),(0,0,0),t)

                    cv2.line(frame,(x1,y2),(x1+30,y2),(0,0,0),t)
                    cv2.line(frame,(x1,y2),(x1,y2-30),(0,0,0),t)

                    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,0),1)
                    self.mark_attendance(name=bestMatchName)
                        
            ctime=time.time()
            fps=1/(ctime-ptime)
            ptime=ctime
            cv2.rectangle(frame,(2,0),(130,40),(255,0,255),cv2.FILLED)
            cv2.putText(frame,f"FPS: {fps:.2f}",(5,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),3)
            # Convert the frame back to BGR format
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            cv2.imshow('MediaPipe Face Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()