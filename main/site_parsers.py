import requests
import bs4
from bs4 import BeautifulSoup


class GameNotFoundError(Exception):
    pass


def get_soup(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise requests.HTTPError('Status code is not 200')
    return BeautifulSoup(response.content, 'html.parser')


def zaka_zaka_parser(game_title):
    """Returns the (name, price) tuple of the relevant game from zaka-zaka site"""
    url = f'https://zaka-zaka.com/search/?ask={game_title.lower().replace(" ", "+")}'
    soup = get_soup(url)

    # Let's assume that the first one will be the most relevant
    first_result = soup.select_one('.game-block')
    if not first_result:
        raise GameNotFoundError('Relevant game not found')

    tags = [element for element in first_result.contents if isinstance(element, bs4.element.Tag)]
    name = None
    price = None

    for tag in tags:
        match tag['class'][0]:
            case 'game-block-name':
                name = tag.contents[0]
            case 'game-block-prices':
                price = tag.contents[3].contents[0].strip()

    return name, price


def steambuy_parser(game_title):
    pass


def steampay_parser(game_title):
    pass
