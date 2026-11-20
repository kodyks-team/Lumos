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
        Form.setStyleSheet(u"background: url(:/icons/assets/backgrounds/wall_bcg.png);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"color: white;\n"
"padding: 10px 10px;")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"background: none;\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.7 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius: 100px;")

        self.verticalLayout_5.addWidget(self.label)

        self.frame1 = QFrame(self.frame)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setStyleSheet(u"background: none;\n"
"padding: 0px 0px;")
        self.gridLayout_2 = QGridLayout(self.frame1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(2)
        self.frame2 = QFrame(self.frame1)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setStyleSheet(u"background: none;")
        self.verticalLayout_4 = QVBoxLayout(self.frame2)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 1)
        self.verticalSlider = QSlider(self.frame2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        sizePolicy1.setHeightForWidth(self.verticalSlider.sizePolicy().hasHeightForWidth())
        self.verticalSlider.setSizePolicy(sizePolicy1)
        self.verticalSlider.setLayoutDirection(Qt.LeftToRight)
        self.verticalSlider.setAutoFillBackground(False)
        self.verticalSlider.setStyleSheet(u"background-color: none;")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_4.addWidget(self.verticalSlider, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.frame2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: none;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.spinBox_5 = QSpinBox(self.frame2)
        self.spinBox_5.setObjectName(u"spinBox_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spinBox_5.sizePolicy().hasHeightForWidth())
        self.spinBox_5.setSizePolicy(sizePolicy2)
        self.spinBox_5.setLayoutDirection(Qt.LeftToRight)
        self.spinBox_5.setAutoFillBackground(False)
        self.spinBox_5.setStyleSheet(u"background-color: none;\n"
"color: black;")
        self.spinBox_5.setWrapping(False)
        self.spinBox_5.setFrame(False)
        self.spinBox_5.setAlignment(Qt.AlignCenter)
        self.spinBox_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_5.setAccelerated(False)

        self.verticalLayout_4.addWidget(self.spinBox_5)


        self.gridLayout_2.addWidget(self.frame2, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.frame1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background: none;")
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 1)
        self.verticalSlider_3 = QSlider(self.frame_2)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        sizePolicy1.setHeightForWidth(self.verticalSlider_3.sizePolicy().hasHeightForWidth())
        self.verticalSlider_3.setSizePolicy(sizePolicy1)
        self.verticalSlider_3.setLayoutDirection(Qt.LeftToRight)
        self.verticalSlider_3.setAutoFillBackground(False)
        self.verticalSlider_3.setStyleSheet(u"background-color: none;")
        self.verticalSlider_3.setOrientation(Qt.Vertical)

        self.verticalLayout_7.addWidget(self.verticalSlider_3, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: none;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_4)

        self.spinBox_3 = QSpinBox(self.frame_2)
        self.spinBox_3.setObjectName(u"spinBox_3")
        sizePolicy2.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy2)
        self.spinBox_3.setLayoutDirection(Qt.LeftToRight)
        self.spinBox_3.setAutoFillBackground(False)
        self.spinBox_3.setStyleSheet(u"background-color: none;\n"
"color: black;")
        self.spinBox_3.setWrapping(False)
        self.spinBox_3.setFrame(False)
        self.spinBox_3.setAlignment(Qt.AlignCenter)
        self.spinBox_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_3.setAccelerated(False)

        self.verticalLayout_7.addWidget(self.spinBox_3)


        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame3 = QFrame(self.frame1)
        self.frame3.setObjectName(u"frame3")
        self.frame3.setStyleSheet(u"background: none;")
        self.verticalLayout_6 = QVBoxLayout(self.frame3)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 1)
        self.verticalSlider_2 = QSlider(self.frame3)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        sizePolicy1.setHeightForWidth(self.verticalSlider_2.sizePolicy().hasHeightForWidth())
        self.verticalSlider_2.setSizePolicy(sizePolicy1)
        self.verticalSlider_2.setLayoutDirection(Qt.LeftToRight)
        self.verticalSlider_2.setAutoFillBackground(False)
        self.verticalSlider_2.setStyleSheet(u"background-color: none;")
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.verticalLayout_6.addWidget(self.verticalSlider_2, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.frame3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: none;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.spinBox_2 = QSpinBox(self.frame3)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setLayoutDirection(Qt.LeftToRight)
        self.spinBox_2.setAutoFillBackground(False)
        self.spinBox_2.setStyleSheet(u"background-color: none;\n"
"color: black;")
        self.spinBox_2.setWrapping(False)
        self.spinBox_2.setFrame(False)
        self.spinBox_2.setAlignment(Qt.AlignCenter)
        self.spinBox_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_2.setAccelerated(False)

        self.verticalLayout_6.addWidget(self.spinBox_2)


        self.gridLayout_2.addWidget(self.frame3, 0, 2, 1, 1)

        self.lineEdit = QLineEdit(self.frame1)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy3)
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.setStyleSheet(u"background-color: none;\n"
"color: black;")
        self.lineEdit.setMaxLength(7)
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setDragEnabled(False)

        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 3)


        self.verticalLayout_5.addWidget(self.frame1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.verticalLayout_5.setStretch(0, 150)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">R</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">G</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">B</span></p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"#000000", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u043a", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

