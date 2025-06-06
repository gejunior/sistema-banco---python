#criar um sistema bancario com as operações: sacar, depositar e visualizar extrato

#Exercicio:
#Fomos contratados por um grande banco para desenvolver o seu novo sistema. 
# Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. 
# Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

#Deposito
#Deve ser possível depositar valores positivos para a minha conta bancária. 
# A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar 
# em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser 
# armazenados em uma variável e exibidos na operação de extrato.

#Saques
#O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. 
# Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que 
# não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados 
# em uma variável e exibidos na operação de extrato.

#Operação de extrato
#Essa operação deve listar todos os depósitos e saques realizados na conta. 
# No fim da listagem deve ser exibido o saldo atual da conta.
#Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
#1500.45 = R$ 1500.45

saldo = 0
saques = []
saque_diario = 0
depositos = []

def depositar(valor):
    global saldo
    if valor > 0.0:
        saldo += valor
        depositos.append(valor)

def sacar():
    global saque_diario, saldo, saques
    if saque_diario >= 3:
        print("Limite de saque diario atingido!")
        return
    else:
        valor = float(input("Digite o valor do saque: R$ "))
        
        if valor < 0:
            print("Valor inválido para saque.")
            return
    
        elif valor > saldo or saldo <= 0:
            print("Saldo insuficiente.")
            return

        elif valor > 500:
            print("Limite de apenas R$ 500,00")
            return
        else:
            print(f"Saque de {valor:.2f} realizado com sucesso!")
            saque_diario += 1
            saques.append(valor)
            saldo -= valor

def extrato():
    print("Extrato:".center(15, "="))
    print("Depósitos:")
    for deposito in depositos:
        print(f"R$ {deposito:.2f}")
    print("Saques:")
    for saque in saques:
        print(f"R$ {saque:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}")

def menu():
    op = 0
    print("Menu".center(15))
    print("[1] depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[0] Sair")
    op = int(input("Opcao: "))
    return op

def main():
    print("Bem-vindo ao sistema bancário!")
    
    while True:
        op = menu()
        match op:
            case 1:
                valor = float(input("Digite o valor do depósito: R$ "))
                depositar(valor)
            case 2:
                sacar()
            case 3:
                extrato()
            case 0:
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida, tente novamente.")
    print("Obrigado por usar nosso sistema bancário!")

main()