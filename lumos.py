from fn_socket import *
from PyQt6.QtWidgets import * # type: ignore
from PyQt6.QtCore import * # type: ignore
from PyQt6.QtGui import * # type: ignore
from PyQt6.QtWidgets import QApplication, QInputDialog, QMessageBox


def get_input(text: str, title: str = "Ввод", password: bool = False) -> str:
    """
    Показывает диалог ввода с возможностью маскировки
    
    Args:
        text: текст подсказки
        title: заголовок окна
        password: если True - скрывает ввод звездочками
    
    Returns:
        str: введенный текст или "0" если отмена
    """
    dialog = QInputDialog(None)
    dialog.setWindowTitle(title)
    dialog.setLabelText(text)
    dialog.setOkButtonText("OK")
    dialog.setCancelButtonText("Отмена")
    
    # Настраиваем поле ввода
    line_edit = dialog.findChild(QLineEdit)
    if line_edit:
        if password:
            # Маскируем ввод звездочками
            line_edit.setEchoMode(QLineEdit.Password)
        else:
            line_edit.setEchoMode(QLineEdit.Normal)
    
    result = dialog.exec()
    
    if result == QInputDialog.Accepted:
        return dialog.textValue()
    return "0"

def show_error(text: str, title: str = "Ошибка") -> None: 
    QMessageBox.critical(None, title, text)

def show_confirm_dialog(parent, title, message):
    """
    Показывает диалог подтверждения с кнопками Да/Нет
    
    Args:
        parent: родительский виджет
        title: заголовок окна
        message: текст сообщения
    
    Returns:
        bool: True если нажали "Да", False если нажали "Нет" или закрыли окно
    """
    msg_box = QMessageBox(parent)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    
    # Создаем кнопки
    yes_button = msg_box.addButton("Да", QMessageBox.YesRole) # type: ignore
    no_button = msg_box.addButton("Нет", QMessageBox.NoRole) # type: ignore
    
    # Устанавливаем кнопку "Нет" как кнопку по умолчанию
    msg_box.setDefaultButton(no_button)
    
    # Устанавливаем Escape и Enter на "Нет"
    # Escape всегда закрывает диалог с результатом "Нет"
    # Enter нажимает кнопку по умолчанию ("Нет")
    
    # Показываем диалог
    msg_box.exec()
    
    # Определяем, какая кнопка была нажата
    clicked_button = msg_box.clickedButton()
    
    if clicked_button == yes_button:
        return True
    else:
        return False

def authorization():
    global master_password
    mast_p = get_input("Введите мастер-пароль", password = True)
    if not check_password(mast_p):
        show_error("Неправильный мастер-пароль")
        sys.exit()
    else:
        master_password = mast_p


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    authorization()

    print(GET(0))

    #sys.exit(app.exec())
