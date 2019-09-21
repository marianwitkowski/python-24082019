import requests
import bs4

def clear_text(text):
    return text.replace("\n","").replace("\r","").replace(" ","")

search_url = "https://www.otomoto.pl/osobowe/volkswagen/golf/od-2004/?search%5Bfilter_enum_damaged%5D=0&search%5Bfilter_enum_no_accident%5D=1&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D="

result = requests.get(search_url)
html_data = bs4.BeautifulSoup(result.text, features='lxml')
#print(html_data)
max_page = int(html_data.select('.page')[-1].text)
print("Liczba stron dla wynikow=",max_page)

for index in range(1, max_page+1):
    url = f"{search_url}&page={index}"
    result = requests.get(url)
    html_data = bs4.BeautifulSoup(result.text, features='lxml')
    items =  html_data.select('article.offer-item')
    for item in items:
        print("ID:", item.attrs["data-ad-id"])
        print("Link:", item.attrs["data-href"])
        title = item.find('a', class_='offer-title__link').text.strip()
        print("Nazwa:",title)
        price = clear_text(item.find('span', class_='offer-price__number').text.strip())
        print("Cena:",price)

        params = item.find_all('li', class_='offer-item__params-item')
        for param in params:
            key = clear_text( param.attrs["data-code"] )
            value = clear_text(param.text)
            print(key,"=",value)

        print("-"*30)

