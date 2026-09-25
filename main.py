import sys
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow
from PySide6.QtCore import QSize



class MainWindow(QMainWindow):
    def __init__(self, fullscreen=False):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ChatSearch.textChanged.connect(self.on_search)

    def on_search(self, text: str):
        print("Поиск Чата:", text)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        size = int(min(self.ui.SettingsBtn.width(),
                       self.ui.SettingsBtn.height()) * 0.67)

        self.ui.SettingsBtn.setIconSize(
            QSize(size, size)
        )

        size = max(12, int(self.width() * 0.02))

        font = QFont()
        font.setPointSize(size)
        self.ui.ChatSearch.setFont(font)

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

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
