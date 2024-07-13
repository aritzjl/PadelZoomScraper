# PadelZoom Scraper

The PadelZoom Scraper is a Python tool designed to scrape paddle information from the [PadelZoom](https://padelzoom.es/) website. It extracts detailed attributes, statistics, and pricing information for various paddles, saving the data in a structured JSON format.
![image](https://github.com/user-attachments/assets/b7158250-d120-4692-983d-d71de5bbad35)

## Features

- Scrapes paddle details, including name, brand, materials, and statistics.
- Saves scraped data into a `paddles.json` file.
- Supports user-defined limits for the number of pages to scrape.

## Requirements

To run this project, you need to install the required libraries. You can install them using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` includes all necessary libraries.

## Usage

1. Clone the repository:
    
    ```bash
    git clone https://github.com/yourusername/padelzoom-scraper.git
    cd padelzoom-scraper
    ```
    
2. Run the main script:
    
    ```bash
    python main.py
    ```
    
3. Follow the on-screen prompts to specify the number of pages to scrape.

## Code Structure

- `main.py`: The main script that initializes the console, prompts for user input, and invokes the scraping process.
- `scraper.py`: Contains the scraping logic, including functions to fetch paddle details from individual pages.
- `paddle.py`: Defines the `Paddle` class to structure the scraped data.

## Future Improvements

- Implement automatic detection of the total number of pages to scrape, eliminating the need for user input.
- Enhance store data retrieval, which is currently limited due to JavaScript loading.

## Contributing

Contributions are welcome! If you submit a pull request, please ensure that your code follows PEP 8 conventions using Flake8.

Feel free to open issues or submit pull requests.

---

For any questions or suggestions, feel free to open an issue on the repository.
