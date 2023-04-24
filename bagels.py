import random

MAX_DIGITOS = int(input("Digite o número máximo de dígitos: "))
MAX_TENTATIVAS = int(input("Digite o número máximo de tentativas: "))

def main():
    print('''
    Eu estou pensando em um número com {} dígitos distintos.
    Veja se você consegue adivinhá-lo.
    Aqui vão algumas dicas.
    Quando eu disser:       Eu quero dizer:
        Fermi                   Um dos dígitos está na posição correto;
        Pico                    Um dos dígitos está correto, mas na posição errada;
        Bagels                  Nenhum dos dígitos está correto;

    Por exemplo, se o número secreto fosse 287 e você dissesse 784, a dica seria Fermi Pico.

    Vocẽ tem {} tentativas.

    Boa sorte!
    '''.format(MAX_DIGITOS, MAX_TENTATIVAS))

    while True:
        num_secreto = obter_num_secreto()
        num_tentativas = 1
        while num_tentativas <= MAX_TENTATIVAS:
            num_tentado = ''
            while len(num_tentado) < MAX_DIGITOS or not num_tentado.isdecimal():
                print(f"Tentativa {num_tentativas}")
                num_tentado = input("> ")
            num_tentativas += 1

            dicas = obter_dicas(num_tentado, num_secreto)
            print(dicas)

            if num_tentado == num_secreto:
                break

            if num_tentativas > MAX_TENTATIVAS:
                print("Você ultrapassou o limite de tentativas.")
                print(f"A resposta era {numero_secreto}.")
            
        print("Deseja jogar novamente? (sim/não)")
        if not input("> ").lower().startswith('s'):
            break

    print("Obrigado por jogar!")

def obter_num_secreto():
    lista_nums = list('0123456789')
    random.shuffle(lista_nums)

    num_secreto = ''
    for i in range(MAX_DIGITOS):
        num_secreto += lista_nums[i]
    print(num_secreto)
    return num_secreto

def obter_dicas(num_tentado, num_secreto):
    if num_tentado == num_secreto:
        return "Parabéns! Você acertou!"

    dicas = []

    for i in range(len(num_tentado)):
        if num_tentado[i] == num_secreto[i]:
            dicas.append("Fermi")
        elif num_tentado[i] in num_secreto:
            dicas.append("Pico")

    if len(dicas) == 0:
        return "Bagels"
    else:
        dicas.sort()
        return ' '.join(dicas)

main()
            
