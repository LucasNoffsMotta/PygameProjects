import json
from player import PlayerData
from text_display import TextObject

def save_data(name,score,level,gems):
    data = {'name': name,
            'score':score,
            'level':level,
            'gems':gems
    }


    try:
        with open('save.json','r') as r:
            current_saved = json.load(r)
        r.close()
        current_saved.append(data)

        with open('save.json', 'w') as d:
            json.dump(current_saved,d)
        d.close()


    except (json.JSONDecodeError,FileNotFoundError):
        players = [data]
        with open('save.json', 'a+') as d:
            json.dump(players,d)
        d.close()


def load_data(screen):
    players = []
    pos1 = [300,300]
    with open('save.json', 'r') as d:
        data = json.load(d)
    
    for player in data:
        players.append(PlayerData(player['name'], player['score'], player['level'], player['gems'],screen,pos1))
        
    players.sort(reverse=True)

    for player in players:
        player.pos1 = [pos1[0], pos1[1]]
        pos1[0] = pos1[0] + 200

    print(pos1)
    return players




def get_sorted_players(players):
    return players.sort()

        
