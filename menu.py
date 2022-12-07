globalLista = []

class client:
    nome = str()
    cpf = str()
    cep = str()
    data = str()

def menuPrincipal():
    print(''' 
**** MENU PRINCIPAL ****

    [1] Cadastrar  
    [2] Listar Dados
    [3] Editar
    [4] Sugestão de Pacote  
    ''')

    while True: 
        m = str(input('Opção:'))
        if m != 1 or m != 2 or m != 3 or m != 4:
            break
        if m == 1:
            cadastar()
        if m == 2:
            listar()
        if m == 3:
            editar()
menuPrincipal()

def cadastar():
    person = client() #classe 
    person.nome = str(input("Digite seu nome:"))
    person.cpf = str(input('cpf:'))
    person.cep = str(input('cep:'))
    person.data = str(input('Data de nascimento:'))
    globalLista.append(person)
    
cadastar()
menuPrincipal()

 
def listar():

   for i in range(len(globalLista)):
    print(f'Nome:{globalLista[i].nome}')
    print(f'CPF:{globalLista[i].cpf}')
    print(globalLista[i].cep)
    print(globalLista[i].data)

listar()
menuPrincipal()
        
def editar():
    print('''
    [1] Nome
    [2] CPF
    [3] CEP
    [4] Data de nasciemento 
    ''')

    for i in range(1): 
        p = int(input('Opção que será editada:'))
        if p == 1:
            del globalLista[0] #deleta o que ta na posição 0 da lista 
            aq = str(input('Reescreva aqui:'))
            globalLista.insert(0, aq) #adicina na posição 0 
            print(globalLista) #so printa o nome editado da lista 
editar()


def menuSecundario():
    print('''
    ** EDITAR CARRINHO **
    [1] Remover item do carrinho
    [2] Ver descrição do carrinho
    [3] Escolher horário de instalação
    [4] Confirmar endereço
    [5] Finalizar compra
    ''')
    
    carrinhoEdit = int(input('Digite um número para continuar ou editar a compra: '))
    if carrinhoEdit == 1:
        
    


   