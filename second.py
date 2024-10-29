from bs4 import BeautifulSoup
filename= "Data/fruits.html"
with open(filename,'r', encoding='utf-8') as ex:
    soup = BeautifulSoup(ex, 'html.parser')

print(soup.find('p','name2'))
print()

print(soup.find('p',id='fruits2'))
print()

print('='*10)

result = soup.find_all( 'span','store')
print(result)

f = open('Data/store.txt', 'w', encoding='utf-8')

for i in result :
    txt= i.get_text()
    f.write(txt+'\n')
f.close()







