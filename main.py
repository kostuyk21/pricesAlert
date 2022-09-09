from bs4 import BeautifulSoup
import requests



URL = "https://www.kupi.cz/slevy"
to_search = "ovoce-a-zelenina"
list_of_fruits_to_buy = ["pomeranče", "avokádo", ]
def main():
    response = requests.get(URL)
    #print(response.text)
    if response.ok:

        soup = BeautifulSoup(response.text, "html.parser")
        searched_categories = soup.find_all('a', class_="category_item")#['href']
        for category in searched_categories:
            if to_search in category['href']:
                searched_link = URL + category["href"][6::]
    print(searched_link)
    response = requests.get(searched_link+"?sh3=3&sh1=1")
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        #TODO find a way to find products by entering a div
        products = soup.find(id="product_append").contents
        print(dir(products))
        #product = products.find_all("div")
        #print(product)






if __name__ == '__main__':
    main()
