from scraper import init_scrap
import json
import pyfiglet
from rich.console import Console
from rich.prompt import Prompt


def display_welcome_message(console):
    """
    Display a welcome message for the PadelZoom Scraper.

    This function generates an ASCII art banner and prints it
    along with a brief description of the program's functionality
    and prompts the user to enter the number of pages to scrape.

    Args:
        console (Console): An instance of the Console class
                           from the rich library used for formatted
                           console output.
    """
    ascii_banner = pyfiglet.figlet_format("PadelZoom Scraper")
    console.print(ascii_banner, style="bold cyan")
    console.print('This program will scrape all the paddles from the PadelZoom website',  # noqa: E501
                  style="bold magenta")
    console.print('Please, introduce the total amount of pages to scrape:',
                  style="bold blue")


def get_max_pages():
    """
    Prompt the user for the maximum number of pages to scrape.

    This function uses a prompt to ask the user for input and
    returns the provided number as an integer.

    Returns:
        int: The maximum number of pages to scrape, as entered by the user.
    """
    max_pages = Prompt.ask("Number of pages", default="1", show_default=True)
    return int(max_pages)


def save_paddles_to_json(paddles):
    """
    Save the scraped paddle data to a JSON file.

    This function takes a list of paddle objects, converts them
    into a dictionary format, and writes them to a file named
    'paddles.json' in JSON format.

    Args:
        paddles (list): A list of paddle objects containing the scraped data.
    """
    paddles_dict = [paddle.__dict__ for paddle in paddles]
    with open('paddles.json', 'w') as file:
        json.dump(paddles_dict, file, ensure_ascii=False, indent=4)


def main():
    """
    The main entry point of the PadelZoom Scraper program.

    This function initializes the console, displays the welcome
    message, prompts the user for the number of pages to scrape,
    invokes the scraping function, and saves the results to a JSON file.
    """
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
