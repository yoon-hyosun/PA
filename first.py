first='''
<html>
    <head>
      <title> HTML연습 </title>
    </head>
    <body>
        <p  align="center"> 홍길동 </p>
        <p  align="left"> 이순신 </p>
        <p  align="right"> 유관순 </p>
    </body>
</html>
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(first, 'html.parser')

print(soup.find('p'))
print(soup.find('p', align='right'))
print(soup.find_all('p'))
print()

result = soup.find_all('p')

for i in result:
    print(i.get_text())