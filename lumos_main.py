import sys
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QSizePolicy, QWidget
from MainWindow import Ui_MainWindow
from LumosSettings import Ui_SettingsWidget



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
        self.setting_widget = QWidget()
        self.settings_ui = Ui_SettingsWidget()
        self.settings_ui.setupUi(self.setting_widget)
        self.setting_widget.show()

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

    window = MainWindow()
    window.show()
    sys.exit(app.exec())