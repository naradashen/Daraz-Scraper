# Daraz-Scraper

This project is a web scraper for daraz.lk deals using Selenium. The script navigates through the deals categories on the Daraz website, extracts product information, and prints it.

## Prerequisites

- Python 3.x
- Google Chrome
- ChromeDriver (ensure the ChromeDriver version matches your Chrome version)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/naradashen/Daraz-Scraper.git
    cd Daraz_Scaper
    ```

2. Create a virtual environment and activate it (optional but recommended):
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip3 install -r requirements.txt
    ```

4. Download ChromeDriver and place it in `/usr/local/bin` or update the path in `daraz.py`.

## Usage

Run the scraper:
```sh
python3 daraz.py
