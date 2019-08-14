#importando as classes apropriadas do PySide2
from PySide2.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication([])

    label = QLabel("Hello World!")
    label.show()

    app.exec_()