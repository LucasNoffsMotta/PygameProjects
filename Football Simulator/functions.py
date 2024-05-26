from random import randint

def Prog(m, x, p1, pc):

    #Variaveis:

    gol_casa = gol_fora = cartao_a_casa = cartao_a_fora = cartao_v_casa = cartao_v_fora = expulsos_casa = expulsos_fora = 0
    jogadores_p1 = 11
    jogadores_p2 = 11

    #Frases que aparecem no jogo:

    lista_frases_chute_errado = ['Isolou a bola!', 'Meu deus, que fase! Escorregou e errou o chute.',
                                 'Chutou fraco em cima do goleiro...']
    lista_frases_gols = ['Camisa 9 chutou de fora da area e fez um golaco!', 'Meu deus, que fase! Gol contra!',
                         'Gol de cabeca!', 'Golaco de falta!', 'Gol depois de linda tabela entra os atacantes!',
                         'Falha incrivel da defesa, atacante nao perdoou!']

    minutos_gol = []
    min_gols_time_casa = []
    min_gols_time_fora = []

    #Inicio do jogo:

    print(f'Jogo: {p1} x {pc}')

    #Definicao dos dois tempos:

    for d in range(0, 2):

        if d == 0:
            t = 'Primeiro tempo'

        elif d == 1:
            t = 'Segundo tempo'
            print('Fim do primeiro tempo.')
            minutos_gol.append(min_gols_time_casa)
            minutos_gol.append(min_gols_time_fora)
            sleep(x)
            print(f'Placar:\n{p1} - {gol_casa}\n{pc} - {gol_fora}')
            intervalo(p1,pc,gol_casa,gol_fora,cartao_a_casa,cartao_a_fora,cartao_v_casa,cartao_v_fora,jogadores_p1,jogadores_p2,minutos_gol)
            sleep(x)
            print('Inicio do segundo tempo!')
            sleep(4)

    #Inicio do jogo minuto a minuto:

        for c in range(1, 45 + m):
            frase_chute_errado = choice(lista_frases_chute_errado)
            frase_gol = choice(lista_frases_gols)

            print(f'{c}`min ')
            sleep(x)
            acao = jogo(p1, pc)

        #Acoes durante o jogo:

            if acao == 'gol':
                gol_casa += 1
                print(f'{frase_gol}', end=' ')
                print(f'Gol do {p1} aos {c}min do {t}!\n{p1}: {gol_casa}\n{pc}: {gol_fora}')
                min_gols_time_casa.append(c)


            elif acao == 'gol_fora':
                gol_fora += 1
                print(f'{frase_gol}', end=' ')
                print(f'Gol do {pc} aos {c}min do {t}!\n{p1}: {gol_casa}\n{pc}: {gol_fora}\n {c}`min.')
                min_gols_time_fora.append(c)


            elif jogadores_p1 > jogadores_p2:
                chance_gol = randint(0,500)
                if chance_gol < 5:
                    gol_casa += 1
                    print(f'{frase_gol}', end=' ')
                    print(f'Gol do {p1} aos {c}min do {t}!\n{p1}: {gol_casa}\n{pc}: {gol_fora}')
                    min_gols_time_casa.append(c)


            elif jogadores_p2 > jogadores_p1:
                chance_gol = randint(0,500)
                if chance_gol < 5:
                    gol_fora += 1
                    print(f'{frase_gol}', end=' ')
                    print(f'Gol do {pc} aos {c}min do {t}!\n{p1}: {gol_casa}\n{pc}: {gol_fora}')
                    min_gols_time_fora.append(c)

            elif acao == 'cartao_amarelo_casa':
                cartao_a_casa += 1
                print(f'Falta feia! Cartao amarelo para o jogador do {p1}')
                if cartao_a_casa > 1 and cartao_a_casa % 2 == 0:
                    print(f'Dois cartoes amarelos. Jogador do {p1} expulso aos {c}` min.')
                    expulsos_casa += 1
                    jogadores_p1 -= 1
                    cartao_v_casa +=1

            elif acao == 'cartao_vermelho_casa':
                cartao_v_casa += 1
                expulsos_casa += 1
                print(f'Falta criminosa! Cartao vermelho. Jogador do {p1} expulso aos {c}` min.')
                jogadores_p1 -= 1

            elif expulsos_casa > 4:
                print(f'Jogo encerrado por W.O, quatro jogadores expulsos. Vitoria do {pc}')
                break

            elif acao == 'cartao_amarelo_fora':
                cartao_a_fora += 1
                print(f'Falta feia! Cartao amarelo para o jogador do {pc}')
                if cartao_a_fora > 1 and cartao_a_fora % 2 == 0:
                    print(f'Dois cartoes amarelos. Jogador do {pc} expulso aos {c}` min.')
                    expulsos_fora += 1
                    jogadores_p2 -= 1
                    cartao_v_fora += 1

            elif acao == 'cartao_vermelho_fora':
                cartao_v_fora += 1
                expulsos_fora += 1
                jogadores_p2 -= 1
                print(f'Falta criminosa! Cartao vermelho. Jogador do {pc} expulso aos {c}` min.')

            elif expulsos_fora > 4:
                print(f'Jogo encerrado por W.O, quatro jogadores expulsos. Vitoria do {p1}')
                break

            elif acao == 'penalti_casa':

                penal = randint(0, 300)

                if penal < 150:
                    gol_casa += 1
                    print(f'PRIII! O juiz apita para a marca de penalti para o {p1}!')
                    sleep(2)
                    print('Jogador vai para a bola.')
                    sleep(1)
                    print('Ele bate forte e...')
                    sleep(1)
                    print(f'Goooooool! Placar:\n{p1}: {gol_casa}\n{pc}: {gol_fora}')
                    min_gols_time_casa.append(c)

                else:
                    print(f'PRIII! O juiz apita para a marca de penalti para o {p1}!')
                    sleep(2)
                    print('Jogador vai para a bola.')
                    sleep(1)
                    print('Ele bate forte e...')
                    sleep(1)
                    print('Bateu mal pra caramba, bola pra fora!')

            elif acao == 'penalti_fora':
                penal = randint(0, 300)
                if penal < 150:
                    gol_fora += 1
                    print(f'PRIII! O juiz apita para a marca de penalti para o {pc}!')
                    sleep(2)
                    print('Jogador vai para a bola.')
                    sleep(1)
                    print('Ele bate forte e...')
                    sleep(1)
                    print(f'Goooooool! Placar:\n{p1}: {gol_casa}\n{pc}: {gol_fora}')
                    min_gols_time_fora.append(c)

                else:
                    print(f'PRIII! O juiz apita para a marca de penalti para o {pc}!')
                    sleep(2)
                    print('Jogador vai para a bola.')
                    sleep(1)
                    print('Ele bate forte e...')
                    sleep(1)
                    print(f'{frase_chute_errado}!')


            elif c == 45:
                print(f'Acrecimos: {c} + {m - 1} min')

    sleep(2)
    print(f'Placar:\n{p1}:{gol_casa}\n{pc}:{gol_fora}')
    if gol_casa > gol_fora:
        print(f'Vitoria do {p1}')
        print('-_-'*30)
        return p1
    elif gol_casa < gol_fora:
        print(f'Vitoria do {pc}')
        print('-_-' *30)
        return pc

    else:
        print('Empate!')
        sleep(x)
        print('Disputa de penaltis!')
        vencedor = disputa_penaltis(p1,pc)
        return vencedor


def jogo(time_casa, time_fora):
    gol = gol_fora = cartao_amarelo_casa = cartao_amarelo_fora = cartao_vermelho_casa = cartao_vermelho_fora = penalti = 0

    tier1 = [
        'Flamengo',  # Brasil
        'Palmeiras',  # Brasil
        'River Plate',  # Argentina
        'Atletico Mineiro',  # Brasil
        'Nacional',  # Uruguai
        'Peñarol'  # Uruguai
    ]
    tier2 = [
        'Corinthans',  # Brasil
        'Fluminense',  # Brasil
        'Boca Juniors',  # Argentina
        'Independiente',  # Argentina
        'Estudiantes',  # Argentina
        'Athletico Paranaense',  # Brasil
        'Gremio',  # Brasil
        'Internacional',  # Brasil
        'Sao Paulo',  # Brasil
        'San Lorenzo',  # Argentina
        'Huracán',  # Argentina
        'Rosario Central',  # Argentina
        'Newell\'s Old Boys',  # Argentina
        'Vélez Sarsfield',  # Argentina
        'Lanús',  # Argentina
        'Banfield',  # Argentina
        'Argentinos Juniors',  # Argentina
        'Talleres',  # Argentina
        'Colón',  # Argentina
        'Godoy Cruz',  # Argentina
        'Unión',  # Argentina
        'Central Córdoba',  # Argentina
        'Aldosivi',  # Argentina
        'Arsenal de Sarandí',  # Argentina
        'Platense',  # Argentina
        'Sarmiento',  # Argentina
        'Defensa y Justicia'  # Argentina
    ]
    tier3 = [
        'Racing',  # Argentina
        'Cruzeiro',  # Brasil
        'Redbull Bragantino',  # Brasil
        'Botafogo',  # Brasil
        'Vasco',  # Brasil
        'Santos',  # Brasil
        'America Mineiro',  # Brasil
        'Bahia',  # Brasil
        'Atlético Nacional',  # Colômbia
        'Millonarios',  # Colômbia
        'América de Cali',  # Colômbia
        'Deportivo Cali',  # Colômbia
        'Independiente Santa Fe',  # Colômbia
        'Junior',  # Colômbia
        'Once Caldas',  # Colômbia
        'Deportes Tolima',  # Colômbia
        'Atlético Junior',  # Colômbia
        'Cúcuta Deportivo',  # Colômbia
        'Envigado',  # Colômbia
        'Patriotas Boyacá',  # Colômbia
        'Alianza Petrolera',  # Colômbia
        'Jaguares de Córdoba',  # Colômbia
        'Boyacá Chicó',  # Colômbia
        'Rionegro Águilas',  # Colômbia
        'La Equidad',  # Colômbia
        'Atlético Bucaramanga',  # Colômbia
        'Deportivo Pasto',  # Colômbia
        'Águilas Doradas',  # Colômbia
        'Danubio',  # Uruguai
        'Montevideo Wanderers',  # Uruguai
        'Cerro',  # Uruguai
        'Progreso',  # Uruguai
        'Liverpool',  # Uruguai
        'Boston River',  # Uruguai
        'Plaza Colonia',  # Uruguai
        'Fénix',  # Uruguai
        'Cerro Largo',  # Uruguai
        'Deportivo Maldonado',  # Uruguai
        'Rentistas',  # Uruguai
        'Torque',  # Uruguai
        'Villa Española',  # Uruguai
        'Deportivo Colonia',  # Uruguai
        'Rampla Juniors'  # Uruguai
    ]

    if time_casa in tier1 and time_fora in tier2:
        gol = randint(0, 500)
        gol_fora = randint(0, 1000)
        cartao_amarelo_casa = randint(0, 1000)
        cartao_amarelo_fora = randint(0, 600)
        cartao_vermelho_casa = randint(0, 1500)
        cartao_vermelho_fora = randint(0, 600)
        penalti = randint(0, 500)

    elif time_casa in tier1 and time_fora in tier3:
        gol = randint(0, 500)
        gol_fora = randint(0, 2000)
        cartao_amarelo_casa = randint(0, 1000)
        cartao_amarelo_fora = randint(0, 600)
        cartao_vermelho_casa = randint(0, 1500)
        cartao_vermelho_fora = randint(0, 600)
        penalti = randint(0, 500)

    elif time_casa in tier2 and time_fora in tier3:
        gol = randint(0, 500)
        gol_fora = randint(0, 2500)
        cartao_amarelo_casa = randint(0, 1000)
        cartao_amarelo_fora = randint(0, 600)
        cartao_vermelho_casa = randint(0, 1500)
        cartao_vermelho_fora = randint(0, 600)
        penalti = randint(0, 500)


    elif time_casa and time_fora in tier1 or time_casa and time_fora in tier2 or time_casa and time_fora in tier3:
        gol = randint(0, 1000)
        gol_fora = randint(0, 1000)
        cartao_amarelo_casa = randint(0, 1000)
        cartao_amarelo_fora = randint(0, 600)
        cartao_vermelho_casa = randint(0, 1500)
        cartao_vermelho_fora = randint(0, 600)
        penalti = randint(0, 500)

    if gol < gol_fora * 0.01:
        return 'gol'
    elif gol_fora < gol * 0.01:
        return 'gol_fora'
    elif cartao_amarelo_casa < 5:
        return 'cartao_amarelo_casa'
    elif cartao_vermelho_casa < 3:
        return 'cartao_vermelho_casa'
    elif cartao_amarelo_fora < 5:
        return 'cartao_amarelo_fora'
    elif cartao_vermelho_fora < 3:
        return 'cartao_vermelho_fora'
    elif penalti < 2:
        return 'penalti_casa'
    elif penalti > 498:
        return 'penalti_fora'


