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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QTabWidget,
    QWidget)
import lumos_rc

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if not SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.setEnabled(True)
        SettingsWidget.resize(400, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsWidget.sizePolicy().hasHeightForWidth())
        SettingsWidget.setSizePolicy(sizePolicy)
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
"color: white")
        self.Profile = QWidget()
        self.Profile.setObjectName(u"Profile")
        self.settings_tab.addTab(self.Profile, "")
        self.Stylesheet = QWidget()
        self.Stylesheet.setObjectName(u"Stylesheet")
        self.settings_tab.addTab(self.Stylesheet, "")
        self.Securiry = QWidget()
        self.Securiry.setObjectName(u"Securiry")
        self.settings_tab.addTab(self.Securiry, "")
        self.Memory = QWidget()
        self.Memory.setObjectName(u"Memory")
        self.settings_tab.addTab(self.Memory, "")

        self.gridLayout.addWidget(self.settings_tab, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 100)

        self.retranslateUi(SettingsWidget)

        self.settings_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle(QCoreApplication.translate("SettingsWidget", u"Lumos - Settings", None))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.Profile), QCoreApplication.translate("SettingsWidget", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.Stylesheet), QCoreApplication.translate("SettingsWidget", u"\u041e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u0435", None))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.Securiry), QCoreApplication.translate("SettingsWidget", u"\u0411\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c", None))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.Memory), QCoreApplication.translate("SettingsWidget", u"\u041f\u0430\u043c\u044f\u0442\u044c", None))
    # retranslateUi

