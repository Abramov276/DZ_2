import pathlib


def get_cats_info(path):
    cats_info = []

    with open(path, 'r') as cat:

        for line in cat:
            line = line.strip()
            cats = line.split(',')

            if len(cats) == 3:
                cats_dict = {
                    'id': cats[0],
                    'name': cats[1],
                    'age': cats[2]
                }
                cats_info.append(cats_dict)

            else:
                print(f'Помилка у рядку {line}')
    return cats_info


print(get_cats_info('cats.txt'))
