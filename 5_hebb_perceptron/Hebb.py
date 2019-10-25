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