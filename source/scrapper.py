import click
import csv
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

_OUTPUT_FOLDER= "dataset/"
_OUTPUT_FILEPATH= "dataset.csv"

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
    
    h1_tag = soup.find('h1')
    if not h1_tag:
        print("Header not found.")
        return pd.DataFrame()
    
    pre_tag = h1_tag.find_next('pre')
    if not pre_tag:
        print("Data section not found.")
        return pd.DataFrame()
    
    raw_data = pre_tag.text.strip().split('\n')
    data = []
    for line in raw_data:
        parts = line.strip().split()
        if len(parts) < 9:
            continue
        rank = parts[0]
        time = parts[1]
        wind = parts[2]
        athlete = ' '.join(parts[3:-5])
        nationality = parts[-5]
        birthdate = parts[-4]
        event = parts[-3]
        location = parts[-2]
        date = parts[-1]
        data.append([rank, time, wind, athlete, nationality, birthdate, event, location, date])
    df = pd.DataFrame(data, columns=['Rank', 'Time', 'Wind', 'Athlete', 'Nationality', 'Birthdate', 'Event', 'Location', 'Date'])
    
    return df

def _save_to_csv(data):
    """Save extracted data to a CSV file."""
    os.makedirs(os.path.dirname(_OUTPUT_FOLDER), exist_ok=True)
    data_rows = data.values.tolist()
    with open(_OUTPUT_FOLDER +_OUTPUT_FILEPATH, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data.columns)
        writer.writerows(data_rows)
    
@click.command()
@click.option('--url', required=False, default="https://www.alltime-athletics.com/m_100ok.htm", help='Target URL to scrape')
@click.option('--save-csv', required=False, is_flag=True, default=False, help='Save locally the output in a CSV file')
def main(url, save_csv):
    html = _fetch_data(url)
    if html:
        data = _parse_data(html)
        if not data.empty:
            _save_to_csv(data)
            print(f"Scrapping was completed sucecssfully, results saved in csv: {_OUTPUT_FILEPATH}")
        else:
            print("Scrapping was unsucecssfull, results were not saved")

if __name__ == "__main__":
    main()
