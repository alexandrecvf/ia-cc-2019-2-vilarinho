class Hebb:
    def __init__(self, training_set):
        self.training_set = training_set

    def train(self):
        inputs = len(self.training_set[0][0])

        pesos = []

        for i in range(inputs+1):
            pesos.append(0)

        for ts in self.training_set:
            input_list = list(ts[0])
            target = ts[1]

            input_list.append(1)

            for i in range(len(pesos)):
                pesos[i] = pesos[i] + input_list[i] * target
        return pesos

    def print(self, pesos):
        print("Inputs \t\t Target")

        for ts in self.training_set:
            print(ts[0], "\t\t", ts[1])

        print("\nPesos:")
        for w in range(len(pesos)-1):
            print("\tw" + str(w) + " = " + str(pesos[w]))
        print("\twb = " + str(pesos[-1]))

if __name__ == '__main__':
    hebb = Hebb([([1, 1], 1), ([1, -1], -1), ([-1, 1], -1), ([-1, -1], -1)])
    hebb.print(hebb.train())
