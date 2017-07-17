from bs4 import BeautifulSoup
import requests
import wget

def make_soup(url):
    return BeautifulSoup(requests.get(url).content, 'lxml')

def get_images(url):
    soup = make_soup(url)

    images = [img for img in soup.findAll('img')]
    
    image_links = [image.get('src') for image in images]
    for link in image_links:
        print(link)
        filename=link.split('/')[-1]
        image_from_url = wget.download(link)

if __name__ == '__main__':
    get_images('http://www.wookmark.com')
