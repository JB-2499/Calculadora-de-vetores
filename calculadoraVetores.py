print("1 = Soma | 2 = Produto escalar\n")

calculator = 0

def main ():
    #Escolher a operação:
    operation = 0
    repetitions = 0
    while operation == 0:
        try:
            operation = int(input("Qual operação deseja fazer? "))
        except:
            print("\nDigite um valor válido")

    #Soma:
    if operation == 1:
        while repetitions < 1:
            try:
                repetitions = int(input("Quantos vetores serão somados? "))
            except:
                print("\nDigite um valor válido")
        vectors = 0

        I = []
        J = []
        K = []

        #Definir os vetores:
        while vectors < repetitions:
            try:
                v = input("Digite os valores I J K do vetor: ").split()
                if len(v) > 0:
                    I.append(float(v[0]))
                else:
                    I.append(0.0)
                if len(v) > 1:
                    J.append(float(v[1]))
                else:
                    J.append(0.0)
                if len(v) > 2:
                    K.append(float(v[2]))
                else:
                    K.append(0.0)
                vectors += 1
            except:
                print("\nDigite um vetor válido")

        IF=JF=KF=0

        #Somar os vetores:
        for i in I:
            IF += i
        for j in J:
            JF += j
        for k in K:
            KF += k

        #verificar se há decimais:
        if IF - round(IF) == 0:
            IF = int(IF)
        if JF - round(JF) == 0:
            JF = int(JF)
        if KF - round(KF) == 0:
            KF = int(KF)

        print(f"\nO vetor resultante foi: {IF}i {JF}j {KF}k")

    #Multiplicação:
    if operation == 2:
        repetitions = 2
        vectors = 0
        cont = 0

        I = []
        J = []
        K = []

        #Definir os vetores:
        while vectors < repetitions:
            try:
                v = input("Digite os valores I J K do vetor: ").split()
                if len(v) > 0:
                    I.append(float(v[0]))
                else:
                    I.append(0.0)
                if len(v) > 1:
                    J.append(float(v[1]))
                else:
                    J.append(0.0)
                if len(v) > 2:
                    K.append(float(v[2]))
                else:
                    K.append(0.0)
                vectors += 1
            except:
                print("\nDigite um vetor válido")
                
        #multiplicar os vetores:
        valorFinal = (I[0] * I[1]) + (J[0] * J[1]) + (K[0] * K[1])

        if valorFinal - int(valorFinal) != 0:
            print(f"\nO valor resultante foi: {valorFinal:.2f}\n")
        else:
            print(f"\nO valor resultante foi: {valorFinal:.0f}\n")

main()

while calculator < 1:
    try:
        print("\n1 = Sim | 2 = Não")
        yesNo = int(input("Gostaria de executar outra operação? "))
        if yesNo == 2:
            calculator += 1
        else:
            main()
    except:
        print("\nDigite uma resposta válida")