# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lumos.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import lumos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        MainWindow.setStyleSheet(u"background: qlineargradient(\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0 #003366,\n"
"    stop:0.5 #4facfe,\n"
"    stop:1 #00ced1\n"
");\n"
"font-family: Lucida Suns Unicode;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.GlobalFrame = QFrame(self.centralwidget)
        self.GlobalFrame.setObjectName(u"GlobalFrame")
        self.GlobalFrame.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.GlobalFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"")
        self.GlobalFrame.setLineWidth(1)
        self.horizontalLayout_3 = QHBoxLayout(self.GlobalFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.ChatsFrame = QFrame(self.GlobalFrame)
        self.ChatsFrame.setObjectName(u"ChatsFrame")
        self.ChatsFrame.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ChatsFrame.setStyleSheet(u"color: black;\n"
"font-size: 16;\n"
"background-color: none;\n"
"border: none;")
        self.verticalLayout = QVBoxLayout(self.ChatsFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Chats_LayoutH = QHBoxLayout()
        self.Chats_LayoutH.setSpacing(6)
        self.Chats_LayoutH.setObjectName(u"Chats_LayoutH")
        self.Chats_LayoutH.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.SettingsBtn = QPushButton(self.ChatsFrame)
        self.SettingsBtn.setObjectName(u"SettingsBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.SettingsBtn.sizePolicy().hasHeightForWidth())
        self.SettingsBtn.setSizePolicy(sizePolicy)
        self.SettingsBtn.setMinimumSize(QSize(40, 40))
        self.SettingsBtn.setMaximumSize(QSize(16777215, 16777215))
        self.SettingsBtn.setSizeIncrement(QSize(0, 0))
        self.SettingsBtn.setBaseSize(QSize(0, 0))
        self.SettingsBtn.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.SettingsBtn.setAutoFillBackground(False)
        self.SettingsBtn.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 50, 50, 60);\n"
"border-radius: 10px;\n"
"icon-size: auto;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(50, 50, 50, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(50, 50, 50, 90);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/assets/svg/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SettingsBtn.setIcon(icon)
        self.SettingsBtn.setIconSize(QSize(40, 40))
        self.SettingsBtn.setCheckable(False)
        self.SettingsBtn.setChecked(False)
        self.SettingsBtn.setAutoRepeat(False)
        self.SettingsBtn.setAutoExclusive(False)
        self.SettingsBtn.setAutoDefault(False)

        self.Chats_LayoutH.addWidget(self.SettingsBtn)

        self.ChatSearch = QLineEdit(self.ChatsFrame)
        self.ChatSearch.setObjectName(u"ChatSearch")
        self.ChatSearch.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ChatSearch.sizePolicy().hasHeightForWidth())
        self.ChatSearch.setSizePolicy(sizePolicy1)
        self.ChatSearch.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"font-size: 14px;\n"
"border-radius: 10px;")
        self.ChatSearch.setMaxLength(32767)
        self.ChatSearch.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.ChatSearch.setClearButtonEnabled(False)

        self.Chats_LayoutH.addWidget(self.ChatSearch)

        self.Chats_LayoutH.setStretch(0, 1)
        self.Chats_LayoutH.setStretch(1, 4)

        self.verticalLayout.addLayout(self.Chats_LayoutH)

        self.ChatsSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.ChatsSpacer)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 12)

        self.horizontalLayout_3.addWidget(self.ChatsFrame)

        self.ChatFrame = QFrame(self.GlobalFrame)
        self.ChatFrame.setObjectName(u"ChatFrame")
        self.ChatFrame.setEnabled(True)
        self.ChatFrame.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ChatFrame.setStyleSheet(u"border-radius: 10px;color: black;\n"
"font-size: 16;\n"
"background-color: rgba(255, 255, 255, 20);\n"
"border: none;\n"
"border-radius: 10px;")
        self.verticalLayout_2 = QVBoxLayout(self.ChatFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ChatSpacerUp = QSpacerItem(17, 252, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.ChatSpacerUp)

        self.ChatLayoutH = QHBoxLayout()
        self.ChatLayoutH.setSpacing(0)
        self.ChatLayoutH.setObjectName(u"ChatLayoutH")
        self.ChatSpacerLeft = QSpacerItem(37, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ChatLayoutH.addItem(self.ChatSpacerLeft)

        self.ChatInfo = QLabel(self.ChatFrame)
        self.ChatInfo.setObjectName(u"ChatInfo")
        self.ChatInfo.setLineWidth(0)
        self.ChatInfo.setAlignment(Qt.AlignCenter)

        self.ChatLayoutH.addWidget(self.ChatInfo)

        self.ChatSpacerRight = QSpacerItem(37, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ChatLayoutH.addItem(self.ChatSpacerRight)

        self.ChatLayoutH.setStretch(0, 1)
        self.ChatLayoutH.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.ChatLayoutH)

        self.ChatSpacerDown = QSpacerItem(17, 252, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.ChatSpacerDown)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 10)

        self.horizontalLayout_3.addWidget(self.ChatFrame)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)

        self.horizontalLayout.addWidget(self.GlobalFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.SettingsBtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lumos", None))
        self.SettingsBtn.setText("")
#if QT_CONFIG(shortcut)
        self.SettingsBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.ChatSearch.setInputMask("")
        self.ChatSearch.setText("")
        self.ChatSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\U0001f50d \U0000041d\U00000430\U00000439\U00000442\U00000438 \U00000427\U00000430\U00000442", None))
        self.ChatInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#383838;\">\u0427\u0430\u0442 \u043f\u043e\u043a\u0430-\u0447\u0442\u043e \u043d\u0435 \u043e\u0442\u043a\u0440\u044b\u0442 </span><img src=\":/icons/assets/svg/no_emotion.svg\"/></p></body></html>", None))
    # retranslateUi

