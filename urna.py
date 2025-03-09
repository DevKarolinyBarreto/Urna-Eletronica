# SEMPRE SALVAR NA URNA.PYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY CARAMBOLAAAAAAAAAAAAAAAAAAAAAAAAAS
# criar um dicionario para o segundo turno
# calcular com %


senha = int(input('Cadastre uma senha de números: '))      
confirme = int(input('Confirme a senha cadastrada: '))

def senhaC():
    global senha, confirme
    while confirme != senha:
        print('Senha incorreta, tente novamente!')
        confirme = int(input('Confirme a senha cadastrada: '))

def enter():
    global senha, confirme
    while True:
        senha_correta = int(input("Digite a senha cadastrada para iniciar a votação: "))
        if senha_correta != senha:
            print('Senha incorreta, tente novamente!')
        else:
            print('Acesso concedido!')
            break

senhaC()
enter()

candidatos = {}
votos = {}
nulos = 0
branco = 0

with open('urna.txt', 'a', encoding='utf-8') as arq:
    numeroC = int(input('Digite quantos candidatos deseja cadastrar: '))
    while numeroC == 0:
        print('Você precisa cadastrar um candidato! ')
        numeroC = int(input('Digite quantos candidatos deseja cadastrar: '))

    for i in range(numeroC):
        nome = input(f'Digite o nome do candidato {i+1}: ')
        numero = int(input(f'{nome}: Digite o número (chapa) do candidato: '))
        candidatos[numero] = nome
        votos[numero] = 0
        arq.write(f'{nome}, {numero}\n')

def opc():
    print('\n ********** OPÇÕES DE VOTAÇÃO **********')
    with open('urna.txt', 'r', encoding='utf-8') as arq2:
        opções = arq2.readlines()
        for linha in opções:
            print(linha.strip())

opc()

def votação():
    global nulos, branco

    jaca = int(input('Digite a chapa do candidato que deseja votar: '))

    if jaca in candidatos:
        votos[jaca] += 1
        print(f'Voto confirmado para {candidatos[jaca]} chapa {jaca}')
    elif jaca == 0:
        branco += 1
        print('Voto em branco registrado.')
    else:
        nulos += 1
        print('Chapa não encontrada, voto nulo registrado.')

while True:
    a = int(input('Deseja sair? 2 para sair ou qualquer número para continuar a votação: '))
    if a == 2:
        break

    enter()
    votação()

total = sum(votos.values()) + branco + nulos

def prim_turn():
    print("\n ********** RESULTADO DA VOTAÇÃO ********** ")

    global total
    for numero, nome in candidatos.items():
        perc = (votos[numero] / total) * 100 if total > 0 else 0
        print(f'{nome} (Chapa {numero}): {votos[numero]} votos ({perc:.2f}%)')

    perc_branco = (branco / total) * 100 if total > 0 else 0
    perc_nulos = (nulos / total) * 100 if total > 0 else 0

    print('\n'f'Votos em branco: {branco} ({perc_branco:.2f}%)')
    print(f'Votos nulos: {nulos} ({perc_nulos:.2f}%)\n')
 
prim_turn()

def seg_turn():

    if prim_turn > 50:
        return 

    ordem = sorted(votos.items(), key=lambda item: item[1], reverse=True)
    if len(ordem) < 2:
        print("Não há candidatos suficientes para um segundo turno.")
        return
    
    candidatos_segundo_turno = {
        ordem[0][0]: candidatos[ordem[0][0]],
        ordem[1][0]: candidatos[ordem[1][0]]
    }

    faltouluzzzz = {ordem[0][0]: 0, ordem[1][0]: 0}

    print("\n ********** CANDIDATOS SEGUNDO TURNO ********** ")
    for numero, nome in candidatos_segundo_turno.items():
        print(f"{nome} (Chapa {numero})")


    nulos2_turn = 0
    branquitos_2turn = 0

    while True:
        a = int(input('Deseja sair? 2 para sair ou qualquer número para continuar a votação: '))
        if a == 2:
            break
        enter()

        jaca = int(input('Digite a chapa do candidato que deseja votar: '))
        if jaca in candidatos_segundo_turno:
            faltouluzzzz[jaca] += 1
            print(f'Voto confirmado para {candidatos_segundo_turno[jaca]} chapa {jaca}')

        elif jaca == 0:
            branquitos_2turn += 1
            print('Voto em branco registrado.')
        else:
            nulos2_turn += 1
            print('Chapa não encontrada, voto nulo registrado.')


    total_segundo_turno = sum(faltouluzzzz.values()) + branquitos_2turn + nulos2_turn

    print("\n ********** RESULTADOS SEGUNDO TURNO ********** ")

    for numero, nome in candidatos_segundo_turno.items():

        perc = (faltouluzzzz[numero] / total_segundo_turno) * 100 if total_segundo_turno > 0 else 0
        print(f'{nome} (Chapa {numero}): {faltouluzzzz[numero]} votos ({perc:.2f}%)')

    perc_branco = (branquitos_2turn / total_segundo_turno) * 100 if total_segundo_turno > 0 else 0
    perc_nulos = (nulos2_turn / total_segundo_turno) * 100 if total_segundo_turno > 0 else 0

    print(f'\n Votos em branco: {branquitos_2turn} ({perc_branco:.2f}%)')
    print(f'Votos nulos: {nulos2_turn} ({perc_nulos:.2f}%) \n')

seg_turn()