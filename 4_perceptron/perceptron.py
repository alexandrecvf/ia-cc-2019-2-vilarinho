class Perceptron:

    def __init__(self):
        pass

    def learn(self, inputs, targets):
        w = [0, 0, 0]
        a = 1
        limiar = 0

        for k in range(0, 2):
            for i in range(0, len(inputs)):
                yin = 0
                for j in range(0, len(inputs[i])):
                    yin += inputs[i][j] * w[j]
                yin += w[2]

                peso1 = w[0]
                peso2 = w[1]

                print(yin)

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

                print(w)

                if peso1 == w[0] and peso2 == w[1]:
                    break
        return w


if __name__ == '__main__':
    h = Perceptron
    inputs = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
    targets = [1, -1, -1, -1]

    print("Weights: ", h.learn(0, inputs, targets))
