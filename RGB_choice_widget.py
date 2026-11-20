# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RGB_choice_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QVBoxLayout, QWidget)
import lumos_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(300, 540))
        Form.setMaximumSize(QSize(410, 650))
        Form.setStyleSheet(u"background: url(:/backgrounds/assets/backgrounds/wall_bcg.png);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"color: white;\n"
"padding: 10px 10px;")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.GlobalFrame = QFrame(Form)
        self.GlobalFrame.setObjectName(u"GlobalFrame")
        self.GlobalFrame.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.GlobalFrame)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.rgb_circle = QLabel(self.GlobalFrame)
        self.rgb_circle.setObjectName(u"rgb_circle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rgb_circle.sizePolicy().hasHeightForWidth())
        self.rgb_circle.setSizePolicy(sizePolicy1)
        self.rgb_circle.setStyleSheet(u"background: none;\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.7 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius: 100px;")

        self.verticalLayout_5.addWidget(self.rgb_circle)

        self.frame = QFrame(self.GlobalFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background: none;\n"
"padding: 0px 0px;")
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(2)
        self.Red = QFrame(self.frame)
        self.Red.setObjectName(u"Red")
        self.Red.setStyleSheet(u"background: none;")
        self.verticalLayout_4 = QVBoxLayout(self.Red)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 1)
        self.RedSlider = QSlider(self.Red)
        self.RedSlider.setObjectName(u"RedSlider")
        sizePolicy1.setHeightForWidth(self.RedSlider.sizePolicy().hasHeightForWidth())
        self.RedSlider.setSizePolicy(sizePolicy1)
        self.RedSlider.setLayoutDirection(Qt.LeftToRight)
        self.RedSlider.setAutoFillBackground(False)
        self.RedSlider.setStyleSheet(u"background-color: none;")
        self.RedSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_4.addWidget(self.RedSlider, 0, Qt.AlignHCenter)

        self.RedLable = QLabel(self.Red)
        self.RedLable.setObjectName(u"RedLable")
        self.RedLable.setStyleSheet(u"background-color: none;")
        self.RedLable.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.RedLable)

        self.RedSpinBox = QSpinBox(self.Red)
        self.RedSpinBox.setObjectName(u"RedSpinBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.RedSpinBox.sizePolicy().hasHeightForWidth())
        self.RedSpinBox.setSizePolicy(sizePolicy2)
        self.RedSpinBox.setLayoutDirection(Qt.LeftToRight)
        self.RedSpinBox.setAutoFillBackground(False)
        self.RedSpinBox.setStyleSheet(u"background-color: none;\n"
"color: black;")
        self.RedSpinBox.setWrapping(False)
        self.RedSpinBox.setFrame(False)
        self.RedSpinBox.setAlignment(Qt.AlignCenter)
        self.RedSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.RedSpinBox.setAccelerated(False)

        self.verticalLayout_4.addWidget(self.RedSpinBox)


        self.gridLayout_2.addWidget(self.Red, 0, 0, 1, 1)

        self.Green = QFrame(self.frame)
        self.Green.setObjectName(u"Green")
        self.Green.setStyleSheet(u"background: none;")
        self.verticalLayout_7 = QVBoxLayout(self.Green)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 1)
        self.GreenlSlider = QSlider(self.Green)
        self.GreenlSlider.setObjectName(u"GreenlSlider")
        sizePolicy1.setHeightForWidth(self.GreenlSlider.sizePolicy().hasHeightForWidth())
        self.GreenlSlider.setSizePolicy(sizePolicy1)
        self.GreenlSlider.setLayoutDirection(Qt.LeftToRight)
        self.GreenlSlider.setAutoFillBackground(False)
        self.GreenlSlider.setStyleSheet(u"background-color: none;")
        self.GreenlSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_7.addWidget(self.GreenlSlider, 0, Qt.AlignHCenter)

        self.GreeenLable = QLabel(self.Green)
        self.GreeenLable.setObjectName(u"GreeenLable")
        self.GreeenLable.setStyleSheet(u"background-color: none;")
        self.GreeenLable.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.GreeenLable)

        self.GreenSpinBox = QSpinBox(self.Green)
        self.GreenSpinBox.setObjectName(u"GreenSpinBox")
        sizePolicy2.setHeightForWidth(self.GreenSpinBox.sizePolicy().hasHeightForWidth())
        self.GreenSpinBox.setSizePolicy(sizePolicy2)
        self.GreenSpinBox.setLayoutDirection(Qt.LeftToRight)
        self.GreenSpinBox.setAutoFillBackground(False)
        self.GreenSpinBox.setStyleSheet(u"background-color: none;\n"
"color: black;")
        self.GreenSpinBox.setWrapping(False)
        self.GreenSpinBox.setFrame(False)
        self.GreenSpinBox.setAlignment(Qt.AlignCenter)
        self.GreenSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.GreenSpinBox.setAccelerated(False)

        self.verticalLayout_7.addWidget(self.GreenSpinBox)


        self.gridLayout_2.addWidget(self.Green, 0, 1, 1, 1)

        self.Blue = QFrame(self.frame)
        self.Blue.setObjectName(u"Blue")
        self.Blue.setStyleSheet(u"background: none;")
        self.verticalLayout_6 = QVBoxLayout(self.Blue)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 1)
        self.BlueSlider = QSlider(self.Blue)
        self.BlueSlider.setObjectName(u"BlueSlider")
        sizePolicy1.setHeightForWidth(self.BlueSlider.sizePolicy().hasHeightForWidth())
        self.BlueSlider.setSizePolicy(sizePolicy1)
        self.BlueSlider.setLayoutDirection(Qt.LeftToRight)
        self.BlueSlider.setAutoFillBackground(False)
        self.BlueSlider.setStyleSheet(u"background-color: none;")
        self.BlueSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_6.addWidget(self.BlueSlider, 0, Qt.AlignHCenter)

        self.BlueLable = QLabel(self.Blue)
        self.BlueLable.setObjectName(u"BlueLable")
        self.BlueLable.setStyleSheet(u"background-color: none;")
        self.BlueLable.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.BlueLable)

        self.BlueSpinBox = QSpinBox(self.Blue)
        self.BlueSpinBox.setObjectName(u"BlueSpinBox")
        self.BlueSpinBox.setLayoutDirection(Qt.LeftToRight)
        self.BlueSpinBox.setAutoFillBackground(False)
        self.BlueSpinBox.setStyleSheet(u"background-color: none;\n"
"color: black;")
        self.BlueSpinBox.setWrapping(False)
        self.BlueSpinBox.setFrame(False)
        self.BlueSpinBox.setAlignment(Qt.AlignCenter)
        self.BlueSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.BlueSpinBox.setAccelerated(False)

        self.verticalLayout_6.addWidget(self.BlueSpinBox)


        self.gridLayout_2.addWidget(self.Blue, 0, 2, 1, 1)

        self.HEXcolor = QLineEdit(self.frame)
        self.HEXcolor.setObjectName(u"HEXcolor")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.HEXcolor.sizePolicy().hasHeightForWidth())
        self.HEXcolor.setSizePolicy(sizePolicy3)
        self.HEXcolor.setAcceptDrops(True)
        self.HEXcolor.setStyleSheet(u"background-color: none;\n"
"color: black;")
        self.HEXcolor.setMaxLength(7)
        self.HEXcolor.setFrame(True)
        self.HEXcolor.setAlignment(Qt.AlignCenter)
        self.HEXcolor.setDragEnabled(False)

        self.gridLayout_2.addWidget(self.HEXcolor, 1, 0, 1, 3)


        self.verticalLayout_5.addWidget(self.frame)

        self.Buttons = QHBoxLayout()
        self.Buttons.setSpacing(10)
        self.Buttons.setObjectName(u"Buttons")
        self.Ok = QPushButton(self.GlobalFrame)
        self.Ok.setObjectName(u"Ok")
        sizePolicy2.setHeightForWidth(self.Ok.sizePolicy().hasHeightForWidth())
        self.Ok.setSizePolicy(sizePolicy2)

        self.Buttons.addWidget(self.Ok)

        self.Commit = QPushButton(self.GlobalFrame)
        self.Commit.setObjectName(u"Commit")
        sizePolicy2.setHeightForWidth(self.Commit.sizePolicy().hasHeightForWidth())
        self.Commit.setSizePolicy(sizePolicy2)

        self.Buttons.addWidget(self.Commit)

        self.Cancle = QPushButton(self.GlobalFrame)
        self.Cancle.setObjectName(u"Cancle")
        sizePolicy2.setHeightForWidth(self.Cancle.sizePolicy().hasHeightForWidth())
        self.Cancle.setSizePolicy(sizePolicy2)

        self.Buttons.addWidget(self.Cancle)

        self.Buttons.setStretch(0, 1)
        self.Buttons.setStretch(1, 2)
        self.Buttons.setStretch(2, 1)

        self.verticalLayout_5.addLayout(self.Buttons)

        self.verticalLayout_5.setStretch(0, 150)

        self.gridLayout.addWidget(self.GlobalFrame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.rgb_circle.setText("")
        self.RedLable.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">R</span></p></body></html>", None))
        self.GreeenLable.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">G</span></p></body></html>", None))
        self.BlueLable.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">B</span></p></body></html>", None))
        self.HEXcolor.setText(QCoreApplication.translate("Form", u"#000000", None))
        self.Ok.setText(QCoreApplication.translate("Form", u"\u041e\u043a", None))
        self.Commit.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.Cancle.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

