# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:38:47 2020

@author: Artur Movsessian

"""
import sys
import PyQt5.QtCore as core
import PyQt5.QtWidgets as widgets
import PyQt5.QtGui as gui
import PyQt5.uic as uic
import numpy as np
import pandas as pd

import pandas as pd
data = pd.read_csv("DTU_Data_n.txt")

app = widgets.QApplication(sys.argv)
w = uic.loadUi("MainWindow.ui")

def openfiledialog():
    fname = widgets.QFileDialog.getOpenFileName(None, 'Open file', 'C:\\Users\Artur\OneDrive - University of Edinburgh\ML Application\MyGui', "Image files (*.csv *.txt *.mat)")
    global data
#    print(type(fname))
#    print(fname[0])
    data = pd.read_csv(fname[0])
    #print(data)


w.LoadData.clicked.connect(openfiledialog)
def check_button():
    if w.pushButton1.isEnabled():
        print('enabled')
        try:
            print(data)
        except:
            print("No data avalible")
        w.pushButton1.setEnabled(True)
    else:
        print('not enabled')
        w.pushButton1.setEnabled(True)


w.pushButton1.clicked.connect(check_button)

w.show()
sys.exit(app.exec_())


