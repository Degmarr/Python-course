import sys
from PyQt6.QtWidgets import QApplication, QWidget
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(350, 350)
    w.setWindowTitle("Meow")
    w.show()
    sys.exit(app.exec())