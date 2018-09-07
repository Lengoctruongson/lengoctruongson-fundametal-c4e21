# part 1
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'https://www.apple.com/itunes/charts/songs'
conn = urlopen(url)

raw_data = conn.read()

html_page = raw_data.decode('utf-8')

soup = BeautifulSoup(html_page, 'html.parser')

div_list = soup.find_all('div', 'section-content')

li_list = div_list[1].ul.find_all('li')

songs_list = []

for li in li_list:
    a = li.h3.a
    b = li.h4.a
    song = a.string
    artist = b.string
    news = {
        'Song': song,
        'Artist': artist,
    }
    songs_list.append(news)

pyexcel.save_as(records = songs_list, dest_file_name = "iTunes.xlsx")

# part 2
from youtube_dl import YoutubeDL
dl = YoutubeDL()

options = {
    'default_search': 'ytsearch',
    'max_download': 1,
}

dl = YoutubeDL(options)
for i in songs_list:
    n = i['Song'] + ' ' + i['Artist']
    dl.download(n)