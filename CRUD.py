#Tentativa 1 - CRUD
opc = ''
cad = {}
prod = {}
#Menu principal
while opc != 0:
    print("""
[1] Cadastrar
[2] Clientes
[3] Motos
[4] Vendas
[0] Sair
    """)
    opc = int(input('Digite uma opção:'))
    if opc == 1:

        while opc != 0:
            print("""
[1] Cadastrar Cliente
[2] Cadastrar Moto
[0] Sair
            """)
            opc = int(input('Digite uma opção:'))
            if opc == 1:

                t = 'A'
                while True: #Cadastro Perfil Cliente
                    print('\nAdicione um novo Cliente\n')
                    Cliente = []
                    nome = ''
                    cpf = ''
                    tel = ''

                    nome = input('Nome do cliente: ')
                    if nome in cad:
                        print('Nome já cadastrado!')
                    else:
                        Cliente.append(nome)
                        cpf = input ('CPF: ')
                        Cliente.append(cpf)
                        tel = input ('Telefone: ')
                        Cliente.append(tel)


                        cad[f'{nome}'] = Cliente[1:]

                    #Exibir cadastro
                    print(f'{"":-<57}')
                    print(f'{"Nome": <19} {"CPF": <19} {"Telefone": <19}')
                    print(f'{"":-<57}')

                    for x, y in cad.items():
                        print(f'{x: <20}{y[0]: <20}{y[1]: <20}')

                    while True:
                        t = input('\n\nDeseja continuar? [S/N]: ')

                        if t[0] in 'Nn':
                            break
                        elif t[0] in 'Ss':
                            break
                        else:
                            print('Dígito inválido!')


                    if t[0] in 'Nn':
                        break

            if opc == 2:

                while True: #Cadastro Produto
                    print('\nAdicione um novo produto\n')
                    Produto = []
                    Moto = ''
                    Modelo = ''
                    Pot = ''

                    Moto = input('Nome da Moto: ')
                    if Moto in prod:
                        print('Moto já cadastrada!')
                    else:
                        Produto.append(Moto)
                        Modelo = input ('Modelo: ')
                        Produto.append(Modelo)
                        Pot = input ('Potência: ')
                        Produto.append(Pot)


                        prod[f'{Moto}'] = Produto[1:]

                    #Exibir cadastro
                    print(f'{"":-<57}')
                    print(f'{"Moto": <19} {"Modelo": <19} {"Potência": <19}')
                    print(f'{"":-<57}')
                    for x, y in prod.items():
                        print(f'{x: <20}{y[0]: <20}{y[1]: <20}')

                    while True:
                        t = input('\n\nDeseja continuar? [S/N]: ')

                        if t[0] in 'Nn':
                            break
                        elif t[0] in 'Ss':
                            break
                        else:
                            print('Dígito inválido!')
                            exit()

                    if t[0] in 'Nn':
                        break

            if opc == 0:
                opc = ''
                break

    if opc == 2:
        while opc != 0:
            print("""
[1] Exibir todos os clientes
[2] Consultar cliente
[3] Excluir cliente
[0] Sair
            """)
            opc = int(input('Digite uma opção:'))

            if opc == 1:
                if cad == {}:
                    print(f'{"":-<57}')
                    print(f'{"Nome": <19} {"CPF": <19} {"Telefone": <19}')
                    print(f'{"":-<57}')
                    print('Cadastro vazio')
                else:
                    # Exibir cadastro
                    print(f'{"":-<57}')
                    print(f'{"Nome": <19} {"CPF": <19} {"Telefone": <19}')
                    print(f'{"":-<57}')
                    for x, y in cad.items():

                        print(f'{x: <20}{y[0]: <20}{y[1]: <20}')

            if opc == 3:
                if cad == {}:
                    print(f'{"":-<57}')
                    print(f'{"Nome": <19} {"CPF": <19} {"Telefone": <19}')
                    print(f'{"":-<57}')
                    print('Cadastro vazio')
                else: #Modo Exclusão de item chave
                    # Exibir cadastro
                    print(f'{"":-<57}')
                    print(f'{"Nome": <19} {"CPF": <19} {"Telefone": <19}')
                    print(f'{"":-<57}')
                    for x, y in cad.items():

                        print(f'{x: <20}{y[0]: <20}{y[1]: <20}')

                    excluir = input('\nDigite o nome do Cliente que deseja excluir: ')
                    if excluir in cad:
                        del(cad[excluir])
                        print(f'Cliente {excluir} excluído!')
                    else:
                        print('Não existe!')

            if opc == 0:
                opc = ''
                break
    if opc == 3:
        while opc != 0:
            print("""
[1] Exibir todas as motos
[2] Consultar moto
[3] Excluir moto
[0] Sair
            """)
            opc = int(input('Digite uma opção:'))

            if opc == 1:
                if prod == {}:
                    print(f'{"":-<57}')
                    print(f'{"Moto": <19} {"Modelo": <19} {"Potência": <19}')
                    print(f'{"":-<57}')
                    print('Cadastro vazio')
                else:
                    # Exibir cadastro
                    print(f'{"":-<57}')
                    print(f'{"Moto": <19} {"Modelo": <19} {"Potência": <19}')
                    print(f'{"":-<57}')
                    for x, y in prod.items():

                        print(f'{x: <20}{y[0]: <20}{y[1]: <20}')

            if opc == 3:
                if prod == {}:
                    print(f'{"":-<57}')
                    print(f'{"Moto": <19} {"Modelo": <19} {"Potência": <19}')
                    print(f'{"":-<57}')
                    print('Cadastro vazio')
                else: #Modo Exclusão de item chave
                    # Exibir cadastro
                    print(f'{"":-<57}')
                    print(f'{"Moto": <19} {"Modelo": <19} {"Potência": <19}')
                    print(f'{"":-<57}')
                    for x, y in prod.items():
                        print(f'{x: <20}{y[0]: <20}{y[1]: <20}')

                    excluir = input('\nDigite o nome da moto que deseja excluir: ')
                    modeloExc = input('Digite o modelo: ')
                    if excluir in prod:
                        del(prod[excluir])
                        print(f'Moto {excluir} excluído!')
                    else:
                        print('Não existe no estoque!')

            if opc == 0:
                opc = ''
                break
