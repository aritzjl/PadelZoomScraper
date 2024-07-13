from scraper import init_scrap
import json
import pyfiglet
from rich.console import Console
from rich.prompt import Prompt


def display_welcome_message(console):
    ascii_banner = pyfiglet.figlet_format("PadelZoom Scraper")
    console.print(ascii_banner, style="bold cyan")
    console.print('This program will scrape all the paddles from the PadelZoom website',  # noqa: E501
                  style="bold magenta")
    console.print('Please, introduce the total amount of pages to scrape:',
                  style="bold blue")


def get_max_pages():
    max_pages = Prompt.ask("Number of pages", default="1", show_default=True)
    return int(max_pages)


def save_paddles_to_json(paddles):
    paddles_dict = [paddle.__dict__ for paddle in paddles]
    with open('paddles.json', 'w') as file:
        json.dump(paddles_dict, file, ensure_ascii=False, indent=4)


def main():
    console = Console()
    display_welcome_message(console)

    max_pages = get_max_pages()
    console.print('Please wait, this process may take a while...',
                  style="bold yellow")

    paddles = init_scrap('https://padelzoom.es/palas/?fwp_paged=', max_pages)

    save_paddles_to_json(paddles)
    console.print('Paddles scraped successfully!', style="bold green")


if __name__ == '__main__':
    main()
