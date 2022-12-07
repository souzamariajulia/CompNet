import time
#ESQUEMA DE PONTOS
pacote1 = 0
pacote2 = 0 
pacote3 = 0
#PERGUNTAS
armazenar = []
pergunta1 = {
    'pergunta': 'Como você pretende usar sua internet?',
    'alternativas': {'a': ')  Navegar em redes sociais', 'b': ')  Jogar on-line', 'c': ')  Assistir séries/filmes ou ouvir música', 'd': ')  Carregar e baixar arquivos'},
}
pergunta2 = {
        'pergunta': 'Quantos dispositivos estariam conectados na internet ao mesmo tempo?',
        'alternativas': {'a': ')  1 a 5', 'b': ')  5 a 10', 'c': ')  Mais de 10'},
}
pergunta3 = {
        'pergunta': 'Você também procura um plano celular?',
        'alternativas': {'a': ')  Sim', 'b': ')  Não'},
}
pergunta4 = {
        'pergunta': 'Qual média de valor você gastaria de gastar?',
        'alternativas': {'a': ')  Até 50 reais', 'b': ')  100 a 200 reais', 'c': ')  Acima de 200 reais'},
}

#OPÇÕES
print("\033[1;33mOlá, vamos ajudar você na escolha da melhor oferta\033[m")
while True:
    print("""
    Instruções 
    Digite: I - Para acessar as instruções;
    Digite: C - Iniciar;
    Digite: S - Sair.
    """)
    
    instru = input("Escolha uma das opções acima: ").strip().upper()[0]
    if instru not in 'ICS':
        continue
    if instru in 'I':
        print("""
        PAINEL DE INSTRUÇÕES!
        Olá, seja bem-vindo(a) aos serviços da CompNet.
        Responda as seguintes perguntas para analisarmos qual o melhor serviço para você.
        """)
    elif instru in 'C':
        print("Iniciando serviço... ")
        for i in range(0, 2):
            print(i)
            time.sleep(0.50)
        break
    if instru in 'S':
        print('saindo do programa...')
        quit()

print("-="*10, " CompNet ", "-="*10)
for pk, pv in pergunta1.items():
    print(f"{pk}: {pv['pergunta']}")
    print()
    print("ALTERNATIVAS:")
    for ak, av in pv['alternativas'].items():
        print(f" {ak} {av}")
    print()
    while True:
        resposta_user = input("Escolha uma alternativa: ").strip()
        #if caso n tenha nas alternativas
        armazenar.append(resposta_user[0])
        if resposta_user in pv['alternativas'].keys():
            break

print('-='*30)
print('guardando respostas...')
print('-='*30)
time.sleep(1)
print(f'as respostas foram: {armazenar}')