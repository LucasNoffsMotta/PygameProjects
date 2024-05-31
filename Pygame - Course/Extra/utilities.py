

def save_scores(score):
    points =str(score)
    with open('save_score.txt', 'a+') as file:
        file.write(points + '\n')
        file.close()

def append_scores():
    top_scores = list()
    with open('save_score.txt', 'r+') as file:
        line = file.readlines()
        for item in line:
            item.replace('\n','')
            top_scores.append(item)

    return top_scores


def read_scores(top_scores):
    lista_final = list()
    for score in top_scores:
        new_score = score.replace('\n','')
        lista_final.append(new_score)
    return lista_final


def ranking_pontos():
    top_scores = append_scores()
    scores_list = read_scores(top_scores)
    lista_ordenada = sorted(scores_list,reverse=True)
    pos = [(600,100),(600,150),(600,200)]
    if len(lista_ordenada) > 0:
        for count in range(0,len(lista_ordenada)):
            if count <=2:
                score_text_surf = font.render(f'{count +1} place:  {lista_ordenada[count]} points', False, (45,43,23))
                score_text_rect = score_text_surf.get_rect(center=(pos[count]))
                screen.blit(score_text_surf,score_text_rect)
