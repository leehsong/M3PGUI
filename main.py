from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
import cv2
#from matplotlib import pyplot as plt
import numpy as np
import sys
import M3PGUI
import parse
import os

class M3PAIApp(QtWidgets.QMainWindow, M3PGUI.Ui_MainWindow):
    ratio = 1.0
    image = cv2.imread('web.png', cv2.IMREAD_COLOR)
    Xcutlines = []
    Ycutlines = []
    subimages = []
    def __init__(self, parent=None):
        super(M3PAIApp, self).__init__(parent)
        self.entry = QtGui.QStandardItemModel()
        self.setupUi(self)
        self.pushButton_Analysis.clicked.connect(self.btnAnalysis)
        self.pushButton_CutImage.clicked.connect(self.btnCutImage)
        self.pushButton_Refresh.clicked.connect(self.btnSave)
        self.listView.clicked[QtCore.QModelIndex].connect(self.on_listclicked)
        self.listView.doubleClicked[QtCore.QModelIndex].connect(self.on_listdoubleclicked)
        self.listView.setModel(self.entry)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.actionOpen.triggered.connect(self.menuOpen)
        self.actionExit.triggered.connect(QCoreApplication.instance().quit)
        scene = QtWidgets.QGraphicsScene(self)
        pixmap = QPixmap("web.png")
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.graphicsView.setScene(scene)

        for text in ["SUB Images"]:
            it = QtGui.QStandardItem(text)
            self.entry.appendRow(it)
        self.itemOld = QtGui.QStandardItem("text")
        self.textEdit.append("============================")
        self.textEdit.append("Start M3P AI program")
        self.textEdit.append("============================")

    def writeLog1(self, text):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        print("date and time:", date_time)
        self.textEdit.append("[{T}], {str}".format(T=date_time, str=text))

    def menuOpen(self):
        self.writeLog1("Open Button")
        fname = QFileDialog.getOpenFileName(self, 'Open file','', "Image files (*.jpg *.gif *.png)")

        print(fname)
        scene = QtWidgets.QGraphicsScene(self)

        img = cv2.imread(fname[0], cv2.IMREAD_COLOR)
        finalname = fname[0]

        height, width, channels = img.shape
        if height > 600:
            ratio = 0.5
            img_small = cv2.resize(img, dsize=(int(width*ratio), int(height*ratio)), interpolation=cv2.INTER_AREA)
            finalname ='m3p_test_small.png'
            cv2.imwrite(finalname,img_small)

        pixmap = QPixmap(finalname)
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.graphicsView.setScene(scene)

        self.image = img
        print("Menu Open Clicked")

    def btnAnalysis(self):
        self.writeLog1("Analysis Image")
        img = self.image
        print(img)
        img_cutline = img

        height, width, channels = img.shape
        self.Xcutlines = [width]
        self.Ycutlines = [height]
        print("TESTED")
        print(height)
        Columns = 20
        Rows = 20
        for i in range(1, Columns):
            for j in range(1, Rows):
                print('Count Down', i, j)
                x = int(width * i / Columns)
                y = int(height * j / Rows)
                self.Xcutlines.append(x)
                self.Ycutlines.append(y)
 #               img_cutline[:, (x - 1):(x + 1), 0:2] = 0
 #               img_cutline[(y - 1):(y + 1), :, 0:2] = 0
                print("Lines", x, y)

        finalname = 'M3P_array_line.png'
        cv2.imwrite(finalname, img_cutline)
        scene = QtWidgets.QGraphicsScene(self)
        pixmap = QPixmap(finalname)
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)

        self.Ycutlines = list(set(self.Ycutlines))
        self.Xcutlines = list(set(self.Xcutlines))
        self.Xcutlines.sort()
        self.Ycutlines.sort()

        self.graphicsView.setScene(scene)

    def btnCutImage(self):
        self.writeLog1("Cut Image")
        print(self.Xcutlines)
        print(self.Ycutlines)
        x0 = 0
        dx0 = 0
        y0 = 0
        dy0 = 0
        for x in self.Xcutlines:
            dx = x-x0
            dx0 = max(x-x0, dx0)
            x0 =x
        for y in self.Ycutlines:
            dy = y- y0
            dy0 = max(y-y0, dy0)
            y0 =y
        print(dx0, dy0)
        x0 = 0
        y0 = 0
        A = 0
        B = 0
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10, 30)
        fontScale = 1.0
        fontColor = (255, 255, 255)
        lineType = 2

        for x in self.Xcutlines:
            for y in self.Ycutlines:
                subimage = self.image[y0:y0+dy0, x0:x0+dx0, 0:3]
                key = "{keyA}-{keyB}".format(keyA=A, keyB=B)
  #             cv2.putText(subimage, key, bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
                A = A+1
                y0 = y
                self.subimages.append({'name':key, 'image':subimage})
            y0 =0
            A = 0
            B = B + 1
            x0 = x

        for key in self.subimages:
            it = QtGui.QStandardItem(key['name'])
            self.entry.appendRow(it)

    def on_listdoubleclicked(self, index):
        item = self.entry.itemFromIndex(index)
        self.writeLog1("on_double clicked: Image   :   "+item.text())
        print(item)
        print("on_doubleclicked: itemIndex=`{}`, itemText=`{}`".format(item.index().row(), item.text()))
        item.setForeground(QBrush(QColor(255, 0, 0)))
        self.itemOld.setForeground(QBrush(QColor(0, 0, 0)))
        self.itemOld = item


    def on_listclicked(self, index):
        item = self.entry.itemFromIndex(index)
        self.writeLog1("on_clicked: Image   :   "+item.text())
        print(item)
        print("on_clicked: itemIndex=`{}`, itemText=`{}`".format(item.index().row(), item.text()))
        if self.itemOld == item:
            self.on_listdoubleclicked(index)
            return
        item.setForeground(QBrush(QColor(255, 0, 0)))
        self.itemOld.setForeground(QBrush(QColor(0, 0, 0)))
        self.itemOld = item

        ## Image Update
        SelectedImage = []
        for subimage in self.subimages:
            if subimage["name"] == item.text():
                print("Selected")
                SelectedImage.append(subimage)
            else:
                print("No Selection", subimage['name'])
        print(SelectedImage)
        if len(SelectedImage) > 0 :
            finalname = 'item_selected.png'
            cv2.imwrite(finalname, SelectedImage[0]['image'])
            scene = QtWidgets.QGraphicsScene(self)
            pixmap = QPixmap(finalname)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            self.graphicsView.setScene(scene)


    def btnSave(self):
 #       if os.path.isdir('subimages') == 0:
 #           os.mkdir('subimages')
 #           os.mkdir('subimages\\3')
 #           os.mkdir('subimages\\4')
 #           os.mkdir('subimages\\5')
 #           os.mkdir('subimages\\6')
 #           os.mkdir('subimages\\20')

        ShapeLoad = np.load('S20_T5_R5000.npz')
        print("==============btnSave===============")
        print(ShapeLoad['Size'])
        print("==============Shape===============")
        print(ShapeLoad['Shape'])
        self.writeLog1("Button Save clicked ")
        for key in self.subimages:
            print("==============Loop===============")
            it = key['name']
            print("==============keycheck===============", it)
            result = parse.parse("{}-{}", it)
            xindex = int(result[0])
            yindex = int(result[1])
            print("==============Index===============", xindex, yindex)
            subfolder = int(ShapeLoad['Shape'][xindex][yindex])
            print(subfolder)
            filename = "subimages\\{shape}\\{fname}.png".format(shape=subfolder,fname=it)
            print(filename)
            cv2.imwrite(filename, key['image'])

def main():
    app = QApplication(sys.argv)
    form = M3PAIApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()