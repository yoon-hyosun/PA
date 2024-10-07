from bs4 import BeautifulSoup
filename= "Data/fruits.html"
with open(filename,'r', encoding='utf-8') as ex:
    soup = BeautifulSoup(ex, 'html.parser')

print(soup.find('p','name2'))
print()
print(soup.find('p',id='fruits2'))
print()


print('='*10)
#
#
#
result = soup.find_all( 'span','store')
print(result)

f = open('Data/store.txt', 'w', encoding='utf-8')

for i in result :
    txt= i.get_text()
    f.write(txt+'\n')
f.close()

print('='*10)

print(soup.select('p'))
print('='*10)
print(soup.select('p.name2'))
print(soup.select('.name2'))
print(soup.select('#fruits2'))
print(soup.select('p.name2 > span'))
print(soup.select('p.name2 > span.store'))
print(soup.select('.name2 > span.store'))
print(soup.select('#fruits2 > span.store'))

print(soup.select('a[href]'))
print(soup.select('a')[0])




