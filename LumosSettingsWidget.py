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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTabWidget, QWidget)
import lumos_rc

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if not SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.setEnabled(True)
        SettingsWidget.resize(600, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsWidget.sizePolicy().hasHeightForWidth())
        SettingsWidget.setSizePolicy(sizePolicy)
        SettingsWidget.setStyleSheet(u"QWidget {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 0, y2: 1,\n"
"\n"
"        stop: 0.00 #0039A6,\n"
"        stop: 0.333 #0039A6,\n"
"        stop: 0.334 #0039A6,\n"
"        stop: 0.666 #0039A6,\n"
"        stop: 0.667 #0039A6,\n"
"        stop: 1.00 #0039A6\n"
"    );\n"
"}")
        self.settings_tab = QTabWidget(SettingsWidget)
        self.settings_tab.setObjectName(u"settings_tab")
        self.settings_tab.setGeometry(QRect(110, 110, 401, 401))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.settings_tab.sizePolicy().hasHeightForWidth())
        self.settings_tab.setSizePolicy(sizePolicy1)
        self.settings_tab.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border-radius: 7px")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.settings_tab.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.settings_tab.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.settings_tab.addTab(self.tab_2, "")

        self.retranslateUi(SettingsWidget)

        self.settings_tab.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle(QCoreApplication.translate("SettingsWidget", u"Lumos - Settings", None))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.tab_3), QCoreApplication.translate("SettingsWidget", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435", None))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.tab), QCoreApplication.translate("SettingsWidget", u"\u041e\u0431\u0449\u0438\u0439 \u0432\u0438\u0434", None))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.tab_2), QCoreApplication.translate("SettingsWidget", u"\u0421\u0442\u0438\u043b\u044c \u0447\u0430\u0442\u043e\u0432", None))
    # retranslateUi

