import os
import sys
from qt_core import *
from gui.window.main_window.ui_mainWindow import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Graphic Interface")

        self.ui = ui_mainWindow()
        self.ui.setup_ui(self)

        # Connect toggle_button to toggle_button method
        self.ui.toggle_buttom.clicked.connect(self.toggle_button)

        # Connect buttons to their respective methods
        self.ui.btn_1.clicked.connect(self.show_page_1)
        self.ui.btn_2.clicked.connect(self.show_page_2)
        self.ui.settings_buttom.clicked.connect(self.show_page_3)

        self.show()

    def toggle_button(self):
        # Get the width of the sidebar menu:
        menu_width = self.ui.left_menu.width()

        # Check the width:
        width = 50
        if menu_width == 50:
            width = 240

        # Perform transition animation:
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page)
        self.ui.btn_1.set_active(True)

    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page)
        self.ui.btn_1.set_active(True)

    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.settings_buttom.set_active(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
