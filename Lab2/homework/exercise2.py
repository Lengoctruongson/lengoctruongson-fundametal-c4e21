from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
conn = urlopen(url)

raw_data = conn.read()

html_page = raw_data.decode('utf-8')

soup = BeautifulSoup(html_page, 'html.parser')

column = []
td = soup.find_all('td', 'h_t')
for i in td:
    a = i.string
    column.append(a)
print(column)

row = []
table = soup.find('table', id='tableContent')
row = table.find_all('tr')
for i in row:
    a = i.string
    row.append(a)
print(row)
# row = soup.find_all()

