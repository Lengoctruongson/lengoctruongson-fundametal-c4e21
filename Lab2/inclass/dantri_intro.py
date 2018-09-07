from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'https://dantri.com.vn'
conn = urlopen(url)

raw_data = conn.read()

html_page = raw_data.decode('utf-8')

# print(html_page)

# f_conn = open('dantri.html', 'wb')

# f_conn.write(raw_data)

# f_conn.close()
# print('Done')

soup = BeautifulSoup(html_page, 'html.parser')
# print(soup.prettify())

ul = soup.find('ul', 'ul1 ulnew')
# print(soup.prettify())

li_list = ul.find_all('li')

news_list = []

for li in li_list:
    a = li.h4.a
    title = a.string
    link = url + a['href']
    news = {
        'Title': title,
        'Link': link,
    }
    news_list.append(news)
# print (news_list)
pyexcel.save_as(records = news_list, dest_file_name = "news_list.xlsx")
print('done')