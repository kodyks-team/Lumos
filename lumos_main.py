import sys
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QSizePolicy
from MainWindow import Ui_MainWindow
from PySide6.QtCore import QSize



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.SettingsBtn.setFixedSize(40, 40)
        self.ui.SettingsBtn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.ui.SettingsBtn.setIconSize(QSize(40, 40))
        self.ui.SettingsBtn.clicked.connect(self.on_settings_clicked)

        self.ui.ChatSearch.setFixedHeight(40)
        self.ui.ChatSearch.textChanged.connect(self.on_search)

    def on_settings_clicked(self):
        print("Настройки открыты")

    def on_search(self, text: str):
        print("Поиск Чата:", text)

    def resizeEvent(self, event):
        super().resizeEvent(event)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()
        else:
            super().keyPressEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setDesktopFileName("lumos")

    window = MainWindow()
    window.show()
    sys.exit(app.exec())