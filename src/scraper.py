import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_imdb_top_movies():
    url = "https://www.imdb.com/chart/top"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    movies = []
    movie_divs = soup.find_all('div', class_='sc-15ac7568-0 jQHOho cli-children')

    for movie_div in movie_divs:
        # Name
        title_tag = movie_div.find('h3', class_="ipc-title__text ipc-title__text--reduced")
        if title_tag:
            full_name = title_tag.text.strip()
            name = full_name.split('.', 1)[-1].strip()
        else:
            name = "N/A"

        # Year, Length, Certificate
        meta_div = movie_div.find('div', class_="sc-15ac7568-6 fqJJPW cli-title-metadata")
        year, length = "N/A", "N/A"
        if meta_div:
            meta_spans = meta_div.find_all('span', class_="sc-15ac7568-7 cCsint cli-title-metadata-item")
            if len(meta_spans) > 0:
                year = meta_spans[0].text.strip()
            if len(meta_spans) > 1:
                length = meta_spans[1].text.strip()

        # Rating
        rating_span = movie_div.find('span', attrs={"aria-label": True, "data-testid": "ratingGroup--imdb-rating"})
        rating = "N/A"
        if rating_span:
            aria_label = rating_span.get("aria-label", "")
            if "IMDb rating:" in aria_label:
                rating = aria_label.replace("IMDb rating:", "").strip()

        movies.append((name, year, length, rating))

    df = pd.DataFrame(movies, columns=["Name", "Year", "Length", "Rating"])
    return df


def scrape_former_presidents():
    url = "https://en.wikipedia.org/wiki/List_of_presidents_of_India"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    presidents = []
    for row in soup.select('table.wikitable tbody tr'):
        cells = row.find_all('td')
        if len(cells) > 6:
            # Extract name and lifespan
            name_life = cells[1].get_text(strip=True)
            if '(' in name_life and ')' in name_life:
                name = name_life.split('(')[0].strip()
                lifespan = name_life.split('(')[1].replace(')', '').strip()
            else:
                name = name_life
                lifespan = ""
            home_state = cells[2].get_text(strip=True)
            time_in_office = cells[6].get_text(strip=True)
            presidents.append({
                'Name': name,
                'Lifespan': lifespan,
                'Home State': home_state,
                'Time in Office': time_in_office
            })

    return pd.DataFrame(presidents)
