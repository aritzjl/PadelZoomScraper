from paddle import Paddle
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup


def init_scrap(url: str, maxPages: int) -> list[Paddle]:
    paddles = []
    for page in tqdm(range(1, maxPages + 1),
                     desc="Scraping pages",
                     unit="page"):
        paddles.extend(scrap_page(f'{url}{page}'))
    return paddles


def scrap_page(url: str) -> list[Paddle]:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paddles = []

    for paddle in soup.find_all('div', class_='col-md-pala'):
        paddle_url = paddle.find('a')['href']
        paddles.append(scrap_paddle(paddle_url))

    return paddles


def scrap_paddle(url: str) -> Paddle:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    paddle = Paddle(url)

    # Details
    add_paddle_details(paddle, soup)

    # Statistics
    add_paddle_statistics(paddle, soup)

    # Stores
    add_paddle_stores(paddle, soup)

    return paddle


def add_paddle_details(paddle: Paddle, soup: BeautifulSoup) -> None:
    paddle.image_url = (soup.find('div', class_='img-single-pala')
                            .find('img')['src'])
    paddle.name = soup.find('div', class_='title-pala').find('h1').text

    data = soup.find("div", class_="col-md-4 col-sm-6")
    paddle.brand = data.find_all('a')[1].text
    paddleDescription = (
        soup.find('div', class_='description-pala')
        .find_all('p'))
    paddle.season = int(paddleDescription[0].text.split(': ')[1])
    paddle.frameMaterial = paddleDescription[1].text.split(': ')[1]
    paddle.surfaceMaterial = paddleDescription[2].text.split(': ')[1]
    paddle.rubberMaterial = paddleDescription[3].text.split(': ')[1]
    paddle.touch = paddleDescription[4].text.split(': ')[1]
    paddle.shape = paddleDescription[5].text.split(': ')[1]
    paddle.weight = paddleDescription[6].text.split(': ')[1]


def add_paddle_statistics(paddle: Paddle, soup: BeautifulSoup) -> None:
    statistics = (soup.find('div', id='row-progress-bar')
                  .find_all('div', class_='col-md-1 col-sm-2'))
    paddle.total = float(statistics[0]
                         .find('div', class_='value-puntuacion').text)
    paddle.power = float(statistics[1]
                         .find('div', class_='value-puntuacion').text)
    paddle.control = float(statistics[2]
                           .find('div', class_='value-puntuacion').text)
    paddle.output = float(statistics[3]
                          .find('div', class_='value-puntuacion').text)
    paddle.maneuverability = float(statistics[4]
                                   .find('div', class_='value-puntuacion')
                                   .text)
    paddle.sweetSpot = float(statistics[5]
                             .find('div', class_='value-puntuacion').text)


def add_paddle_stores(paddle: Paddle, soup: BeautifulSoup) -> None:
    paddle.originalPrice = float(soup.find(id='pvp-price-single').text)
    try:
        paddle.bestPrice = float(soup.find(property='offers').text)
    except (AttributeError, ValueError):
        paddle.bestPrice = None


def get_max_pages(url: str) -> int:
    respone = requests.get(url)
    soup = BeautifulSoup(respone.content, 'html.parser')
    pages = soup.find('a', class_='last')
    return int(pages.content) if pages else 1
