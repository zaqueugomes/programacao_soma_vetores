#MENU - Soma de vetores
import model
opcao = 1
print()
print('Caso não saiba usar o programa')
print('leia antes as instruções! ')
while opcao != '3':
    print()
    print('Escolha uma opção abaixo: ')
    opcao = input('[1] Soma de Vetores - [2] Instruções - [3] Encerrar o Programa ')
    if opcao == '1':
        model.soma_vetores()

        
    elif opcao == '2':
        model.instrucoes()
        
        
    elif opcao == '3':
        print('saindo do programa')


    else:
        print()
        print('Opção Invalida, leia atentamente e coloque a opção correta! ')
        print()



