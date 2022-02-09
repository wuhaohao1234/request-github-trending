import requests
from pyquery import PyQuery as pq
import datetime

time = datetime.datetime.now().strftime('%Y-%m-%d')

HEADERS = {
  'User-Agent'		: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
  'Accept'			: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Encoding'	: 'gzip,deflate,sdch',
  'Accept-Language'	: 'zh-CN,zh;q=0.8'
}

url = 'https://github.com/trending'

res = requests.get(url, headers=HEADERS)
#实例化
doc = pq(res.content)

items = doc('article.Box-row')

str = ''

for item in items:
  i = pq(item)
  link = i('h1 a').attr('href')
  title = i('h1 a').text()
  # print('\b')
  # print(title)
  desc = i('p').text()
  # print(desc)
  str += '# ' + time + ' github trending热榜' + '\n' + '## ' + title + '\n' + '[地址](' + link + ')' + '\n\n' + desc + '\n'

f = open('./' + time +'.md', 'w')

f.write(str)

f.close()