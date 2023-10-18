import requests
from bs4 import BeautifulSoup
import pandas as pd
df = pd.DataFrame(columns = ['page_no','index','product_url', 'product_name', 'product_price', 'rating', 'number_of_reviews'])
for j in range(1,20):
    print(j)
for k in range(100):
    URL = "https://www.amazon.in/s?k=bags&page={j}&crid=2M096C61O4MLT&qid=1697476556&sprefix=ba%2Caps%2C283&ref=sr_pg_2"
    response = requests.get(URL)
    soup=BeautifulSoup(response.content,"html")
for i in range(0,23):
        try:
            page_no = j
            index = i
            product_url = 'https://www.amazon.in/' + soup.find("div", attrs={"data-index":f'{i}'}).find("a", attrs = {"class":"a-link-normal s-no-outline"}).get('href')
            product_name = soup.find("div", attrs={"data-index":f'{i}'}).find("span", attrs = {"class":"a-size-medium a-color-base a-text-normal"}).text
            product_price = soup.find("div", attrs={"data-index":f'{i}'}).find("span", attrs = {"class":"a-price-whole"}).text
            rating = soup.find("div", attrs={"data-index":f'{i}'}).find("span", attrs = {"class":"a-icon-alt"}).text
            number_of_reviews = soup.find("div", attrs={"data-index":f'{i}'}).find("span", attrs = {"class":"a-size-base s-underline-text"}).text
            df.loc[len(df.index)] = [page_no,index,product_url, product_name, product_price, rating, number_of_reviews]
        except:
            a = 'failed'
            if df[['product_url']].drop_duplicates().shape[0] >= 200:
                break

print(df)
product_urls = 'https://www.amazon.in/' + soup.find("div", attrs={"data-index":f'{i}'}).find("a", attrs = {"class":"a-link-normal s-no-outline"}).get('href')

for url in product_urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting product information
    product_description = soup.find('div', {'id': 'productDescription'}).text.strip()
    asin = soup.find('th', text='ASIN').find_next('td').text.strip()
    manufacturer = Soup.find('th', text='Manufacturer').find_next('td').text.strip()

    # Add the extracted data to the product_data list
    product_data.append({
        'URL': url,
        'Description': product_description,
        'ASIN': asin,
        'Manufacturer': manufacturer
    })
