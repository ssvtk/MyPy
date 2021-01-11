import requests
import json
from flickrparse.flickr_soup import StatusCodeError

KEY = 'e237a7f575d1c9cc5c8c3bd105f4ba98'
#
# Secret:
# 0f7119aed20f2595
tag = 'cat'


def get_photos_id(tag):
    """Returns a list of IDs for required tag
    """

    req = f'https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key={KEY}&tags={tag}&format=json&nojsoncallback=1'
    resp = requests.get(req)
    if resp.status_code == 200:
        data = json.loads(resp.text)
        idlist = [elem['id'] for elem in data['photos']['photo']]
    else:
        raise StatusCodeError('Not 200 status')
    return idlist


def get_urls():
    """Возвращает список списков url для каждого из id несколько размеров
                        Square
                        Large Square
                        Thumbnail
                        Small
                        Small 320
                        Small 400
                        Medium
                        Medium 640
                        Medium 800
                        Large
                        Large 1600
                        Large 2048
                        X-Large 3K
                        Original
                            """
    urllist = []
    for id in get_photos_id('cat'):
        req = f'https://www.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key={KEY}&photo_id={id}&format=json&nojsoncallback=1'
        resp = requests.get(req)
        if resp.status_code == 200:
            data = json.loads(resp.text)
            one_urllist = [elem['source'] for elem in data['sizes']['size']]
            urllist.append(one_urllist)
        else:
            raise StatusCodeError('Not 200 status')
    return urllist


i = 1

for elem in get_urls():
    url = elem[1]
    req = requests.get(url)
    f = open(f'file_cat_{i}.jpg', 'wb')
    f.write(req.content)
    f.close()
    i += 1
