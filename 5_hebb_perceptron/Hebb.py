class Hebb:
    def __init__(self):
        pass

    def learn(self, inputs,  targets):
        w = [0,0,0]
        #inputs[0]#inputs[0:4]#[x[0] for x in inputs]
        #print(len(inputs))
        for i in range(len(inputs)):
            for j in range(len(inputs[i])):
                w[j] = w[j] + inputs[i][j] * targets[i]
            w[2] = w[2] + targets[i]
            #print(w)
        return w


# if __name__ == '__main__':
#     h = hebb
#     inputs = [[1,1], [1,-1], [-1,1], [-1,-1]]
#     targets = [1,-1,-1,-1]
#
#     a = h.learn(0,inputs,targets)
#
#     print("Inputs     Targets")
#     resp = ''
#     for i in range(len(inputs)):
#         resp = '['
#         for j in range(len(inputs[i])):
#             resp = resp + str(inputs[i][j])
#
#             if (j < len(inputs[i]) - 1):
#                 resp = resp + ', '
#         resp = resp + ']        ' + str(targets[i])
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

