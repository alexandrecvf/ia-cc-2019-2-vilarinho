import sys

from PySide2 import QtCore
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QSpinBox


def dinheiro_pouco():
    dinheiro = dinheiro_sb.value()
    if dinheiro <= 30:
        return 1
    if 30 < dinheiro < 50:
        return (50 - dinheiro) / 20
    if dinheiro >= 50:
        return 0


def dinheiro_razoavel():
    dinheiro = dinheiro_sb.value()
    if dinheiro <= 30:
        return 0
    if 30 < dinheiro <= 50:
        return (dinheiro - 30) / 20
    if 70 > dinheiro > 50:
        return (70 - dinheiro) / 20
    if dinheiro >= 70:
        return 0


def dinheiro_adquado():
    dinheiro = dinheiro_sb.value()
    if dinheiro <= 50:
        return 0
    if 50 < dinheiro < 70:
        return (dinheiro - 50) / 20
    if dinheiro >= 70:
        return 1


def pessoal_insuficiente():
    pessoa = pessoas_sb.value()
    if pessoa <= 30:
        return 1
    if 30 < pessoa < 70:
        return (70 - pessoa) / 40
    if pessoa >= 70:
        return 0


def pessoal_satisfatorio():
    pessoa = pessoas_sb.value()
    if pessoa <= 30:
        return 0
    if pessoa >= 70:
        return 1
    if 30 < pessoa < 70:
        return (pessoa - 30) / 40


def regras(vet):  # RISCOS

    if dinheiro_pouco() > pessoal_insuficiente():
        alto = dinheiro_pouco()
    else:
        alto = pessoal_insuficiente()
    if dinheiro_pouco() < pessoal_satisfatorio():
        alto2 = dinheiro_pouco()
    else:
        alto2 = pessoal_satisfatorio()
    # Alto
    if alto < alto2:
        vet[2] = alto
    else:
        vet[2] = alto2
    # Medio
    if dinheiro_razoavel() < pessoal_satisfatorio():
        vet[1] = dinheiro_razoavel()
    else:
        vet[1] = pessoal_satisfatorio()
    # Baixo
    if dinheiro_adquado() < pessoal_satisfatorio():
        vet[0] = dinheiro_adquado()
    else:
        vet[0] = pessoal_satisfatorio()


def risco(valor):
    if 0 <= valor < 50:
        return 'Baixo'
    if 50 <= valor < 70:
        return 'Medio'
    if valor >= 70:
        return 'Alto'


def on_calcular_pushbutton_clicked():
    intervalos = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    vet = [0, 0, 0]
    regras(vet)

    print(vet)

    numerador = 0
    denominador = 0
    contador = 0
    j = 0

    for i in intervalos:
        if contador == 3 or contador == 6:
            j += 1

        contador += 1
        numerador += i * vet[j]
        denominador += vet[j]

    if denominador != 0:
        calc = numerador / denominador
    elif denominador == 0:
        calc = 1000

    print(calc)

    risco_label2.setText(risco(calc))


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    ui_file = QFile("logica_fuzzy.ui")
    ui_file.open(QFile.ReadOnly)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    dinheiro_label = window.findChild(QLabel, 'dinheiroLabel')
    pessoas_label = window.findChild(QLabel, 'pessoasLabel')
    risco_label = window.findChild(QLabel, 'riscoLabel')
    risco_label2 = window.findChild(QLabel, 'riscoLabel2')
    dinheiro_sb = window.findChild(QSpinBox, 'dinheiroSpinBox')
    pessoas_sb = window.findChild(QSpinBox, 'pessoasSpinBox')

    calcular_btn = window.findChild(QPushButton, 'calcularPushButton')
    calcular_btn.clicked.connect(on_calcular_pushbutton_clicked)

    window.show()

    sys.exit(app.exec_())
