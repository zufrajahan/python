import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/index.html"
response = requests.get(url)
print("status code ",response.status_code)
# parse HTML content
soup = BeautifulSoup(response.text,'html.parser')
print(soup.prettify()[:500])

book_data=[]
# Extract Book Titles
# books = soup.find_all('h3')
books = soup.find_all("article",class_="product_pod")
for book in books:
    title=book.h3.a["title"]
# Extract Book Prices
    price=book.find("p",class_="price_color").text
    # print(f"title: {title} | price: {price}")
    book_data.append([title,price])

# convert list into pandas DataFrame
df = pd.DataFrame(book_data,columns=["title","price"])
df.to_csv("sheet.csv",index=False,encoding="utf-8")






