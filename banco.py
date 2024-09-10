class ContaBancaria:
    def __init__(self, numero_conta, titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0.0
        self.extrato = []
        self.saques_diarios = 0
        self.limite_saques = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor and self.saques_diarios < self.limite_saques:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.saques_diarios += 1
            print("Saque realizado com sucesso!")
        else:
            if valor > self.saldo:
                print("Saldo insuficiente.")
            elif self.saques_diarios >= self.limite_saques:
                print("Limite de saques diários atingido.")
            else:
                print("Valor inválido para saque.")

    def extrato(self):
        print("\n===== Extrato Bancário =====")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("=============================")

# Criando uma conta
conta = ContaBancaria(12345, "João da Silva")

while True:
    # Menu de opções para o usuário
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        conta.depositar(valor)
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        conta.sacar(valor)
    elif opcao == "e":
        conta.extrato()
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")