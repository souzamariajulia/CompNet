pacote1 = 0
pacote2 = 0
pacote3 = 0
def question1 ():
    print(''' 
**** Como você pretende usar sua internet? ****
    [A] Navegar em redes sociais  
    [B] Jogar on-line
    [C] Assistir séries/filmes ou ouvir música
    [D] Carregar e baixar arquivos
    ''')
    resp = str(input('escolha uma alternativa: '))
    print(resp)
    if resp == 'a':
        pacote1 += 1
    elif resp == 'b':
        pacote1 += 1
    elif resp == 'c':
        pacote2 += 1
    elif resp == 'd':
        pacote2 += 1


def question2 ():
    print(''' 
**** Quantos dispositivos estariam conectados na internet ao mesmo tempo? ****
    [A] 1 a 5  
    [B] 5 a 10
    [C] Mais de 10
    ''')
    resp = str(input('escolha uma alternativa: '))
    if resp == 'a':
        pacote1 += 1
    elif resp == 'b':
        pacote1 += 1
    elif resp == 'c':
        pacote2 += 1
    elif resp == 'd':
        pacote2 += 1

def question3 ():
    print(''' 
**** Você também procura um plano celular? ****
    [A] Sim 
    [B] Não
    ''')
    resp = str(input('escolha uma alternativa: '))
    if resp == 'a':
        pacote1 += 1
    elif resp == 'b':
        pacote1 += 1
    elif resp == 'c':
        pacote2 += 1
    elif resp == 'd':
        pacote2 += 1

def question4 ():
    print(''' 
**** Qual média de valor você gastaria de gastar? ****
    [A] Até 50 reais 
    [B] 100 a 200 reais
    [C] Acima de 200 reais
    ''')
    resp = str(input('escolha uma alternativa: '))
    if resp == 'a':
        pacote1 += 1
    elif resp == 'b':
        pacote1 += 1
    elif resp == 'c':
        pacote2 += 1
    elif resp == 'd':
        pacote2 += 1


def IA():

    if pacote1 > pacote2 and pacote1 > pacote3:
        print('o melhor pacote para você é o 1')
    elif pacote2 > pacote1 and pacote2 > pacote3:
        print('o melhor pacote para você é o 2')
    elif pacote3 > pacote1 and pacote3 > pacote2:
        print('o melhor pacote para você é o 3')



question1()
