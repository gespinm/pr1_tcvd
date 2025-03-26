import click
import csv
import requests
from bs4 import BeautifulSoup
import os

_OUTPUT_FILEPATH = "/dataset/dataset.csv"


def _fetch_data(url):
    """Fetch data from the given URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

def _parse_data(html):
    """Parse the retrieved HTML and extract relevant data."""
    soup = BeautifulSoup(html, 'html.parser')
    data = []
    return data

def _save_to_csv(data, output_file):
    """Save extracted data to a CSV file."""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

@click.command()
@click.option('--url', required=False, default="https://www.google.es?", help='Target URL to scrape')
@click.option('--save-csv', required=False, default=True, help='Save locally the output in a CSV file')
def main(url, save_csv):
    html = _fetch_data(url)
    if html:
        data = _parse_data(html)
        _save_to_csv(data, _OUTPUT_FILEPATH)
        print(f"Data saved to {_OUTPUT_FILEPATH}")

if __name__ == "__main__":
    main()
