import requests
from bs4 import BeautifulSoup
from time import sleep
from random import uniform
import os


class StatusCodeError(Exception):
    """
    Raised when status code is NOT 200
    """
    def __init__(self, message):
        self.message = message


if __name__ == '__main__':

    welcome = 'Welcome to flickr image-downloading Bot'
    print(welcome, '\n', '=' * len(welcome), sep='')
    user_inp = input('What images do you need from flickr?: ')
    while not user_inp.strip():
        user_inp = input('Again, what images do you need from flickr?: ')
    QUERY = 'https://www.flickr.com/search/?text=' + user_inp.replace(" ", "+")
    resp = requests.get(QUERY)

    if resp.status_code == 200:
        doc = BeautifulSoup(resp.text, 'html.parser')
        div_photo = doc.find_all('div', class_='photo-list-photo-view')
        i = 1
        newpath = (r'{}'.format(user_inp)).replace(" ", "_")
        if not os.path.exists(newpath):
            os.makedirs(newpath)
            print(f'Folder - {newpath} created!', '\n')
        for element in div_photo:
            url = 'http://' + str(element)[(str(element).find('//')):str(element).find(')">')].lstrip('//')
            extension = url.split('.')[-1]
            with open(f'{newpath}\{user_inp.replace(" ", "_")}_image{i}.{extension}', 'wb') as f:
                #sleep(uniform(0.5, 1.5)) #Пока отдают и так.
                picresp = requests.get(url)
                picresp.raw.decode_content = True
                f.write(picresp.content)
                print(f"Copying img №{i} to {newpath} folder")
                i += 1

    else:
        raise StatusCodeError('Status Code is not "200"')
