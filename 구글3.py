# 구글에서 뉴스검색 내용을 파일에 저장

# Step 1. 필요한 모듈과 라이브러리를 로딩
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas  as pd
import time
from selenium.webdriver.chrome.service import Service

s = Service("c:/Temp/chromedriver.exe")
driver = webdriver.Chrome(service=s)


# Step 2. 구글 이동 및 검색어 입력
driver.get("https://www.google.co.kr")
driver.maximize_window()

query_txt = "가을여행"
f_name =  "Data/google_가을여행_2.txt"



# Step 3. 검색창의 이름을 찾아서 검색어를 입력하고 검색을 실행
element = driver.find_element("name","q")
element.send_keys(query_txt)
element.send_keys("\n")


# Step 4. "뉴스"로 이동하여 검색하여 텍스트 추출과 관련된 태그 추출

driver.find_element("link text","뉴스").click()
full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')
news_data = soup.find_all('div','SoaBEf')


# Step 5.추출한 데이터를 화면 출력과 동시에 파일에 저장

number = 1

f = open(f_name, 'w', encoding='UTF-8')

for i in news_data:
    print(number)
    f.write('번호:' + str(number) + "\n")

    try:
        title = i.find('div','n0jPhd ynAwRc MBeuO nDgy9d').get_text()
        print(title)
    except:
        pass
    f.write(title + "\n")

    try:
        content = i.find('div','GI74Re nDgy9d').get_text()
        print(content)
    except:
        pass
    f.write(content + "\n")

    number += 1
f.close()

#=====================================

for page in range(2,11):
    driver.find_element("link text",f'{page}').click()
    news_data = soup.find_all('div','SoaBEf')

    f = open(f_name, 'a', encoding='UTF-8')

    for i in news_data:
        print(number)
        f.write('번호:' + str(number) + "\n")

        try:
            title = i.find('div','n0jPhd ynAwRc MBeuO nDgy9d').get_text()
            print(title); f.write(title + "\n")
        except:
            pass

        try:
            content = i.find('div','GI74Re nDgy9d').get_text()
            print(content); f.write(content + "\n")
        except:
            pass

        number += 1
    f.close()

