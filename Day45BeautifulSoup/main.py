import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")
titles = soup.find_all(name="h3", class_="title")

titles_text = [title.getText() for title in titles][::-1]
print(titles_text)

with open("movies.txt", "w") as movie_file:
    for title in titles_text:
        movie_file.write(f"{title}\n")

