from bs4 import BeautifulSoup
import requests

URL = "https://www.kupi.cz/"
to_find = "Batoh Essential 17 l vínový"
def main():
    response = requests.get(URL)
    #print(response.text)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        searched_link = soup.find_all('a', title="Decathlon leták")[0]['href']
        searched_link = URL + searched_link[1::]
        print(searched_link)
    response = requests.get(searched_link)





if __name__ == '__main__':
    main()
