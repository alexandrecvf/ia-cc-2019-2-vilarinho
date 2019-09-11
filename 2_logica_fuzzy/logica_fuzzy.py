import sys, resource
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QLabel, \
    QPushButton, QAction
from PySide2.QtCore import QFile


def on_calcular_pushbutton_clicked():
    calcular_btn.setVisible(True)


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    ui_file = QFile("logica_fuzzy.ui")
    ui_file.open(QFile.ReadOnly)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    calcular_btn = window.findChild(QPushButton, 'calcularPushButton')
    calcular_btn.clicked.connect(on_calcular_pushbutton_clicked)

    window.show()

    sys.exit(app.exec_())