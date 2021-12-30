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
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView
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
        self.ion_label.resize(90,40)
        
        
        # ion textbox
        self.ion = QLineEdit(self)
        self.ion.move(80, 20)
        self.ion.resize(40,40)
        
        
        # L label
        self.L_label = QLabel('L:',self)
        self.L_label.move(20,60)
        self.L_label.resize(80,40)
        
        
        # L textbox
        self.L = QLineEdit(self)
        self.L.move(80, 60)
        self.L.resize(40,40)
        
        # S label
        self.S_label = QLabel('S:',self)
        self.S_label.move(20,100)
        self.S_label.resize(80,40)
        
        
        # S textbox
        self.S = QLineEdit(self)
        self.S.move(80, 100)
        self.S.resize(40,40)
        
        
        # Z label
        self.Z_label = QLabel('Z:',self)
        self.Z_label.move(20,140)
        self.Z_label.resize(80,40)
        
        
        # Z textbox
        self.Z = QLineEdit(self)
        self.Z.move(80, 140)
        self.Z.resize(40,40)
        
        
        # SO label
        self.SO_label = QLabel('Spin-Orbit (meV):',self)
        self.SO_label .move(20,180)
        self.SO_label .resize(160,40)
        
        
        # SO textbox
        self.SO = QLineEdit(self)
        self.SO.move(160, 180)
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
        
        
        
        # B parameters label
        self.B_parameters_label = QLabel('B parameters',self)
        self.B_parameters_label .move(400,20)
        self.B_parameters_label .resize(200,40)
        # Create a table for B parameters
        self.B_parameters = QTableWidget(self)
        self.B_parameters.move(400 , 50)
        self.B_parameters.resize(300,400)
        self.B_parameters.setRowCount(8)
        self.B_parameters.setColumnCount(2)
        self.B_parameters.setItem(0,0, QTableWidgetItem("B20 (meV)"))
        self.B_parameters.setItem(1,0, QTableWidgetItem("B21 (meV)"))
        self.B_parameters.setItem(2,0, QTableWidgetItem("B22 (meV)"))
        self.B_parameters.setItem(3,0, QTableWidgetItem("B40 (meV)"))
        self.B_parameters.setItem(4,0, QTableWidgetItem("B41 (meV)"))
        self.B_parameters.setItem(5,0, QTableWidgetItem("B42 (meV)"))
        self.B_parameters.setItem(6,0, QTableWidgetItem("B43 (meV)"))
        self.B_parameters.setItem(7,0, QTableWidgetItem("B44 (meV)"))
        
        self.B_parameters.horizontalHeader().setStretchLastSection(True)
        self.B_parameters.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.B_parameters.verticalHeader().setStretchLastSection(True)
        self.B_parameters.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)




        
        
        # Energies label
        self.Energies_label = QLabel('Energies',self)
        self.Energies_label .move(800,20)
        self.Energies_label .resize(100,40)
        # Create a table for Energies
        self.Energies = QTableWidget(self)
        self.Energies.move(800 , 50)
        self.Energies.resize(200,400)
        self.Energies.setRowCount(1)
        self.Energies.setColumnCount(1)
        self.Energies.setUpdatesEnabled(True)
        
        self.Energies.horizontalHeader().setStretchLastSection(True)
        self.Energies.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.Energies.verticalHeader().setStretchLastSection(True)
        self.Energies.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        
        
        # Energies + SO label
        self.Energies_SO_label = QLabel('Energies + SO',self)
        self.Energies_SO_label .move(1100,20)
        self.Energies_SO_label .resize(100,40)
        # Create a table for Energies
        self.Energies_SO = QTableWidget(self)
        self.Energies_SO.move(1100 , 50)
        self.Energies_SO.resize(200,400)
        self.Energies_SO.setRowCount(1)
        self.Energies_SO.setColumnCount(1)
        self.Energies_SO.setUpdatesEnabled(True)

        
        self.Energies_SO.horizontalHeader().setStretchLastSection(True)
        self.Energies_SO.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.Energies_SO.verticalHeader().setStretchLastSection(True)
        self.Energies_SO.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        
        
        self.show()
        
        

    @pyqtSlot()
    def on_click(self):
        ion_text = self.ion.text()
        L_text = self.L.text()
        S_text = self.S.text()
        Z_text = self.Z.text()
        SO_text = self.SO.text()
        QMessageBox.question(self, 'Crystal Field', "You typed: ion = " + ion_text +\
        ", L = " + L_text + ", S = " + S_text + ", Z = " + Z_text + ", SO = " +\
        SO_text, QMessageBox.Ok, QMessageBox.Ok)
        #self.ion.setText("")
        
        ion = ion_text
        L = int(L_text)
        S = int(S_text)
        Z = int(Z_text)
        calc = cef.LS(L,S)
        Degeneracy = L*S
        
        O20 = calc.Olm(L,S,2,0)
        O21 = calc.Olm(L,S,2,1)
        O22 = calc.Olm(L,S,2,2)
        O40 = calc.Olm(L,S,4,0)
        O41 = calc.Olm(L,S,4,1)
        O42 = calc.Olm(L,S,4,2)
        O43 = calc.Olm(L,S,4,3)
        O44 = calc.Olm(L,S,4,4)
        
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
        
        QMessageBox.question(self, 'Crystal Field', 'Results are down below' +\
        '\n B20: ' + str(B[0]) +\
        '\n B21: ' + str(B[1]) +\
        '\n B22: ' + str(B[2]) +\
        '\n B40: ' + str(B[3]) +\
        '\n B41: ' + str(B[4]) +\
        '\n B42: ' + str(B[5]) +\
        '\n B43: ' + str(B[6]) +\
        '\n B44: ' + str(B[7]), QMessageBox.Ok, QMessageBox.Ok)

        self.B_parameters.setItem(0,1, QTableWidgetItem(str(B[0])))
        self.B_parameters.setItem(1,1, QTableWidgetItem(str(B[1])))
        self.B_parameters.setItem(2,1, QTableWidgetItem(str(B[2])))
        self.B_parameters.setItem(3,1, QTableWidgetItem(str(B[3])))
        self.B_parameters.setItem(4,1, QTableWidgetItem(str(B[4])))
        self.B_parameters.setItem(5,1, QTableWidgetItem(str(B[5])))
        self.B_parameters.setItem(6,1, QTableWidgetItem(str(B[6])))
        self.B_parameters.setItem(7,1, QTableWidgetItem(str(B[7])))

        
        Hcf = B[0]*O20 + B[1]*O21 + B[2]*O22 + B[3]*O40 + B[4]*O41 + B[5]*O42 + B[6]*O43 + B[7]*O44
        Ecf_val,Ecf_val_excitation,H_cf_vt = calc.Diag(Hcf,printfunction=True)
        SO_matrix = calc.SO(ion,L,S,self.SO)
        Hcf_so = Hcf + SO_matrix
        Ecf_so_val,Ecf_so_val_excitation,H_cf_so_vt = calc.Diag(Hcf_so,printfunction=True)
        
        self.Energies.setRowCount(len(Degeneracy))
        self.Energies_SO.setRowCount(len(Degeneracy))
        
        for k in range(len(Degeneracy)):
            self.Energies.setItem(k,0, QTableWidgetItem(str(Ecf_val_excitation[k])))
            self.Energies_SO.setItem(k,0, QTableWidgetItem(str(Ecf_so_val_excitation[k])))

        



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


