#Codigos e funções

# O que vai ser inserido 
import math
def soma_vetores():
    print()
    print('Insira apenas Números!!! ')
    print()
    m1 = float(input('Qual o Modulo do Vetor: '))
    a1 = float(input('Qual o Angulo do Vetor em graus: '))
    print()
    y1 = m1 * math.sin(math.radians(a1))    #seno do vetor 1
    x1 = m1 * math.cos(math.radians(a1))    #cosseno do vetor 1

    y2 = 0
    x2 = 0
    r = 'S'
    while r == 'S':
        m2 = float(input('Digite o Modulo do Vetor: '))
        a2 = float(input('Digite o Ângulo do Vetor em graus: '))
        y2 = y2 + (m2 * math.sin(math.radians(a2)))    #seno do vetor 1
        x2 = x2 + (m2 * math.cos(math.radians(a2)))    #cosseno do vetor 1
        print()
        print('Deseja Somar mais um Vetor? ')
        r = str(input('Sim[S] - Não[N]: ' )).upper()
        if r == 'S':
            print()
        elif r == 'N':
            print()
            print('Ok!')
            print()
        else:
            print()
            print('Opção invalida')
            print('Para não perder os valores colocado até o momento. ')
            print('sera exibido o resultado da soma de todos os vetores. ')
            print()


    # Soma das componentes X e Y    

    sy = y1 + y2                  
    sx = x1 + x2                       



    # Modulo Resultante              
    
    mr = math.sqrt(sx ** 2 + sy ** 2)       



    # Como o programa esta configurado para aparecer somente 2 numeros após a virgula
    #então qualquer numero abaixo de 0.01 será considerado como 0.00 pelo programa,
    #ou seja, não vai possuir modulo resultante.
    if mr < 0.01:
        print('O vetor resultante é nulo!')
        print()

    else:

        # Ângulo Resultante

        ar = math.degrees(math.atan(sy/sx))     
        arn = ar * -1                           



        # Quadrantes

        q1 = (sy > 0) and (sx > 0)              #Quadrante1
        q2 = (sy > 0) and (sx < 0)              #Quadrante2
        q3 = (sy < 0) and (sx < 0)              #Quadrante3
        q4 = (sy < 0) and (sx > 0)              #Quadrante4




        # O que o programa vai exibir

        print('O Resultado da soma dos vetores é: ')
        print('Modulo: {:.2f}. '.format(mr))                 #Modulo Resultantes
            
        if q1:
            if ar < 0:
                print('Ângulo: {:.2f} Graus. '.format(arn))         #Ângulo Resultante
            else:
                print('Ângulo: {:.2f} Graus. '.format(ar))          #Ângulo Resultante
                
            print('Ele faz parte do 1º quadrante. ')                #Quadrante1

        elif q2 :
            if ar < 0:
                print('Ângulo: {:.2f} Graus. '.format(180 - arn))   #Ângulo Resultante
            else:
                print('Ângulo: {:.2f} Graus. '.format(180 - ar))    #Ângulo Resultante
                
            print('Ele faz parte do 2º quadrante. ')                #Quadrante2
                        
        elif q3 :
            if ar < 0:
                print('Ângulo: {:.2f} Graus. '.format(270 - arn))   #Ângulo Resultante
            else:
                print('Ângulo: {:.2f} Graus. '.format(270 - ar))    #Ângulo Resultante
                
            print('Ele faz parte do 3º quadrante. ')                #Quadrante3

        elif q4 :
            if ar < 0:
                print('Ângulo: {:.2f} Graus. '.format(360 - arn))   #Ângulo Resultante
            else:
                print('Ângulo: {:.2f} Graus. '.format(360 - ar))    #Ângulo Resultante
                
            print('Ele faz parte do 4º quadrante ')                 #Quadrante4




        # Componente X e Y no grafico para a localiação do sentido do vetor resultante

        print()
        print('As componentes do Vetor Resultante é: ')
        print('y = {:.2f}. '.format(sy))
        print('x = {:.2f}. '.format(sx))
        print()
        print('*Lembrando que o ângulo resultante é formado a partir do eixo +X no sentido ant horario ')
        print()



#instruções de como usar o programa
    
def instrucoes():
    print()
    print('1 - Insira Ângulos positivos de 0 à 360; ')

    print()
    print('2 - Os ângulos começam a contar a partir do eixo +X no sentido ant horário; ')

    print()
    print('3 - Se inserir números negativos o resultado poderá sair errado')
    print('    por isso verifique corretamente o ângulo do vetor.' )

    print()
    print('4 - Insira quantos vetores quiser e o programa vai calcular a soma deles. ')
    print()
