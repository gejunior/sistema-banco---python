from datetime import datetime

class Conta:

    saldo, saque_diario = 0
    saques, depositos = []
    transacao_diaria = {}
    limite_transacoes = 10

    def transacao():
        global transacao_diaria
        global limite_transacoes

        data_atual_obj = datetime.now()
        data_atual_str = data_atual_obj.strftime("%Y/%m/%d")
        
        num_transacoes_hj = transacao_diaria.get(data_atual_str, 0)

        if(num_transacoes_hj < limite_transacoes):
            transacao_diaria[data_atual_str] = num_transacoes_hj + 1
            print("Transacao feita com sucesso!")
        else:
            print("Erro, limite de transações atingido")


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
    transacao()
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