import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
web_archive = response.text
soup = BeautifulSoup(web_archive, 'html.parser')
all_films = soup.find_all(name="h3", class_="title")

film_list = [film.getText() for film in all_films]
# print(film_list)


with open("movies.txt", 'w', encoding='UTF-8') as txt_file:
    for line in film_list[::-1]:
        try:
            txt_file.write(''.join(str(line)) + '\n')
        except UnicodeEncodeError:
            txt_file.write("PROBLEM \n")

    print("File done!")
