import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://quotes.toscrape.com/")
url = driver.current_url
if "https" in url:
    print("website is secure")
else:
    print("website is not secure")

quotes = driver.find_elements(By.CLASS_NAME,"text")
authors = driver.find_elements(By.CLASS_NAME,"author")
tags = driver.find_elements(By.CLASS_NAME,"tag")

quote_list = []
author_list = []
tags_list = []

for i in range(len(quotes)):
    quote_list.append(quotes[i].text)
    author_list.append(authors[i].text)
    tags_list.append(tags[i].text)

df = pd.DataFrame({"Quote": quote_list, "Author": author_list, "Tags": tags_list})

df.to_csv("quotes.csv",index=False,encoding="utf-8")  

df=pd.read_csv("quotes.csv",encoding="utf-8")
# print(df.head())

title = driver.title
print("page title: ",title)
    

driver.quit()