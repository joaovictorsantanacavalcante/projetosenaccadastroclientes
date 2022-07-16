import cliente

inforcliete=[]
verificar=0
print('seja bem vindo ao cadastro  e informaçoes de clientes de clientes!')



verificar=int(input('DIGITE (1) PARA CADASTRAR NOVO CLIENTE OU (2) PARA ACESSAR DADOS DE CLIENTES JA CADASTRADO E (3) PARA PARA'))

while(verificar!=3):
 if verificar==1:
    inforcliete.append(input('digite o nome completo de cliente'))
    nascimento=input('data de nascimento de cliente')
    objetocliente=cliente.Cliente( 'nomecli', 'datanascimento', 'cpf', 'email', 'endereço', 'divida')


