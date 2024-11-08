import streamlit as st
import requests

api_key = 'QvJALTXQrz4DLZwFCwLNRpEhAhSi1k67pz2GuvoU'
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
response = requests.get(url)

apod_content = response.json()

st.title(apod_content['title'])
st.image(apod_content['url'])
st.write(apod_content['explanation'])

# Image downloader
image_link = requests.get(apod_content['url'])
image = image_link.content
with open('img.jpg', 'wb') as file:
    file.write(image)