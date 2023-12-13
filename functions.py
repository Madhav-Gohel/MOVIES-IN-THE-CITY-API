import requests
import json
from bs4 import BeautifulSoup

# Function to fetch the HTML content of a web page
def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

# Function to parse HTML content using BeautifulSoup
def parse_html(html):
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    else:
        return None



#Function to get detials of movies in that city
def getMovies(city):
    movielist = []
    url = "https://paytm.com/movies/"
    page = get_html(url+city)
    soup = parse_html(page)
    links = soup.find_all('ul',class_ = "H5RunningMovies_gridWrapper__KuuvC")
    movies = soup.find_all("li",class_="H5RunningMovieV2_runningMovie__5uA8A")

    for movie in movies:
        try:
            link = url + movie.find("a",href=True)['href'][8:]
        except:
            link = "N/A"
        try:
            img = movie.find("a").find("div",class_="H5RunningMovieV2_imgWrapper__Tadcr").find("img",class_= "bgImg")["src"].split('?')[0]
            
            print()
        except:
            img = "N/A"
        try:
            title = movie.find("div",class_="H5RunningMovieV2_movieDetails__uNOSv").find("div",class_= "H5RunningMovieV2_movieName__XlSnn").text
        except:
            title = "N/A"
        movielist.append(dict({"title":f"{title}","imgsrc":f"{img}","link": f"{link}"}))
    
    json_movies = json.loads(str(movielist).replace("'",'"'))
    return json_movies