import sys
from PySide2.QtWidgets import *
from PySide2 import QtGui
import math
import matplotlib.pyplot as plt
import numpy as np
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('plane.png'))
        self.setWindowTitle('NACA 2412 Airfoil Generator')

        self.ui.max_chamber_edit.setText("2")
        self.ui.max_chamber_pos_edit.setText("40")
        self.ui.thickness_edit.setText("40")
        self.ui.no_of_points_edit.setText("81")
        
        self.ui.plot_button.clicked.connect(lambda: self.plot())
        self.show()

    def plot(self):
        try:
            m = float(self.ui.max_chamber_edit.toPlainText()) / 100
            p = float(self.ui.max_chamber_pos_edit.toPlainText()) / 100
            t = float(self.ui.thickness_edit.toPlainText()) / 100
            n = int(self.ui.no_of_points_edit.toPlainText())

            if m < 0 or m > 0.095 or p < 0 or p > 0.9 or t < 0.01 or t > 0.4 or n < 20 or n > 200:
                err = QMessageBox()
                err.setIcon(QMessageBox.Critical)
                err.setText("Error")
                err.setInformativeText('Please Enter the Right Values')
                err.setWindowTitle("Wrong Values")
                err.setWindowIcon(QtGui.QIcon('error.png'))
                err.exec_()
            else:
                plt.close()
                x = np.linspace(0,1,n)
                for item in naca4(x, m, p, t):
                    plt.plot(item[0], item[1], 'b')

                plt.plot(x, camber_line(x, m, p), 'r')
                plt.show()
        except:
            err = QMessageBox()
            err.setIcon(QMessageBox.Critical)
            err.setText("Error")
            err.setInformativeText('Please Enter the Right DataType')
            err.setWindowTitle("Wrong DataType")
            err.setWindowIcon(QtGui.QIcon('error.png'))
            err.exec_()


def camber_line( x, m, p, c=1 ):
    return np.where((x>=0)&(x<=(c*p)),
                    m * (x / np.power(p,2)) * (2.0 * p - (x / c)),
                    m * ((c - x) / np.power(1-p,2)) * (1.0 + (x / c) - 2.0 * p ))

def dyc_over_dx( x, m, p, c=1 ):
    return np.where((x>=0)&(x<=(c*p)),
                    ((2.0 * m) / np.power(p,2)) * (p - x / c),
                    ((2.0 * m ) / np.power(1-p,2)) * (p - x / c ))

def thickness( x, t, c ):
    term1 =  0.2969 * (np.sqrt(x/c))
    term2 = -0.1260 * (x/c)
    term3 = -0.3516 * np.power(x/c,2)
    term4 =  0.2843 * np.power(x/c,3)
    term5 = -0.1015 * np.power(x/c,4)
    return 5 * t * c * (term1 + term2 + term3 + term4 + term5)

def naca4(x, m, p, t, c=1):
    dyc_dx = dyc_over_dx(x, m, p, c)
    th = np.arctan(dyc_dx)
    yt = thickness(x, t, c)
    yc = camber_line(x, m, p, c)  
    return ((x - yt*np.sin(th), yc + yt*np.cos(th)), 
            (x + yt*np.sin(th), yc - yt*np.cos(th)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
