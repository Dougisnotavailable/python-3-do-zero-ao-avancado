"""
Faça um programa que peça ao usuário para digitar um número entrada,
informe se este número é par ou ímpar. Caso o usuário não digite um número
entrada, informe que não é um número entrada.
"""
entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar is True:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
    
else:
    print("Você não digitou um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input('Digite a hora certa: ')

if horario.isdigit():
        horario_int = int(entrada)

        if horario_int <= 11:
             print('Bum dia')
        elif horario_int <= 17:
            print('Boas tardes')
        else:
             print('Boa noite')
                
else:
    print("Você não digitou um horário inteiro")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu nome: ')

if len(nome) < 5:
     print("Seu nome é curto")
elif len(nome) < 7:
     print("Seu nome é normal")
else:
     print("Seu nome é muito grande")
    