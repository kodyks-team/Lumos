# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LumosSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)
import lumos_rc

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if not SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.setEnabled(True)
        SettingsWidget.resize(400, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsWidget.sizePolicy().hasHeightForWidth())
        SettingsWidget.setSizePolicy(sizePolicy)
        SettingsWidget.setMinimumSize(QSize(400, 600))
        SettingsWidget.setMaximumSize(QSize(400, 600))
        SettingsWidget.setStyleSheet(u"background: qlineargradient(\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0 #003366,\n"
"    stop:0.5 #4facfe,\n"
"    stop:1 #00ced1\n"
");\n"
"font-family: Lucida Suns Unicode;")
        self.gridLayout = QGridLayout(SettingsWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.settings_tab = QTabWidget(SettingsWidget)
        self.settings_tab.setObjectName(u"settings_tab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.settings_tab.sizePolicy().hasHeightForWidth())
        self.settings_tab.setSizePolicy(sizePolicy1)
        self.settings_tab.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border-radius: 12px;\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"")
        self.Profile = QWidget()
        self.Profile.setObjectName(u"Profile")
        self.settings_tab.addTab(self.Profile, "")
        self.Stylesheet = QWidget()
        self.Stylesheet.setObjectName(u"Stylesheet")
        self.gridLayout_9 = QGridLayout(self.Stylesheet)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.Stylesheet)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background: none")
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame1 = QFrame(self.frame)
        self.frame1.setObjectName(u"frame1")
        self.gridLayout_2 = QGridLayout(self.frame1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(6)
        self.label = QLabel(self.frame1)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(30)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-size: 19pt;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)

        self.radioButton = QRadioButton(self.frame1)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setMinimumSize(QSize(0, 40))
        self.radioButton.setChecked(False)

        self.gridLayout_2.addWidget(self.radioButton, 2, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.frame1)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMinimumSize(QSize(0, 40))
        self.radioButton_2.setChecked(True)

        self.gridLayout_2.addWidget(self.radioButton_2, 2, 1, 1, 1)

        self.radioButton_3 = QRadioButton(self.frame1)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.radioButton_3, 2, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame1)

        self.frame2 = QFrame(self.frame)
        self.frame2.setObjectName(u"frame2")
        self.verticalLayout_2 = QVBoxLayout(self.frame2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame3 = QFrame(self.frame2)
        self.frame3.setObjectName(u"frame3")
        self.frame3.setEnabled(False)
        self.verticalLayout = QVBoxLayout(self.frame3)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.pushButton = QPushButton(self.frame3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame3)

        self.frame_2 = QFrame(self.frame2)
        self.frame_2.setObjectName(u"frame_2")
        self.gridLayout_10 = QGridLayout(self.frame_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(10)
        self.gridLayout_10.setVerticalSpacing(6)
        self.radioButton_6 = QRadioButton(self.frame_2)
        self.radioButton_6.setObjectName(u"radioButton_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.radioButton_6.sizePolicy().hasHeightForWidth())
        self.radioButton_6.setSizePolicy(sizePolicy3)
        self.radioButton_6.setMinimumSize(QSize(0, 30))
        self.radioButton_6.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_10.addWidget(self.radioButton_6, 1, 2, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_5, 0, 0, 1, 3)

        self.radioButton_4 = QRadioButton(self.frame_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        sizePolicy3.setHeightForWidth(self.radioButton_4.sizePolicy().hasHeightForWidth())
        self.radioButton_4.setSizePolicy(sizePolicy3)
        self.radioButton_4.setMinimumSize(QSize(0, 30))
        self.radioButton_4.setChecked(False)

        self.gridLayout_10.addWidget(self.radioButton_4, 1, 0, 1, 1)

        self.radioButton_5 = QRadioButton(self.frame_2)
        self.radioButton_5.setObjectName(u"radioButton_5")
        sizePolicy3.setHeightForWidth(self.radioButton_5.sizePolicy().hasHeightForWidth())
        self.radioButton_5.setSizePolicy(sizePolicy3)
        self.radioButton_5.setMinimumSize(QSize(0, 30))
        self.radioButton_5.setChecked(True)

        self.gridLayout_10.addWidget(self.radioButton_5, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame4 = QFrame(self.frame2)
        self.frame4.setObjectName(u"frame4")
        self.gridLayout_8 = QGridLayout(self.frame4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame5 = QFrame(self.frame4)
        self.frame5.setObjectName(u"frame5")
        self.frame5.setEnabled(False)
        self.gridLayout_7 = QGridLayout(self.frame5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_8 = QLabel(self.frame5)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setMinimumSize(QSize(0, 20))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.frame5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy5)
        self.pushButton_7.setMinimumSize(QSize(0, 50))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.pushButton_7, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame5, 0, 3, 1, 1)

        self.frame6 = QFrame(self.frame4)
        self.frame6.setObjectName(u"frame6")
        self.gridLayout_6 = QGridLayout(self.frame6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_6 = QLabel(self.frame6)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setMinimumSize(QSize(0, 20))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.frame6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy5.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy5)
        self.pushButton_5.setMinimumSize(QSize(0, 50))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(0, 206, 209);")

        self.gridLayout_6.addWidget(self.pushButton_5, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame6, 0, 2, 1, 1)

        self.frame7 = QFrame(self.frame4)
        self.frame7.setObjectName(u"frame7")
        self.gridLayout_5 = QGridLayout(self.frame7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_3 = QLabel(self.frame7)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy5.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy5)
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(79, 172, 254);")

        self.gridLayout_5.addWidget(self.pushButton_2, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame7, 0, 1, 1, 1)

        self.frame8 = QFrame(self.frame4)
        self.frame8.setObjectName(u"frame8")
        self.gridLayout_3 = QGridLayout(self.frame8)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.frame8)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setMinimumSize(QSize(0, 20))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.frame8)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy5.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy5)
        self.pushButton_6.setMinimumSize(QSize(0, 50))
        self.pushButton_6.setStyleSheet(u"background-color: rgb(0, 51, 102);")

        self.gridLayout_3.addWidget(self.pushButton_6, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame8, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame4)

        self.frame9 = QFrame(self.frame2)
        self.frame9.setObjectName(u"frame9")
        self.frame9.setEnabled(False)
        self.gridLayout_4 = QGridLayout(self.frame9)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(10)
        self.lineEdit = QLineEdit(self.frame9)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.lineEdit, 2, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame9)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(20, 0))
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_3.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_3.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/svg/assets/svg/file_open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setAutoRepeat(False)
        self.pushButton_3.setAutoExclusive(False)

        self.gridLayout_4.addWidget(self.pushButton_3, 2, 1, 1, 1)

        self.label_4 = QLabel(self.frame9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame9)


        self.verticalLayout_3.addWidget(self.frame2)


        self.gridLayout_9.addWidget(self.frame, 0, 0, 1, 1)

        self.settings_tab.addTab(self.Stylesheet, "")
        self.Security = QWidget()
        self.Security.setObjectName(u"Security")
        self.settings_tab.addTab(self.Security, "")
        self.Memory = QWidget()
        self.Memory.setObjectName(u"Memory")
        self.settings_tab.addTab(self.Memory, "")

        self.gridLayout.addWidget(self.settings_tab, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 100)

        self.retranslateUi(SettingsWidget)

        self.settings_tab.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle(QCoreApplication.translate("SettingsWidget", u"Lumos - Settings", None))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.Profile), QCoreApplication.translate("SettingsWidget", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.label.setText(QCoreApplication.translate("SettingsWidget", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0438\u043f \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u044f", None))
        self.radioButton.setText(QCoreApplication.translate("SettingsWidget", u"\u0421\u043f\u043b\u043e\u0448\u043d\u043e\u0439 \u0446\u0432\u0435\u0442", None))
        self.radioButton_2.setText(QCoreApplication.translate("SettingsWidget", u"\u0413\u0430\u0440\u0434\u0438\u0435\u043d\u0442", None))
        self.radioButton_3.setText(QCoreApplication.translate("SettingsWidget", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWidget", u"\u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430", None))
        self.pushButton.setText("")
        self.radioButton_6.setText(QCoreApplication.translate("SettingsWidget", u"4", None))
        self.label_5.setText(QCoreApplication.translate("SettingsWidget", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0446\u0432\u0435\u0442\u043e\u0432 \u0434\u043b\u044f \u0433\u0430\u0440\u0434\u0438\u0435\u043d\u0442\u0430", None))
        self.radioButton_4.setText(QCoreApplication.translate("SettingsWidget", u"2", None))
        self.radioButton_5.setText(QCoreApplication.translate("SettingsWidget", u"3", None))
        self.label_8.setText(QCoreApplication.translate("SettingsWidget", u"\u0426\u0432\u0435\u0442 4", None))
        self.pushButton_7.setText("")
        self.label_6.setText(QCoreApplication.translate("SettingsWidget", u"\u0426\u0432\u0435\u0442 3", None))
        self.pushButton_5.setText("")
        self.label_3.setText(QCoreApplication.translate("SettingsWidget", u"\u0426\u0432\u0435\u0442 2", None))
        self.pushButton_2.setText("")
        self.label_7.setText(QCoreApplication.translate("SettingsWidget", u"\u0426\u0432\u0435\u0442 1", None))
        self.pushButton_6.setText("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("SettingsWidget", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.pushButton_3.setText("")
        self.label_4.setText(QCoreApplication.translate("SettingsWidget", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443 \u0441 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435\u043c", None))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.Stylesheet), QCoreApplication.translate("SettingsWidget", u"\u041e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u0435", None))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.Security), QCoreApplication.translate("SettingsWidget", u"\u0411\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c", None))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.Memory), QCoreApplication.translate("SettingsWidget", u"\u041f\u0430\u043c\u044f\u0442\u044c", None))
    # retranslateUi

