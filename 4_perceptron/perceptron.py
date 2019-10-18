class Perceptron:

    def __init__(self):
        pass

    def learn(self, inputs, targets):
        w = [0, 0, 0]
        a = 1
        limiar = 0
        epoca = 0

        while (True):
            peso1 = w[0]
            peso2 = w[1]
            bias = w[2]

            for i in range(0, len(inputs)):
                yin = 0
                for j in range(0, len(inputs[i])):
                    yin += inputs[i][j] * w[j]
                yin += w[2]

                if yin > limiar:
                    y = 1
                elif yin < limiar:
                    y = -1
                else:
                    y = 0

                if y != targets[i]:
                    w[0] = w[0] + a * targets[i] * inputs[i][0]
                    w[1] = w[1] + a * targets[i] * inputs[i][1]
                    w[2] = w[2] + a * targets[i]

            epoca = epoca + 1

            if peso1 == w[0] and peso2 == w[1] and bias == w[2]:
                break
        return w, epoca


if __name__ == '__main__':
    h = Perceptron
    inputs = [[1, 1], [1, 0], [0, 1], [0, 0]]
    targets = [1, -1, -1, -1]

    (w, epoca) = h.learn(0, inputs, targets)

    print("PERCEPTRON")

    print("\nInputs", "\t", "Targets")
    for i in range(len(inputs)):
        print(inputs[i], "\t", targets[i])

    print("\nPesos: ")
    for i in range(len(w)-1):
        strw = "w" + str(i)
        print("\t", strw, "=", w[i])

    print("\t", "wb", "=", w[2])

    print("epocas: ", epoca)
