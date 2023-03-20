menu = ('Bem vindo a interface \n digite: \n [d] Depositar \n [s] Sacar \n [e] Extrato \n [q] Sair \n =>')

saldo = 0
limite = 500
extrato = ''
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == 'd':
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}'
        
        else:
            print('Operação falhou! O valor informado é inválido')
    
    elif opcao == 's':
        valor = float(input('Informe o valor de saque: '))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saque = numero_de_saques >= LIMITE_DE_SAQUES

        if excedeu_saldo:
            print('Operação falhou: Você não tem saldo suficiente!')
        
        elif excedeu_limite:
            print('Operação falhou: Valor excedeu limite de saque!')
        
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_de_saques += 1
        else:
            print('Operação falhou: O valor informado é inválido!')


    elif opcao == 'e':
        print('\n===========Extrato===========')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print("===============================")
    
    elif opcao == 'q':
        print('Sistema encerrado! ')
        break
    
    else:
        print('Operação inválida, porfavor selecione novamente a opção desejada.')
    

