import requests
from bs4 import BeautifulSoup

x = int(input('Введите номер страницы для парсинга\n'))
source = requests.get(f'https://groupprice.ru/brands/dstrend/comments?page={x}').text
soup = BeautifulSoup(source, 'lxml')

i = 0
for comment_item in soup.findAll('div', class_='comment-item'):
    print(f'Отзыв №{i}')


    #забираем и выводим ссылку на фото
    photo = comment_item.find('a')
    try:
        print('https://groupprice.ru/', photo.get('href'), sep='')
    except AttributeError:
        print('Нет фото')


    #забираем купленный размер
    size = comment_item.find('div', class_='bought_notice')
    try:
        for letter in size.text:
            if letter.isdigit():
                print(letter, end='')
        print(' - Размер\n')
    except:
        print('Нет размера')

    #Забираем дату покупки
    date_and_name = comment_item.find('div', class_='date')
    raw_date_and_name = date_and_name.text
    formated_date_and_name = ' '.join(raw_date_and_name.split())
    print(formated_date_and_name)

    #забираем текст отзыва

    raw_text = comment_item.find('div', class_='text')
    formated_text = ' '.join(raw_text.text.split())


    #забираем фотки бабушек
    photo_of_babushka = comment_item.find('a', class_='view')
    try:
        print(photo_of_babushka.get('href'))
    except AttributeError:
        print('')

    print(formated_text, end='\n\n' * 3)
    i += 1
input()