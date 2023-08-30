# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainRBzMXR.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(600, 450))
        MainWindow.setMaximumSize(QSize(600, 450))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(600, 450))
        self.centralwidget.setMaximumSize(QSize(600, 450))
        self.centralwidget.setStyleSheet(u"background: #91D8E4;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Montserrat")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:#0A2647")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.max_chamber_edit = QTextEdit(self.frame)
        self.max_chamber_edit.setObjectName(u"max_chamber_edit")
        self.max_chamber_edit.setMaximumSize(QSize(200, 50))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(18)
        self.max_chamber_edit.setFont(font1)
        self.max_chamber_edit.setStyleSheet(u"color:#205295;\n"
"border: 2px solid #EAFDFC;")
        self.max_chamber_edit.setLineWidth(1)
        self.max_chamber_edit.setLineWrapMode(QTextEdit.NoWrap)

        self.horizontalLayout.addWidget(self.max_chamber_edit)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"Montserrat")
        font2.setPointSize(9)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color:#0A2647")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 80))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"color:#0A2647")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_15)

        self.max_chamber_pos_edit = QTextEdit(self.frame_4)
        self.max_chamber_pos_edit.setObjectName(u"max_chamber_pos_edit")
        self.max_chamber_pos_edit.setMaximumSize(QSize(200, 50))
        self.max_chamber_pos_edit.setFont(font1)
        self.max_chamber_pos_edit.setStyleSheet(u"color:#205295;\n"
"border: 2px solid #EAFDFC;")

        self.horizontalLayout_3.addWidget(self.max_chamber_pos_edit)

        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"color:#0A2647")

        self.horizontalLayout_3.addWidget(self.label_16)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color:#0A2647")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.thickness_edit = QTextEdit(self.frame_2)
        self.thickness_edit.setObjectName(u"thickness_edit")
        self.thickness_edit.setMaximumSize(QSize(200, 50))
        self.thickness_edit.setFont(font1)
        self.thickness_edit.setStyleSheet(u"color:#205295;\n"
"border: 2px solid #EAFDFC;")

        self.horizontalLayout_2.addWidget(self.thickness_edit)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"color:#0A2647")

        self.horizontalLayout_2.addWidget(self.label_10)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color:#0A2647")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_13)

        self.no_of_points_edit = QTextEdit(self.frame_3)
        self.no_of_points_edit.setObjectName(u"no_of_points_edit")
        self.no_of_points_edit.setMaximumSize(QSize(200, 50))
        self.no_of_points_edit.setFont(font1)
        self.no_of_points_edit.setStyleSheet(u"color:#205295;\n"
"border: 2px solid #EAFDFC;")

        self.horizontalLayout_4.addWidget(self.no_of_points_edit)

        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color:#0A2647")

        self.horizontalLayout_4.addWidget(self.label_14)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.plot_button = QPushButton(self.frame_5)
        self.plot_button.setObjectName(u"plot_button")
        sizePolicy1.setHeightForWidth(self.plot_button.sizePolicy().hasHeightForWidth())
        self.plot_button.setSizePolicy(sizePolicy1)
        self.plot_button.setMinimumSize(QSize(0, 50))
        self.plot_button.setMaximumSize(QSize(120, 50))
        font3 = QFont()
        font3.setFamily(u"Montserrat SemiBold")
        font3.setPointSize(15)
        self.plot_button.setFont(font3)
        self.plot_button.setStyleSheet(u"QPushButton {\n"
"	border-radius : 20; \n"
"	border : 2px solid #0A2647;\n"
"	color:#0A2647\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #0A2647;\n"
"	color: #91D8E4;\n"
"}")
        self.plot_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.plot_button)


        self.verticalLayout.addWidget(self.frame_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Max Chamber (%)", None))
        self.max_chamber_edit.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"First digit. 0 to 9.5%", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Max camber position (%)", None))
        self.max_chamber_pos_edit.setPlaceholderText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Second digit. 0 to 90%", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Thickness", None))
        self.thickness_edit.setPlaceholderText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Third & fourth digit. \n"
"1 to 40%", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Number of points", None))
        self.no_of_points_edit.setPlaceholderText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"20 to 200", None))
        self.plot_button.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
    # retranslateUi

