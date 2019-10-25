import sys

from Hebb import Hebb
from Perceptron import Perceptron

from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QLabel, \
    QPushButton, QAction, QSpinBox, QPlainTextEdit, QComboBox
from PySide2.QtCore import QFile

def testaBotao():
    w1.setText("0")
    w2.setText("0")
    wb.setText("0")

    texto = entrada.toPlainText()
    saidas = saida.toPlainText()

    saidasSplit = saidas.split('\n')

    print(saidasSplit)

    saidasInt = []
    for i in range(len(saidasSplit)):
        saidasInt.append(int(saidasSplit[i]))

    print(saidasInt)

    textoSplit1 = texto.split('\n')
    print(textoSplit1)
    qtdText = len(textoSplit1)
    qtdList = 0

    for i in range(len(textoSplit1[0])):
        if textoSplit1[0][i] != " ":
            qtdList = qtdList + 1

    print(qtdList)

    textoSplit2 = ""
    for i in range(qtdText):
        if i == qtdText - 1:
            textoSplit2 = textoSplit2 + textoSplit1[i]
        else:
            textoSplit2 = textoSplit2 + textoSplit1[i] + " "

    print(textoSplit2)

    textoSplit3 = textoSplit2.split()

    print(textoSplit3)

    inputs = []
    lista = []
    controle = 0
    for i in range(len(textoSplit3)):
        lista.append(int(textoSplit3[i]))
        controle = controle + 1
        if (controle == qtdList):
            inputs.append(lista)
            lista = []
            controle = 0

    print(inputs)


    if (funcao.currentText() == "Hebb"):
        hebb = Hebb()
        resp = hebb.learn(inputs, saidasInt)
        w1.setText(str(resp[0]))
        w2.setText(str(resp[1]))
        wb.setText(str(resp[2]))
        epoca.setText('')
        epocaText.setText('')
    else:
        perceptron = Perceptron()
        (resp, epocas) = perceptron.learn(inputs, saidasInt)
        w1.setText(str(resp[0]))
        w2.setText(str(resp[1]))
        wb.setText(str(resp[2]))
        epoca.setText(str(epocas))
        epocaText.setText("Épocas")

def botaoRodar():
    texto = rodarEntrada.toPlainText()
    valEntrada = texto.split()
    resp = 0
    aux = True
    for i in range(len(valEntrada)):
        resp = int(valEntrada[i]) + resp
        if aux and int(valEntrada[i]) <= 0:
            aux = False

    if (aux):
        resp = resp + 1

    print(resp)

    w_1 = int(w1.text())
    w_2 = int(w2.text())
    w_b = int(wb.text())

    if w_1 > 0 and w_2 > 0:
        resp = (resp * w_1 * w_2) + w_b
    else:
        resp = resp + w_b

    if resp > 0:
        respRodar.setText("1")
    elif resp <= 0:
        respRodar.setText("-1")

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    ui_file = QFile("hebb_perceptron.ui")
    ui_file.open(QFile.ReadOnly)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    entrada = window.findChild(QPlainTextEdit, "entradas")

    rodarEntrada = window.findChild(QPlainTextEdit, "rodarEntrada")

    saida = window.findChild(QPlainTextEdit, "saidas")

    funcao = window.findChild(QComboBox, "comboBox")

    w1 = window.findChild(QLabel, "w1")
    w2 = window.findChild(QLabel, "w2")
    wb = window.findChild(QLabel, "wb")
    epoca = window.findChild(QLabel, "epocas")
    epocaText = window.findChild(QLabel, "epocaText")
    respRodar = window.findChild(QLabel, "respRodar")

    treino = window.findChild(QPushButton, "treino")
    treino.clicked.connect(testaBotao)

    rodar = window.findChild(QPushButton, "rodar")
    rodar.clicked.connect(botaoRodar)

    window.show()

    sys.exit(app.exec_())