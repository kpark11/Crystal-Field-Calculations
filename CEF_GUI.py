# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 17:18:53 2021

@author: brian
"""
import Crystal_Field_Calcuations as cef
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPalette
import sys
import numpy as np




class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Crystal Field Calculation'
        self.left = 110
        self.top = 110
        self.width = 1400
        self.height = 840
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        
        # ion label
        self.ion_label = QLabel('Ion:',self)
        self.ion_label.move(20,20)
        self.ion_label.resize(40,40)
        
        
        # ion textbox
        self.ion = QLineEdit(self)
        self.ion.move(60, 20)
        self.ion.resize(40,40)
        
        
        # L label
        self.L_label = QLabel('L:',self)
        self.L_label.move(20,60)
        self.L_label.resize(40,40)
        
        
        # L textbox
        self.L = QLineEdit(self)
        self.L.move(60, 60)
        self.L.resize(40,40)
        
        # S label
        self.S_label = QLabel('S:',self)
        self.S_label.move(20,100)
        self.S_label.resize(40,40)
        
        
        # S textbox
        self.S = QLineEdit(self)
        self.S.move(60, 100)
        self.S.resize(40,40)
        
        
        # Z label
        self.Z_label = QLabel('Z:',self)
        self.Z_label.move(20,140)
        self.Z_label.resize(40,40)
        
        
        # Z textbox
        self.Z = QLineEdit(self)
        self.Z.move(60, 140)
        self.Z.resize(40,40)
        
        
        # SO label
        self.SO_label = QLabel('Spin-Orbit (meV):',self)
        self.SO_label .move(20,180)
        self.SO_label .resize(110,40)
        
        
        # SO textbox
        self.SO = QLineEdit(self)
        self.SO.move(140, 180)
        self.SO.resize(40,40)
        
        
        # Ion_position label
        self.Ion_position = QLabel('Ion_position (x,y,z):',self)
        self.Ion_position .move(20,240)
        self.Ion_position .resize(110,40)
        
        
        # Ion_position textbox for x
        self.Ion_position_x = QLineEdit(self)
        self.Ion_position_x.move(140, 240)
        self.Ion_position_x.resize(40,40)
        # Ion_position textbox for y
        self.Ion_position_y = QLineEdit(self)
        self.Ion_position_y.move(180, 240)
        self.Ion_position_y.resize(40,40)
        # Ion_position textbox for z
        self.Ion_position_z = QLineEdit(self)
        self.Ion_position_z.move(220, 240)
        self.Ion_position_z.resize(40,40)
        
        
        # Ligand 1 label
        self.Li1 = QLabel('Ligand 1 (x,y,z):',self)
        self.Li1 .move(20,280)
        self.Li1 .resize(110,40)
        
        
        # Ligand 1 textbox for x
        self.Li1_x = QLineEdit(self)
        self.Li1_x.move(140, 280)
        self.Li1_x.resize(40,40)
        # Ligand 1 textbox for y
        self.Li1_y = QLineEdit(self)
        self.Li1_y.move(180, 280)
        self.Li1_y.resize(40,40)
        # Ligand 1 textbox for z
        self.Li1_z = QLineEdit(self)
        self.Li1_z.move(220, 280)
        self.Li1_z.resize(40,40)
        
        
        # Ligand 2 label
        self.Li2 = QLabel('Ligand 2 (x,y,z):',self)
        self.Li2 .move(20,320)
        self.Li2 .resize(110,40)
        
        
        # Ligand 2 textbox for x
        self.Li2_x = QLineEdit(self)
        self.Li2_x.move(140, 320)
        self.Li2_x.resize(40,40)
        # Ligand 2 textbox for y
        self.Li2_y = QLineEdit(self)
        self.Li2_y.move(180, 320)
        self.Li2_y.resize(40,40)
        # Ligand 2 textbox for z
        self.Li2_z = QLineEdit(self)
        self.Li2_z.move(220, 320)
        self.Li2_z.resize(40,40)
        
        
        # Ligand 3 label
        self.Li3 = QLabel('Ligand 3 (x,y,z):',self)
        self.Li3 .move(20,360)
        self.Li3 .resize(110,40)
        
        
        # Ligand 3 textbox for x
        self.Li3_x = QLineEdit(self)
        self.Li3_x.move(140, 360)
        self.Li3_x.resize(40,40)
        # Ligand 3 textbox for y
        self.Li3_y = QLineEdit(self)
        self.Li3_y.move(180, 360)
        self.Li3_y.resize(40,40)
        # Ligand 3 textbox for z
        self.Li3_z = QLineEdit(self)
        self.Li3_z.move(220, 360)
        self.Li3_z.resize(40,40)
        
        
        
        # Ligand 4 label
        self.Li4 = QLabel('Ligand 4 (x,y,z):',self)
        self.Li4 .move(20,400)
        self.Li4 .resize(110,40)
        
        
        # Ligand 4 textbox for x
        self.Li4_x = QLineEdit(self)
        self.Li4_x.move(140, 400)
        self.Li4_x.resize(40,40)
        # Ligand 4 textbox for y
        self.Li4_y = QLineEdit(self)
        self.Li4_y.move(180, 400)
        self.Li4_y.resize(40,40)
        # Ligand 4 textbox for z
        self.Li4_z = QLineEdit(self)
        self.Li4_z.move(220, 400)
        self.Li4_z.resize(40,40)
        
        
        # Ligand 5 label
        self.Li5 = QLabel('Ligand 5 (x,y,z):',self)
        self.Li5 .move(20,440)
        self.Li5 .resize(110,40)
        
        
        # Ligand 5 textbox for x
        self.Li5_x = QLineEdit(self)
        self.Li5_x.move(140, 440)
        self.Li5_x.resize(40,40)
        # Ligand 5 textbox for y
        self.Li5_y = QLineEdit(self)
        self.Li5_y.move(180, 440)
        self.Li5_y.resize(40,40)
        # Ligand 5 textbox for z
        self.Li5_z = QLineEdit(self)
        self.Li5_z.move(220, 440)
        self.Li5_z.resize(40,40)
        
        
        # Ligand 6 label
        self.Li6 = QLabel('Ligand 6 (x,y,z):',self)
        self.Li6 .move(20,480)
        self.Li6 .resize(110,40)
        
        
        # Ligand 6 textbox for x
        self.Li6_x = QLineEdit(self)
        self.Li6_x.move(140, 480)
        self.Li6_x.resize(40,40)
        # Ligand 6 textbox for y
        self.Li6_y = QLineEdit(self)
        self.Li6_y.move(180, 480)
        self.Li6_y.resize(40,40)
        # Ligand 6 textbox for z
        self.Li6_z = QLineEdit(self)
        self.Li6_z.move(220, 480)
        self.Li6_z.resize(40,40)
        
        
        
        # Ligand 7 label
        self.Li7 = QLabel('Ligand 7 (x,y,z):',self)
        self.Li7 .move(20,520)
        self.Li7 .resize(110,40)
        
        
        # Ligand 7 textbox for x
        self.Li7_x = QLineEdit(self)
        self.Li7_x.move(140, 520)
        self.Li7_x.resize(40,40)
        # Ligand 7 textbox for y
        self.Li7_y = QLineEdit(self)
        self.Li7_y.move(180, 520)
        self.Li7_y.resize(40,40)
        # Ligand 7 textbox for z
        self.Li7_z = QLineEdit(self)
        self.Li7_z.move(220, 520)
        self.Li7_z.resize(40,40)
        
        
        # Ligand 8 label
        self.Li8 = QLabel('Ligand 8 (x,y,z):',self)
        self.Li8 .move(20,560)
        self.Li8 .resize(110,40)
        
        
        # Ligand 8 textbox for x
        self.Li8_x = QLineEdit(self)
        self.Li8_x.move(140, 560)
        self.Li8_x.resize(40,40)
        # Ligand 8 textbox for y
        self.Li8_y = QLineEdit(self)
        self.Li8_y.move(180, 560)
        self.Li8_y.resize(40,40)
        # Ligand 8 textbox for z
        self.Li8_z = QLineEdit(self)
        self.Li8_z.move(220, 560)
        self.Li8_z.resize(40,40)
        
        
        
        
        
        
        # Create a button in the window
        self.calculate = QPushButton('Calculate', self)
        self.calculate.move(120,620)
        
        
        # connect button to function on_click
        self.calculate.clicked.connect(self.on_click)
        self.show()
    
    
    @pyqtSlot()
    def on_click(self):
        ion_text = self.ion.text()
        L_text = self.L.text()
        S_text = self.S.text()
        Z_text = self.Z.text()
        SO_text = self.SO.text()
        QMessageBox.question(self, 'Crystal Field', "You typed: ion = " + ion_text + ", L = " + L_text + ", S = " + S_text + ", Z = " + Z_text + ", SO = " + SO_text, QMessageBox.Ok, QMessageBox.Ok)
        #self.ion.setText("")
        
        ion = ion_text
        L = int(L_text)
        S = int(S_text)
        Z = int(Z_text)
        calc = cef.LS(L,S)
        
        
        ion_center = np.array([float(self.Ion_position_x.text()),    float(self.Ion_position_y.text()),    float(self.Ion_position_z.text())])
        O1 = np.array([float(self.Li1_x.text()),    float(self.Li1_y.text()),   float(self.Li1_z.text())])
        O2 = np.array([float(self.Li2_x.text()),    float(self.Li2_y.text()),   float(self.Li2_z.text())])
        O3 = np.array([float(self.Li3_x.text()),   float(self.Li3_y.text()),   float(self.Li3_z.text())])
        O4 = np.array([float(self.Li4_x.text()),    float(self.Li4_y.text()),    float(self.Li4_z.text())])
        O5 = np.array([float(self.Li5_x.text()),    float(self.Li5_y.text()),   float(self.Li5_z.text())])
        O6 = np.array([float(self.Li6_x.text()),    float(self.Li6_y.text()),    float(self.Li6_z.text())])
        O7 = np.array([float(self.Li7_x.text()),    float(self.Li7_y.text()),  float(self.Li7_z.text())])
        O8 = np.array([float(self.Li8_x.text()),    float(self.Li8_y.text()), float(self.Li8_z.text())])
        
        
        O1_d = O1 - ion_center
        O2_d = O2 - ion_center
        O3_d = O3 - ion_center
        O4_d = O4 - ion_center
        O5_d = O5 - ion_center
        O6_d = O6 - ion_center
        O7_d = O7 - ion_center
        O8_d = O8 - ion_center
        
        d = np.array([O1_d,O2_d,O3_d,O4_d,O5_d,O6_d,O7_d,O8_d])
        B = calc.PC(ion,L,S,d,Z)
        
        QMessageBox.question(self, 'Crystal Field', "Finished calculation! Here are the B: " + B, QMessageBox.Ok, QMessageBox.Ok)

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # setting the colors
    palette = QPalette()
    palette.setColor(QPalette.Window, Qt.lightGray)
    palette.setColor(QPalette.ButtonText, Qt.red)
    palette.setColor(QPalette.WindowText, Qt.darkGreen)
    app.setPalette(palette)
    ex = App()
    
    sys.exit(app.exec_())


