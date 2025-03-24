import streamlit as st
import pandas as pd
import requests
import openpyxl as xl
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


st.title("Book Data Scraping and Visualization with Streamlit")
st.header("Books to scrape")
url =st.text_input("Enter url:","https://")
st.write("you entered: ",url)
response = requests.get(url)
st.write("status code: ",response.status_code)
# print(response.status_code)
soup = BeautifulSoup(response.text,'html.parser')
books = soup.find_all("article",class_="product_pod")
data=[]
for book in books:
    title=book.h3.a["title"]
    price=book.find("p",class_="price_color").text
    data.append([title,price])
st.subheader("Extracted data:")
st.write(data)   

df= pd.DataFrame(data,columns=["Title","Price"])
df.to_csv("sheet.csv",index=False,encoding="utf-8")
st.write(df)

st.subheader("Data Plotting")
columns = df.columns.tolist()

x_axis = st.selectbox("select x_axis coloumn ",columns)
y_axis = st.selectbox("select y_axis coloumn ",columns)

st.line_chart(df.set_index(x_axis)[y_axis])
st.snow()
st.balloons()
