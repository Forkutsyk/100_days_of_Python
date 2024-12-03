import requests
from bs4 import BeautifulSoup

BILBOARD_URL = "https://www.billboard.com/charts/hot-100/"


def ask_user():
    # TODO: make a simple GUI for this , using for example Tkinter
    return input("Which year do you want to travel to ? Type the date in the format YYYY-MM-DD\n")


def data_collector(year):
    header = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    response = requests.get(url=f'{BILBOARD_URL}{year}/', headers=header)
    response.raise_for_status()
    return response.text


def parser(data):
    soup = BeautifulSoup(data, 'html.parser')
    title_tags = soup.select('li > h3[class^="c-title"]')
    songwriter_tags = soup.select('li > span[class^="c-label"]')

    title_names = [title.getText().split("\t")[9] for title in title_tags]
    step_one = [title.getText().split("\t")[2].split("\n")[0] for title in songwriter_tags]
    step_two = [item for item in step_one if (item == '112' or not item.isdigit() and item != 'NEW' and item != '-') or ' ' in item]
    return title_names, step_two


if __name__ == '__main__':
    user_response = ask_user()
    clean_html = data_collector(user_response)
    titles, bands = parser(clean_html)

