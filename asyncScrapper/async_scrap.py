import aiohttp
from random import sample, uniform, randint
import aiofiles
import requests
from bs4 import BeautifulSoup as bs4
from ruia import Item, TextField, AttrField, Spider
import os


class StatusCodeError(Exception):
    """
    Raised when status code is NOT 200
    """

    def __init__(self, message):
        self.message = message


URL = 'https://xkcd.ru/num/'

response = requests.get(URL)

if response.status_code == 200:
    soup = bs4(response.text, 'html.parser')
else:
    raise StatusCodeError('Status Code is not "200". Unable to connect!')


def get_n_link_list(link_amt) -> list:
    """
    sync
    Возвращает список из n случайных элементов-ссылок на страницы с комиксами.
    """
    real_link_list = soup.find_all('li', class_='real')
    return ['https://xkcd.ru' + link.a['href'] for link in sample(real_link_list, k=link_amt)]


class GetPage(Item):
    target_item = TextField(css_select='.main')
    url = AttrField(css_select='img', attr='src')

    async def clean_title(self, value):
        return value.strip()


class ComicSpider(Spider):
    start_urls = [url for url in get_n_link_list(40)]

    # concurrency = 10

    async def parse(self, response):
        async with aiohttp.ClientSession() as session:
            async for item in GetPage.get_items(html=response.html):
                # await asyncio.sleep(uniform(0.2, 0.5)) Документация уверяет что в библиотеке предусмотрены ожидания, хотя я не уверен.

                async with session.get(f'{item.url}') as resp:
                    filename = item.url.split('/')[-1]
                    async with aiofiles.open(f'{path}/{filename}', 'wb') as f:
                        await f.write(await resp.content.read())

            yield item


if __name__ == '__main__':
    path = 'pictures'
    if not os.path.exists(path):
        os.mkdir('pictures')
    else:
        path = f'{path}{randint(1, 50)}'
        os.mkdir(path)

    ComicSpider.start()
