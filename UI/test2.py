import sys
from PIL import Image, ImageTk
import tkinter as tk
import argparse
import datetime
import cv2
import os
from tkinter.filedialog import askopenfilename
#from tkinter import filedialog
from tkinter import PhotoImage
from shutil import copyfile
import shutil




class Application:
    def __init__(self, output_path = "./"):


        self.vs = cv2.VideoCapture(0)  # capture video frames, 0 is your default video camera
        self.output_path = output_path  # store output path
        self.current_image = None  # current image from the camera

        self.root = tk.Tk()  # initialize root window
        self.root.title("Intellera")  # set window title
        # self.destructor function gets fired when the window is closed
        """"#self.root.protocol('WM_DELETE_WINDOW', self.destructor)"""

        self.panel = tk.Label(self.root)  # initialize image panel
        self.panel.config(height=400, width=400)
        self.panel.pack(padx=5, pady=5)

        label = tk.Label(self.root, text="Intellera")
        label.config(font=("BankGothic LT BT", 20))
        label.pack()

        label1 = tk.Label(self.root, text="<-Take Photo          Browse Photo->")
        label1.config(font=("BankGothic LT BT", 15))
        label1.pack()


        # create a button, that when pressed, will take the current frame and save it to file
        btn = tk.Button(self.root, text="Snapshot!", command=self.take_snapshot, bg="red")
        btn.config(height=2, width=12)
        btn.pack(side=tk.RIGHT, expand = True, fill = tk.BOTH)


        btn2 = tk.Button(self.root, text="Browse", command=self.browsecsv, bg="#f9f485")
        btn2.config(height=2, width=12)
        btn2.pack(side=tk.RIGHT, expand = True, fill = tk.BOTH)
        """btn3 = tk.Button(self.root, text="Refresh", command=restart_program, bg="#ff9e0a")
        btn3.config(height=2, width=12)
        btn3.pack()"""




        # start a self.video_loop that constantly pools the video sensor
        # for the most recently read frame
        self.video_loop()

    def video_loop(self):
        """ Get frame from the video stream and show it in Tkinter """
        ok, frame = self.vs.read()  # read frame from video stream
        if ok:  # frame captured without any errors
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
            self.current_image = Image.fromarray(cv2image)  # convert image for PIL
            imgtk = ImageTk.PhotoImage(image=self.current_image)  # convert image for tkinter
            self.panel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
            self.panel.config(image=imgtk)  # show the image
        self.root.after(30, self.video_loop)  # call the same function after 30 milliseconds

    def take_snapshot(self):
        cam = cv2.VideoCapture(0)
        frame = cam.read()[1]
        cv2.imwrite(filename='/Users/preetam/Desktop/101-classification/examples/img.jpg', img=frame)
        #self.video_loop()
        os.system('python env.py')
        #self.video_loop()



    def destructor(self):
        #Destroy the root object and release all resources
        print("[INFO] closing...")
        self.root.destroy()
        self.vs.release()  # release web camera
        cv2.destroyAllWindows()  # it is not mandatory in this application

    def browsecsv(self):

        #os.remove("C:/101-classification/examples/img.jpg")
        ftypes = [('Images', "*.*")]
        ttl = "Title"
        dir1 = '/home/'

        fileName = askopenfilename(filetypes=ftypes, initialdir=dir1, title=ttl)
        #os.remove("C:/101-classification/examples/img.jpg")
        shutil.copy(fileName,"/Users/preetam/Desktop/101-classification/examples/")
        #path="C:/101-classification/"
        os.chdir("/Users/preetam/Desktop/101-classification/examples/")
        #fileName.save("{}").format(fileName)
        #os.rename(fileName, "img.jpg")
        #os.system("check.bat")
        os.system("python classify.py -m 101.model -l mlb.pickle -i"+'"'+fileName+'"')
        #os.system("copy"+fileName+"C:/101-classification/examples")



#if __name__=='__main__':
    #main()
"""def restart_program():

    python = sys.executable
    os.execl(python, python, *sys.argv)"""






# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", default="./",
    help="path to output directory to store snapshots (default: current folder")
args = vars(ap.parse_args())

# start the app
print("[INFO] starting...")
pba = Application(args["output"])
pba.root.mainloop()
