import requests
from typing import List, Tuple

SW_API = 'https://swapi.co/api/'


class ApiError(Exception):
    pass


def get_planets_list() -> List[Tuple[str, int]]:
    """
    Возвращает список планет в виде [('Название', 'id')]
    """
    req = SW_API + 'planets/'
    planets = []
    while req is not None:
        resp = requests.get(req)
        if resp.status_code != 200:
            raise ApiError(resp.status_code)
        data = resp.json()

        for planet_data in data['results']:
            name = planet_data['name']
            url = planet_data['url']
            planet_id = int(url[:-1].split('/')[-1])
            planets.append((name, planet_id))
        req = data['next']

    return planets


def get_planet_data(planet_id: int) -> dict:
    """Возвращает информацию о планете с данным id
    Возвращаемые данные -  словарь в том же формате, в которому
    возвразаются данные с SW API
    https://swapi.co/documentation#planets
    """
    req = SW_API + f'planets/{planet_id}'
    resp = requests.get(req)
    if resp.status_code != 200:
        raise ApiError(resp.status_code)
    return resp.json()


def print_planet(planet_data: dict) -> None:
    """Принимает словарь с данными о планете
    Который вернула функция get_planet_data и выводит эти
    данные на экран с помощью print"""
    print(planet_data['name'].upper())
    print('=' * len(planet_data['name']))
    print('Поверхность {0}, климат {1}:'.format(planet_data['terrain'], planet_data['climate']))
    print('Сутки: {} час, год: {} дн, гравитация {}G'.format(
        planet_data['rotation_period'],
        planet_data['orbital_period'],
        planet_data['gravity']
    ))
    print("Население: {}".format(planet_data['population']))
    print()


if __name__ == '__main__':
    print('БАЗА ДАННЫХ ПЛАНЕТ STAR WARS')
    print('q - выход')
    print('l - список планет')
    cmd = ''
    while cmd != 'q':
        cmd = input('? ')
        try:
            if cmd == 'l':
                print('Получаю информацию...')
                planets = get_planets_list()
                planets = sorted(planets, key=lambda x: x[1])
                for name, planet_id in planets:
                    print(f'{planet_id}. {name}')
            elif cmd.isdigit():
                print('Получаю информацию...')
                planet_data = get_planet_data(int(cmd))
                print_planet(planet_data)
            elif cmd != 'q':
                print('Не понимаю. Введите q или номер планеты. l - для списка')
        except ApiError() as e:
            print(f'Ошибка! Код {e.args[0]}')
