import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


# ========== ЭЛЕМЕНТ СПИСКА ЧАТОВ ==========
class ChatListItem(QWidget):
    """Элемент списка чатов: аватар + имя + последнее сообщение"""
    
    clicked = pyqtSignal(str)  # сигнал с user_id
    
    def __init__(self, user_id: str, name: str, last_message: str,
                 avatar_color: str = "#4CAF50", parent=None):
        super().__init__(parent)
        
        self.user_id = user_id
        self.is_selected = False
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 8, 10, 8)
        layout.setSpacing(10)
        
        # --- Аватар ---
        self.avatar = QLabel(name[0].upper() if name else "?")
        self.avatar.setFixedSize(45, 45)
        self.avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.avatar.setStyleSheet(f"""
            QLabel {{
                background: {avatar_color};
                color: white;
                border-radius: 22px;
                font-size: 36px;
                font-weight: bold;
            }}
        """)
        layout.addWidget(self.avatar)
        
        # --- Текст (имя + последнее сообщение) ---
        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)
        text_layout.setContentsMargins(0, 0, 0, 0)
        
        self.name_label = QLabel(name)
        self.name_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 10px;
                font-weight: bold;
            }
        """)
        
        short_message = last_message[:20] + "..." if len(last_message) > 20 else last_message
        self.message_label = QLabel(short_message)
        self.message_label.setStyleSheet("""
            QLabel {
                color: #8e8e93;
                font-size: 12px;
            }
        """)
        
        text_layout.addWidget(self.name_label)
        text_layout.addWidget(self.message_label)
        layout.addLayout(text_layout, 1)
        
        self.setFixedHeight(65)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self._apply_style(False)
    
    def _apply_style(self, selected: bool):
        if selected:
            bg = "#2b5278"
            hover = "#2b5278"
        else:
            bg = "transparent"
            hover = "#2b2b2b"
        
        self.setStyleSheet(f"""
            ChatListItem {{
                background: {bg};
                border-radius: 8px;
            }}
            ChatListItem:hover {{
                background: {hover};
            }}
        """)
    
    def set_selected(self, selected: bool):
        self.is_selected = selected
        self._apply_style(selected)
    
    def update_last_message(self, text: str):
        """Обновляет текст последнего сообщения"""
        short = text[:20] + "..." if len(text) > 20 else text
        self.message_label.setText(short)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(self.user_id)
        super().mousePressEvent(event)


# ========== ВИДЖЕТ ЧАТА ==========
class ChatWidget(QWidget):
    
    message_sent = pyqtSignal(str, str)  # (user_id, text) — для обновления последнего сообщения
    
    def __init__(self, user_id: str, name: str, parent=None):
        super().__init__(parent)
        
        self.user_id = user_id
        self.name = name
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # --- Шапка чата ---
        header = QWidget()
        header.setFixedHeight(60)
        header.setStyleSheet("""
            QWidget {
                background: #17212b;
                border-bottom: 1px solid #2b2b2b;
            }
        """)
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(15, 0, 15, 0)
        
        self.header_label = QLabel(name)
        self.header_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
            }
        """)
        header_layout.addWidget(self.header_label)
        header_layout.addStretch()
        
        layout.addWidget(header)
        
        # --- Область сообщений ---
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("""
            QScrollArea {
                background: #0e1621;
                border: none;
            }
            QScrollBar:vertical {
                background: #17212b;
                width: 8px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: #2b5278;
                border-radius: 4px;
                min-height: 30px;
            }
            QScrollBar::handle:vertical:hover {
                background: #3a6ea5;
            }
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)
        
        self.messages_container = QWidget()
        self.messages_container.setStyleSheet("background: #0e1621;")
        self.messages_layout = QVBoxLayout(self.messages_container)
        self.messages_layout.setContentsMargins(15, 15, 15, 15)
        self.messages_layout.setSpacing(10)
        self.messages_layout.addStretch()
        
        self.scroll.setWidget(self.messages_container)
        layout.addWidget(self.scroll, 1)
        
        # --- Поле ввода ---
        input_widget = QWidget()
        input_widget.setFixedHeight(60)
        input_widget.setStyleSheet("""
            QWidget {
                background: #17212b;
                border-top: 1px solid #2b2b2b;
            }
        """)
        input_layout = QHBoxLayout(input_widget)
        input_layout.setContentsMargins(10, 10, 10, 10)
        input_layout.setSpacing(10)
        
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Написать сообщение...")
        self.input_field.setMinimumHeight(38)
        self.input_field.setStyleSheet("""
            QLineEdit {
                background: #242f3d;
                border: none;
                border-radius: 19px;
                padding: 0 15px;
                color: #ffffff;
                font-size: 14px;
            }
            QLineEdit:focus {
                background: #2b3a4d;
            }
        """)
        
        self.send_button = QPushButton("➤")
        self.send_button.setFixedSize(38, 38)
        self.send_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.send_button.setStyleSheet("""
            QPushButton {
                background: #2b5278;
                color: white;
                border: none;
                border-radius: 19px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: #3a6ea5;
            }
            QPushButton:pressed {
                background: #1e3a5f;
            }
        """)
        
        input_layout.addWidget(self.input_field, 1)
        input_layout.addWidget(self.send_button)
        layout.addWidget(input_widget)
        
        self.send_button.clicked.connect(self.send_message)
        self.input_field.returnPressed.connect(self.send_message)
    
    def add_message(self, text: str, is_mine: bool = False):
        """Добавляет сообщение в чат"""
        bubble = self._create_bubble(text, is_mine)
        self.messages_layout.insertWidget(self.messages_layout.count() - 1, bubble)
        
        QTimer.singleShot(50, lambda: self.scroll.verticalScrollBar().setValue(
            self.scroll.verticalScrollBar().maximum()
        ))
    
    def _create_bubble(self, text: str, is_mine: bool) -> QWidget:
        wrapper = QWidget()
        wrapper_layout = QHBoxLayout(wrapper)
        wrapper_layout.setContentsMargins(0, 0, 0, 0)
        
        bubble = QLabel(text)
        bubble.setWordWrap(True)
        bubble.setMaximumWidth(500)
        bubble.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        
        if is_mine:
            bubble.setStyleSheet("""
                QLabel {
                    background: #2b5278;
                    color: #ffffff;
                    border-radius: 12px;
                    padding: 8px 12px;
                    font-size: 14px;
                }
            """)
            wrapper_layout.addStretch()
            wrapper_layout.addWidget(bubble)
        else:
            bubble.setStyleSheet("""
                QLabel {
                    background: #182533;
                    color: #ffffff;
                    border-radius: 12px;
                    padding: 8px 12px;
                    font-size: 14px;
                }
            """)
            wrapper_layout.addWidget(bubble)
            wrapper_layout.addStretch()
        
        return wrapper
    
    def send_message(self):
        text = self.input_field.text().strip()
        if not text:
            return
        
        self.add_message(text, is_mine=True)
        self.input_field.clear()
        
        # Сообщаем наружу — чтобы обновить последнее сообщение в списке
        self.message_sent.emit(self.user_id, text)


# ========== ГЛАВНОЕ ОКНО ==========
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Lumos")
        self.setGeometry(100, 100, 1100, 700)
        
        central = QWidget()
        self.setCentralWidget(central)
        
        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # ===== ЛЕВАЯ ПАНЕЛЬ =====
        left_panel = QWidget()
        left_panel.setFixedWidth(320)
        left_panel.setStyleSheet("""
            QWidget {
                background: #17212b;
                border-right: 1px solid #0e1621;
            }
        """)
        
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)
        
        # --- Поиск ---
        search_widget = QWidget()
        search_widget.setFixedHeight(60)
        search_layout = QHBoxLayout(search_widget)
        search_layout.setContentsMargins(10, 10, 10, 10)
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Поиск")
        self.search_input.setMinimumHeight(38)
        self.search_input.setStyleSheet("""
            QLineEdit {
                background: #242f3d;
                border: none;
                border-radius: 19px;
                padding: 0 15px;
                color: #ffffff;
                font-size: 14px;
            }
            QLineEdit:focus {
                background: #2b3a4d;
            }
        """)
        search_layout.addWidget(self.search_input)
        left_layout.addWidget(search_widget)
        
        # --- Список чатов ---
        self.chat_scroll = QScrollArea()
        self.chat_scroll.setWidgetResizable(True)
        self.chat_scroll.setStyleSheet("""
            QScrollArea {
                background: #17212b;
                border: none;
            }
            QScrollBar:vertical {
                background: #17212b;
                width: 8px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: #2b5278;
                border-radius: 4px;
                min-height: 30px;
            }
            QScrollBar::handle:vertical:hover {
                background: #3a6ea5;
            }
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)
        
        self.chat_list_container = QWidget()
        self.chat_list_layout = QVBoxLayout(self.chat_list_container)
        self.chat_list_layout.setContentsMargins(5, 5, 5, 5)
        self.chat_list_layout.setSpacing(2)
        self.chat_list_layout.addStretch()
        
        self.chat_scroll.setWidget(self.chat_list_container)
        left_layout.addWidget(self.chat_scroll, 1)
        
        main_layout.addWidget(left_panel)
        
        # ===== ПРАВАЯ ЧАСТЬ (стек чатов) =====
        self.stack = QStackedWidget()
        self.stack.setStyleSheet("background: #0e1621;")
        main_layout.addWidget(self.stack, 1)
        
        # ===== ДАННЫЕ ЧАТОВ =====
        self.chats_data = [
            {"user_id": "user1", "name": "💠Архив", "last": "Потом придумаю чатик...", "color": "#000000",
             "messages": [("Привет! Это архив", False), ("Тут старые сообщения", False)]},
            
            {"user_id": "user2", "name": "⚗️Velum VPN", "last": "Я Ваш личный бот и помощник", "color": "#000000",
             "messages": [("Я Ваш личный бот и помощник Velum VPN", False), ("Чем могу помочь?", False)]},
            
            {"user_id": "user3", "name": "💎MooBot", "last": "lerks купил у тебя 6790 монет", "color": "#000000",
             "messages": [("lerks купил у тебя 4 монеты", False), ("+ 6790 монет зачислено", False)]},
            
            {"user_id": "user4", "name": "🧲Максим Кац", "last": "Пока армия России заявляет...", "color": "#000000",
             "messages": [("Пока армия России заявляет о псевдозахватах,", False), ("мы продолжаем работу", False)]},
            
            {"user_id": "user5", "name": "🥨.......", "last": "Страшновато как то", "color": "#000000",
             "messages": [("Страшновато как то", True)]},
            
            {"user_id": "user6", "name": "🫒Виталя Фишер", "last": "Отменённый звонок", "color": "#000000",
             "messages": [("Отменённый звонок", False)]},
            
            {"user_id": "user7", "name": "🌜2 отряд", "last": "Голосовое сообщение", "color": "#000000",
             "messages": [("ебя", False), ("Голосовое сообщение", False)]},
            
            {"user_id": "user8", "name": "⭐️Чат KODUKS TEAM", "last": "Валентин: Не скажу, думай сам", "color": "#000000",
             "messages": [("Валентин: Не скажу, думай сам", False)]},
            
            {"user_id": "user9", "name": "🙃KODUKS TEAM", "last": "Есть идеи, есть мысли...", "color": "#000000",
             "messages": [("Есть идеи, есть мысли и скорее всего будут изм...", False)]},
            
            {"user_id": "user10", "name": "😃lisiу dankar", "last": "Короче 3 и 4 за зачет...", "color": "#000000",
             "messages": [("Короче 3 и 4 за зачет, самое страшное это когда...", False)]},
            
            {"user_id": "user11", "name": "🧽Валентин", "last": "Входящий звонок", "color": "#000000",
             "messages": [("Входящий звонок", False)]},
            
            {"user_id": "user12", "name": "🪣Pavel Durov", "last": "Telegram has become the sponsor", "color": "#000000",
             "messages": [("Telegram has become the sponsor of Codef...", False)]},
        ]
        
        self.chat_items = {}     # user_id -> ChatListItem
        self.chat_widgets = {}   # user_id -> ChatWidget
        self.current_user_id = None
        
        self._populate_chats()
        
        # Открываем первый чат
        if self.chats_data:
            self.open_chat(self.chats_data[0]["user_id"])
  
    def _populate_chats(self):
        """Заполняет список чатов и создает для каждого виджет"""
        for chat in self.chats_data:
            # Элемент списка
            item = ChatListItem(
                user_id=chat["user_id"],
                name=chat["name"],
                last_message=chat["last"],
                avatar_color=chat["color"]
            )
            item.clicked.connect(self.open_chat)
            self.chat_list_layout.insertWidget(self.chat_list_layout.count() - 1, item)
            self.chat_items[chat["user_id"]] = item
            
            # Виджет чата
            widget = ChatWidget(chat["user_id"], chat["name"])
            widget.message_sent.connect(self._on_message_sent)
            
            # Заполняем историю сообщений
            for text, is_mine in chat.get("messages", []):
                widget.add_message(text, is_mine=is_mine)
            
            self.stack.addWidget(widget)
            self.chat_widgets[chat["user_id"]] = widget
    
    def open_chat(self, user_id: str):
        """Открывает чат"""
        if user_id not in self.chat_widgets:
            return
        
        # Переключаем виджет
        widget = self.chat_widgets[user_id]
        self.stack.setCurrentWidget(widget)
        self.current_user_id = user_id
        
        # Подсветка в списке
        for uid, item in self.chat_items.items():
            item.set_selected(uid == user_id)
    
    def _on_message_sent(self, user_id: str, text: str):
        """Обновляет последнее сообщение в списке чатов"""
        if user_id in self.chat_items:
            self.chat_items[user_id].update_last_message(text)


# ========== ЗАПУСК ==========
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor("#0e1621"))
    palette.setColor(QPalette.ColorRole.WindowText, QColor("#ffffff"))
    palette.setColor(QPalette.ColorRole.Base, QColor("#17212b"))
    palette.setColor(QPalette.ColorRole.Text, QColor("#ffffff"))
    palette.setColor(QPalette.ColorRole.Button, QColor("#2b5278"))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor("#ffffff"))
    app.setPalette(palette)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())