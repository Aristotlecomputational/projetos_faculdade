#Por que a combinação de uma lista contendo dicionários é uma excelente escolha arquitetural para este problema específico?
#Resposta da primeira questão: Porque é uma forma inteligente e funcional de armazenar os dados, organizando-os de modo
#coeso, no intuito de poder acessar as suas variáveis sem nenhuma dor de cabeça.
#Em qual momento do seu código o uso de um laço while se mostrou mais adequado que um laço for?
#Resposta da segunda pergunta: no momento em que não era possível determinar a quantidade de vezes que aquela determinada
#linha deveria rodar ou não, haja vista que o for detém um número delimitado de iterações.
#Como você garantiu que o programa não "quebrasse" se o usuário digitasse o nome de um aluno que não existe no sistema?
#Resposta da terceira pergunta: Eu fiz uma verificação a partir da utilização do for, isto é, verifiquei se o aluno está
#ou não na turma, pegando um variável de controle e comparando o nome digitado num if condicional.
def menu():
    print('=' * 50) 
    print('DIGITE 1 PARA ADICIONAR UM NOVO ALUNO.')
    print('DIGITE 2 PARA REGISTRAR UMA NOTA.')
    print('DIGITE 3 PARA CALCULAR MÉDIA E STATUS.')
    print('DIGITE 4 PARA ESTATÍSTICAS RÁPIDAS.')
    print('DIGITE 5 PARA SAIR DO PROGRAMA.')
    print('DIGITE 6 PARA REGISTRAR FALTAS.')
    print('DIGITE 7 PARA REMOVER UM ALUNO.')
    print('=' * 50)

print('BEM-VINDO AO SISTEMA ACADÊMICO!')
turma = []

while True:
    menu()
    try:
        opcao = int(input("\nDigite uma opção: > "))
    except ValueError:
        print('Opção inválida! Digite um número.')
        continue

    if opcao == 1:
        nome = input('\nDigite o nome do aluno: ').upper()
        aluno_ha = False
        for aluno in turma:
            if aluno['nome'] == nome:
                aluno_ha = True
                break
        if aluno_ha:
            print('Esse aluno já está cadastrado! Tente novamente.')
        else:
            aluno = {'nome': nome, 'notas': [], 'faltas': 0}
            turma.append(aluno)
            print(f'O aluno {nome} foi cadastrado com sucesso')

    elif opcao == 2:
        if not turma:
            print('Não há alunos cadastrados! Cadastre os alunos primeiro.')
        else:
            nome = input('\nInsere o nome do aluno: ').upper()

            aluno_encontrado = None
            for aluno in turma:
                if aluno['nome'] == nome:
                    aluno_encontrado = aluno
                    break

            if not aluno_encontrado:
                print('Aluno não encontrado!')
            else:

                while True:
                    try:
                        nota = float(input('\nDigite uma nota do aluno (0 a 10): '))
                        if 0 <= nota <= 10:
                            aluno_encontrado['notas'].append(nota)
                            print('Nota adicionada com sucesso!')
                            break
                        else:
                            print('Nota inválida! Digite um valor entre 0 e 10.')
                    except ValueError:
                        print('Entrada inválida! Digite um número.')

    elif opcao == 3:
        if not turma:
            print('\nNão há alunos cadastrados! Adicione um aluno primeiro.')
        else:
            nome = input('\nInsere o nome do aluno: ').upper()

            aluno_encontrado = None
            for aluno in turma:
                if aluno['nome'] == nome:
                    aluno_encontrado = aluno
                    break

            if not aluno_encontrado:
                print('\nAluno não encontrado!')
            else:

                if aluno_encontrado['faltas'] > 10:
                    print(f'\nALUNO REPROVADO POR FALTAS! ({aluno_encontrado['faltas']} faltas)')
                    print(f'Aluno: {aluno_encontrado['nome']}')
                    print(f'Faltas: {aluno_encontrado['faltas']}')
                    if aluno_encontrado['notas']:
                        print(f'Notas: {aluno_encontrado['notas']}')
                else:
                    if not aluno_encontrado['notas']:
                        print('\nEste aluno ainda não possui notas cadastradas, caríssimo!')
                        print(f'Faltas: {aluno_encontrado["faltas"]}')
                    else:
                        media = sum(aluno_encontrado['notas']) / len(aluno_encontrado['notas'])

                        if media >= 9:
                            print('A (Excelente)')
                        elif media >= 7:
                            print('B (Bom)')
                        elif media >= 5:
                            print('C (Regular)')
                        else:
                            print('D (Insuficiente)')


                        if media >= 7 and aluno_encontrado['faltas'] <= 10:
                            print('APROVADO!')
                        else:
                            print('REPROVADO!')

    elif opcao == 4:
        if not turma:
            print('\nNão há alunos cadastrados! Adicione um aluno primeiro.')
        else:
            todas_notas = []
            for aluno in turma:
                todas_notas.extend(aluno['notas'])

            if not todas_notas:
                print('\nNenhum aluno possui notas cadastradas!')
            else:
                print("ESTATÍSTICAS DA TURMA")
                print('Maior nota da turma: {}'.format(max(todas_notas)))
                print('Menor nota da turma: {}'.format(min(todas_notas)))
                print('Média da turma: {:.2f}'.format(sum(todas_notas) / len(todas_notas)))
    elif opcao == 5:
        print('\nPrograma terminado. Até mais!')
        break

    elif opcao == 6:
        if not turma:
            print('\nNão há alunos. Adicione um aluno primeiro.')
        else:
            nome = input('\nInsere o nome do aluno: ').upper()
            aluno_encontrado = None
            for aluno in turma:
                if aluno['nome'] == nome:
                    aluno_encontrado = aluno
                    break
            if not aluno_encontrado:
                print('Aluno inexistente!')
            else:
                faltas = int(input('Registre o número de faltas do aluno: '))
                aluno_encontrado['faltas'] = faltas
                if aluno_encontrado['faltas'] > 10:
                    print('Reprovado por falta!')
                else:
                    print('Falta(s) registrada(s)')
                    aluno_encontrado['faltas'] = faltas

    elif opcao == 7:
        if not turma:
            print('\nNão há turma!')
        elif turma:
            nome = input('\nInsere o nome do aluno: ').upper()
            aluno_encontrado = None
            for aluno in turma:
                if aluno['nome'] == nome:
                    aluno_encontrado = aluno
                    pergunta = input('Tens certeza de que vais removê-lo? (S/N)? ').upper()
                    if pergunta == 'S':
                        print('O aluno {} foi removido com sucesso!'.format(aluno['nome']))
                        turma.remove(aluno)
                        print('Turma: {}'.format(turma))
                    elif pergunta == 'N':
                        print('O aluno não foi removido.')
                        print('Turma: {}'.format(turma))
                    else:
                        print('Comando errado!')
                else:
                    print('Aluno inexistente!')
                    continue
    else:
        print('Opção inválida! Digite um número entre 1 e 7.')
    