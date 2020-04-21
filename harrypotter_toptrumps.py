import random

import requests


def random_characterId():
    character_number = random.randint(1, 151)
    url = 'https://www.potterapi.com/v1/$2a$10$M.Hkzc4uzWuz0b5fdxFGjOdGC.QtM9rbi5gybUSwS2YsCjgnPIkKS/'.format(character_number)
    response = requests.get(url)
    character = response.json()

    return {
        'name': character['nameId'],
        'id: character['characterId'],
        'yearOfBirth': character['yearOfBirth'],
    }


def run():
    my_character = random_characterId()
    print('You were given {my_character["nameId"]}')
    stat_choice = input('Which stat do you want to use? (id) ')

    opponent_character = random_characterId()
    print('The opponent chose {}'.format(opponent_character['nameId']))

    my_stat = my_character[stat_choice]
    opponent_stat = opponent_character[stat_choice]

    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')


run()
