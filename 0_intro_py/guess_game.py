import random

# funções são def, como ele não possui chaves, identação é o segredo
def play():
    print("\n*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************\n")

    # variáveis em Python não são tipadas, nunca
    secret_number = random.randrange(1, 101)
    points = 1000

    # print já tem quebra de linha
    print("Defina o nível de dificuldade")

    # input é o scanf do Python, o que o usuário digita, vem como string
    # esse int na frente transforma a string em int
    level = int(input("(1)Fácil (2)Médio (3)Difícil"))

    # if pode ou não utilizar parenteses, elif = else if
    if level == 1:
        tries = 20
    elif level == 2:
        tries = 10
    else:
        tries = 5

    # ao invés de fazer int i = 0; i < tries; i++, ele utiliza esse run in range
    for run in range(tries):
        # {} é o %d do c, ele também aceita %d. Preenche com valores das variaveis
        print("\nTentativa {} de {}".format(run+1, tries))
        # versão estendida da linha 18
        guess_str = input("Qual o seu chute? (Entre 1 e 100): ")
        guess = int(guess_str)

        # é o mesmo que o if verificando se o valor é igual, maior ou menor.
        # a diferença é que agora, utilizam correct, bigger e smaller.
        # correct, bigger e smaller são variáveis booleanas
        correct = guess == secret_number
        bigger = guess > secret_number
        smaller = guess < secret_number

        if guess < 1 or guess > 100:
            print("Você deve digitar um número entre 1 e 100!")
            # o continue ele ignora o resto for e aumenta o valor for
            continue

        if correct:
            print("Acertô miseravi!")
            # break sai do laço, semelhante a outras linguagens
            break
        else:
            if bigger:
                print("Errrrooouuu! O seu chute foi maior que o número secreto.")
            elif smaller:
                print("Errrrooouuu! O seu chute foi menor que o número secreto.")

            # pega os pontos que o usuário tem, ele decrementa, abs é o módulo do número
            points -= abs(secret_number - guess)

    # outra versão da linha 31
    print(f"Pontuação: {points}")
    print("\nFim do Jogo!")


if __name__ == "__main__":
    play()