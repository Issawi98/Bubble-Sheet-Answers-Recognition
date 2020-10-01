import cv2
import numpy as np
from tkinter import *
from tkinter import messagebox
import os
import answers
from PIL import ImageTk, Image
import image
import rotate
import scale


def buttonClick():
    # read original image.
    name = e1.get()
    # handle wrong name
    try:
        if str(name).startswith("test_sample") and e1.get() != "":
            imgOriginal = cv2.imread("Tests/" + name + ".jpg", 1)
            imgOriginal = scale.scaleImg(imgOriginal)
            img = rotate.invRotation(imgOriginal)
            cv2.imwrite("RotatedImages/rotatedImage.png", img)

            myImg = Image.open("RotatedImages/rotatedImage.png")
            myImg = myImg.resize((310, 410), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(myImg)
            l2 = Label(bg="grey", image=photo)
            l2.image = photo
            l2.grid(row=2, column=0, columnspan=2)

            # getting the circles location
            centroids, cirlesNumber, labeledImg = image.getLabels(img)
            # cv2.imshow("check", labeledImg)

            # set answers
            centroids = np.array(centroids)
            gender, semester, program, firstQ, secondQ, thirdQ, fourthQ, fifthQ = answers.getAnswers(centroids)

            # set the output text file data
            fileName = "Result.txt"
            myFile = open(fileName, 'w')
            myFile.write("Gender:   " + str(gender[0]) + "\n"
                         "Semester: " + str(semester[0]) + "\n"
                         "Program:  " + str(program[0]) + "\n\n"
                         "1. Teaching sessions" + "\n"
                         "-------------------------" + "\n"
                         "1.1 " + str(firstQ[0][0]) + "\n"
                         "1.2 " + str(firstQ[1][0]) + "\n"
                         "1.3 " + str(firstQ[2][0]) + "\n"
                         "1.4 " + str(firstQ[3][0]) + "\n"
                         "1.5 " + str(firstQ[4][0]) + "\n\n"
                         "2. Course/Module Support" + "\n"
                         "-------------------------" + "\n"
                         "2.1 " + str(secondQ[0][0]) + "\n"
                         "2.2 " + str(secondQ[1][0]) + "\n"
                         "2.3 " + str(secondQ[2][0]) + "\n"
                         "2.4 " + str(secondQ[3][0]) + "\n"
                         "2.5 " + str(secondQ[4][0]) + "\n"
                         "2.6 " + str(secondQ[5][0]) + "\n\n"
                         "3. Course/Module Organization" + "\n"
                         "-------------------------" + "\n"
                         "3.1 " + str(thirdQ[0][0]) + "\n"
                         "3.2 " + str(thirdQ[1][0]) + "\n"
                         "3.3 " + str(thirdQ[2][0]) + "\n\n"
                         "4. Course/Module Resources" + "\n"
                         "-------------------------" + "\n"
                         "4.1 " + str(fourthQ[0][0]) + "\n"
                         "4.2 " + str(fourthQ[1][0]) + "\n"
                         "4.3 " + str(fourthQ[2][0]) + "\n\n"
                         "5. Course/Module Resources" + "\n"
                         "-------------------------" + "\n"
                         "5.1 " + str(fifthQ[0][0]) + "\n"
                         "5.2 " + str(fifthQ[1][0]) + "\n\n"
                         )


            myFile.close()
            myFile = open(fileName, 'r')
            content = myFile.read()
            text1 = Text(window, height=25, width=25)
            text1.grid(row=2, column=2, rowspan=30)
            text1.insert(INSERT, content)
            sb1 = Scrollbar(window)
            sb1.grid(row=1, column=3, rowspan=10)
            text1.configure(yscrollcommand=sb1.set)
            sb1.configure(command=text1.yview)
            window.update()
            myFile.close()
            os.startfile(fileName)

            # print(gender)
            # print(semester)
            # print(program)
            # print(firstQ)
            # print(secondQ)
            # print(thirdQ)
            # print(fourthQ)
            # print(fifthQ)

            cv2.waitKey()
        else:
            messagebox.showinfo("Error", "Only accepts photos named like (test_sampleX) !!")

    except:
        messagebox.showinfo("Error", "This test sample is not found, try again !!")

# set the GUI
window = Tk()
window.geometry("585x500")
window.title("Answers Extractor")
window.iconbitmap("icon.ico")
window.resizable(False, False)
# sys.path.append('/usr/local/lib/python2.7/site-packages')

l1 = Label(window, text="Name: ")
l1.grid(row=0, column =0)

title_text=StringVar()
e1 = Entry(window, textvariable=title_text, width=50)
e1.grid(row=0, column=1)

b1 = Button(window, text="Export", width=30, command=buttonClick)
b1.grid(row=0, column=2)

l3 = Label(window, text="")
l4 = Label(window, text="")
l3.grid(row=1, column=0)

window.mainloop()
cv2.waitKey()
