print("bem vindo ao jogo")

numero_secreto = 42
totaldetentativas = 3
rodada = 1

for rodada in range(1, totaldetentativas):
    print("Tentativa {} de {}".format(rodada, totaldetentativas))
    chute_str = input("Digite seu numero: ")
    print("voce digitou " , chute_str)
    chute = int(chute_str)

    if(chute<1 or chute>100):
        print("voce deve digitar entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("acertou")
        break
    else:
        if(maior):
            print("chute foi maior")
        elif(menor):
            print("chute menor")



print("fim de jogo")