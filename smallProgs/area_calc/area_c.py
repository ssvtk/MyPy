from area_calc.figures_classes import Circle, Triangle, Rect


def file_parse_list(file):
    with open(file, mode='r', encoding='utf-8') as f:
        content = [line.strip().split(',') for line in f.readlines()]
        return content


def create_figure(type_figure, params):
    if type_figure == 'Circle':
        return Circle(params)
    elif type_figure == 'Rect':
        return Rect(params)
    elif type_figure == 'Triangle':
        return Triangle(params)

    else:
        print('Неверные параметры фигур')


if __name__ == "__main__":

    top_areas = {}
    for element in file_parse_list('figures.txt'):
        top_areas[create_figure(element[0], element[1:]).area()] = element[0]
        print(create_figure(element[0], element[1:]))

    print(f'\n\t\t\t\t Total Area: {sum(top_areas.keys())}')
    print(f'\nTop Areas:')
    for max_area, max_area_figure in sorted(top_areas.items())[-5:]:
        print(f'{max_area} ----> {max_area_figure}')
