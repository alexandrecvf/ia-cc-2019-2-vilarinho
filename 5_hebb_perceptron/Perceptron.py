class Perceptron:

    def __init__(self):
        pass

    def learn(self, inputs, targets):
        w = [0, 0, 0]
        a = 1
        limiar = 0
        epoch = 0

        while(True):

            peso1 = w[0]
            peso2 = w[1]
            bias = w[2]

            for i in range(len(inputs)):
                yin = 0
                for j in range(len(inputs[i])):
                    yin += inputs[i][j] * w[j]
                yin += w[2]

                #print(yin)

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

                #print(w)
            epoch += 1
            if peso1 == w[0] and peso2 == w[1] and bias == w[2]:
                break

        return w, epoch


# if __name__ == '__main__':
#     h = Perceptron
#     inputs = [[1, 1], [1, 0], [0, 1], [0, 0]]
#     targets = [1, -1, -1, -1]
#
#     (a,epoch) = h.learn(0, inputs, targets)
#
#     print("Inputs     Targets")
#     resp = ''
#     espaco = ""
#     for i in range(len(inputs)):
#         resp = '['
#         for j in range(len(inputs[i])):
#             if (inputs[i][j] == 1):
#                 espaco = espaco + "  "
#
#             resp = resp + str(inputs[i][j])
#
#             if (j < len(inputs[i]) - 1):
#                 resp = resp + ', ' + espaco
#         resp = resp + ']       ' + str(targets[i])
#         espaco = ""
#         print(resp)
#
#     print('\nWeigths')
#     resp = ''
#     for i in range(len(a)):
#         if (i == len(a) - 1):
#             resp = '   wb = ' + str(a[i])
#         else:
#             resp = '   w' + str(i) + ' = ' + str(a[i])
#         print(resp)
#
#     print('\nEpoch:', epoch)
