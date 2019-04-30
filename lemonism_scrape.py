import requests
from bs4 import BeautifulSoup as bs
import os

url = 'https://hellogiggles.com/reviews-coverage/everyday-liz-lemonisms/'
# url = 'https://giphy.com/explore/liz-lemon'

# page = requests.get(newurl)
page = requests.get(url)

soup = bs(page.text, 'html.parser')

image_tags = soup.findAll('img')

if not os.path.exists('lemonisms'):
    os.makedirs('lemonisms')

os.chdir('lemonisms')

x = 0

for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('lemonism-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1

    except:
        pass
