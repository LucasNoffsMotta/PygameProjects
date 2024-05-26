import pygame

pygame.init()

def team_positions(name,n_linha,categoria,font):

    #equipe_casa = midright
    #equipe_fora = midleft

    linha = dict()

    #Posicoes na linha 1:
    linha1 = {
        'CASA':(300,100),
        'FORA':(520,100),
    }

    #Posicoes na linha 2:
    linha2 = {
        'CASA': (300, 140),
        'FORA': (520, 140),
    }

    linha3 = {
        'CASA': (300, 180),
        'FORA': (520, 180),
    }

    linha4 = {
        'CASA': (300, 220),
        'FORA': (520, 220),
    }

    linha5 = {
        'CASA': (300, 260),
        'FORA': (520, 260),
    }

    linha6 = {
        'CASA': (300, 300),
        'FORA': (520, 300),
    }

    linha7 = {
        'CASA': (300, 300),
        'FORA': (520, 300),
    }

    linhas = [linha1,linha2,linha3,linha4,linha5,linha6,linha7]
    linha = linhas[n_linha]


    #Definindo como sera a imagem de acordo com a categoria do item:

    name_surface = font.render(name, True, 'black')
    name_rect = name_surface.get_rect()

    for key,values in linha.items():
        if categoria in key:
            if 'CASA' in categoria:
                name_rect = name_surface.get_rect(midright = linha[key])
            else:
                name_rect = name_surface.get_rect(midleft=linha[key])


    return name_surface,name_rect

def cores_times(nome_time):

    cor_time = ' '

    cores = {'CORINTHANS':'white',
             'FLAMENGO':'red',
             'VASCO':'white',
             'FLUMINENSE':'green',
             'CRUZEIRO':'blue',
             'SANTOS':'white'

    }

    for keys,values in cores.items():
        if nome_time in keys:
            cor_time = values

    return cor_time


def variaveis_positions(n_linha,categoria,font,gol_casa,gol_fora,minutos):

    linha1 = {
    'Placar_casa': (365, 100),
    'Placar_fora': (450, 100),
    'Eventos': (780, 100)
    }

    linha2 = {
        'Placar_casa': (365, 140),
        'Placar_fora': (450, 140),
        'Eventos': (700, 140)
    }

    linhas = [linha1,linha2]

    linha = linhas[n_linha]


    if 'Placar_casa' in categoria:
        name_surface = font.render(f'{gol_casa}', True, 'black')
        name_rect = name_surface.get_rect(midright=linha['Placar_casa'])
        return name_surface, name_rect

    if 'Placar_fora' in categoria:
        name_surface = font.render(f'{gol_fora}',True,'black')
        name_rect = name_surface.get_rect(midleft=linha['Placar_fora'])
        return name_surface, name_rect


    if 'Eventos' in categoria:
        name_surface = font.render(f'Gol! {minutos}`min', True, 'black')
        name_rect = name_surface.get_rect(midleft=linha['Eventos'])
        return name_surface, name_rect










