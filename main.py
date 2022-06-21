
# This is a sample Python script.
import re
import struct
from tkinter import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import filedialog
from tkinter.filedialog import *
import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
# from PIL import Image

# outputFile = "C:/Users/Stasy/Desktop/output2FLASH.txt"

fileNamesFluor = ""
fileNamesColor = ""

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Bye, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def selectFluorescentImages():
    global fileNamesFluor
    outputFile = format(text0.get("1.0", 'end-1c'))
    fileNamesFluor = askopenfilenames(parent=window)
    fileNamesFluor = sorted(fileNamesFluor)
    for fileName in fileNamesFluor:
        print(fileName)

    text0.insert(INSERT, 'Готово')

def selectColorImages():
    global fileNamesColor
    outputFile = format(text0.get("1.0", 'end-1c'))
    fileNamesColor = askopenfilenames(parent=window)
    fileNamesColor = sorted(fileNamesColor)
    for fileName in fileNamesColor:
        print(fileName)

    text1.insert(INSERT, 'Готово')

def Generator():
    fileNameOutput = ""
    for i in range(len(fileNamesFluor)):
        print(i)
        print(type(fileNameOutput))
        # imgFluor = cv2.imread(fileNamesFluor[i], cv2.IMREAD_GRAYSCALE).astype(np.float32)
        # imgColor = cv2.imread(fileNamesColor[i], cv2.IMREAD_GRAYSCALE).astype(np.float32)
        imgFluor = cv2.imread(fileNamesFluor[i])
        imgColor = cv2.imread(fileNamesColor[i])
        fileNameOutput = fileNameOutput[:-3]+'output.bmp'
        print(fileNameOutput)
        print(type(fileNameOutput))
        # img = cv2.divide(imgFluor, imgColor)
        img = cv2.subtract(imgFluor, imgColor)
        # img = BGR
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img[:, :, 0]
        cv2.imshow('img',img)
        # image_eq = cv2.equalizeHist(img)
        image_eq = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
        # image_eq = image_eq.astype(np.uint8)
        #####################################################
        # cv2.imshow("Image", image_eq)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        ######################################################
        # plt.imshow(img, clim = (np.max(img)*0.01, np.max(img)*0.99))
        # plt.imshow(img, clim=(25, 125))
        # plt.imshow(img)
        plt.imshow(image_eq)
        plt.colorbar()
        fileNameOutput = fileNameOutput[:-3]
        # plt.savefig([fileNameOutput, 'bmp'])
        plt.show()
    text2.insert(INSERT, 'Готово')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.geometry('1100x100')
    window.title("Fluorescence Ratiometric Imager")

    lbl0 = Label(window, text="Выбор флуоресцентных картинок")
    lbl0.grid(column=0, row=1)
    lbl1 = Label(window, text="Выбор цветных картинок")
    lbl1.grid(column=0, row=2)
    lbl2 = Label(window, text="Сгенерить вывод!")
    lbl2.grid(column=0, row=3)


    text0 = Text(width=7, height=1)
    text0.grid(column=2, row=1, sticky=(W))
    text1 = Text(width=7, height=1)
    text1.grid(column=2, row=2, sticky=(W))
    text2 = Text(width=7, height=1)
    text2.grid(column=2, row=3, sticky=(W))
    # text0.pack()

    btn0 = Button(window, text="Выбрать", command=selectFluorescentImages)
    btn0.grid(column=1, row=1)
    btn1 = Button(window, text="Выбрать", command=selectColorImages)
    btn1.grid(column=1, row=2)
    btn2 = Button(window, text="Сгенерить", command=Generator)
    btn2.grid(column=1, row=3)

    window.mainloop()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

