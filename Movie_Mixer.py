import random
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

def get_year(m_tag):
    msplit = m_tag.text.split ()
    year = msplit[-1]
    return year    

def main():
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    movietags = soup.select('td.titleColumn') 
    inner_movietags = soup.select('td.titleColumn a')
    Ratings_tag = soup.select('td.posterColumn span[name = ir]')

    years = [get_year(tag) for tag in movietags]
    actors_list = [tag['title']for tag in inner_movietags]
    title_list = [tag.text for tag in inner_movietags]
    rating_list = [float(tag['data-value']) for tag in Ratings_tag]

    n_movies = len(title_list)

    while True :
        idx = random.randrange(0, n_movies)
        print(f'{title_list[idx]}, {years[idx]}, Rating : {rating_list[idx]:.1f}, Starring : {actors_list[idx]}')
        user_ip = input('Do you want to continue (y/[n]) ? ')
        if user_ip != 'y':
            break

if __name__ == '__main__':
    main()