
def caixaElet():
    print("\n**** CAIXA ELETRÔNICO ****\n")
    valor = int(input("Qual valor voce deseja sacar? "))

    if(valor < 10 or valor >600):
        print("Valor inválido.\n");
    else:
            
        cont100 = valor //100
        valor -= cont100 *100

        cont50 = valor //50
        valor -= cont50 *50

        cont10 = valor //10
        valor -= cont10 *10

        cont5 = valor //5
        valor -= cont5 *5

        cont1 = valor //1
        valor -= cont1 *1

        print(f"Total de notas \nNotas de R$ 100: {cont100} \nNotas de R$ 50: {cont50} \nNotas de R$ 10: {cont10} \nNotas de R$ 5: {cont5} \nNotas de R$ 1: {cont1} \n")
caixaElet();
