import json

def save_score(score,level,file):

    try:
        with open(file,'r') as s:
            data = json.load(s)


    except (json.JSONDecodeError,FileNotFoundError):
        score_list = []
        level_list = []

        for _ in range(10):
            score_list.append(score)
            level_list.append(level)


        data = {
            'score_list': score_list,
            'level_list': level_list
        }

        with open(file,'w+') as s:
            json.dump(data, s)

    else:
        for key, items in data.items():
            if key == 'score_list':
                items.append(score)
            elif key == 'level_list':
                items.append(level)


        with open(file, 'w') as s:
            json.dump(data, s)
            s.close()


def load_score():
    try:
        with open('save_jason.json') as s:
            data = json.load(s)


    except (json.JSONDecodeError, FileNotFoundError):

        save_score(0,1,'save_jason.json')

        with open('save_jason.json') as s:
            data = json.load(s)

        for key, item in data.items():
            current_n = len(item)
            if current_n < 10:
                blank = 10 - current_n
                for _ in range(blank):
                    if key == 'level_list':
                        item.append(1)
                        item.sort(reverse=True)

                    elif key == 'score_list':
                        item.append(0)
                        item.sort(reverse=True)
            else:
                item.sort(reverse=True)

    else:

        for key, item in data.items():
            current_n = len(item)
            if current_n < 10:
                blank = 10 - current_n
                for _ in range(blank):
                    item.append(0)
                    item.sort(reverse=True)

            if current_n > 20:
                item.sort(reverse=True)
                item.pop(-1)

            else:
                item.sort(reverse=True)

    return data


#Test
# data_dict = load_score()
# print(data_dict)
#









