# Step 1. 필요한 모듈과 라이브러리를 로딩하고 검색어를 입력
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("c:/Temp/chromedriver.exe")
driver = webdriver.Chrome(service=s)

# 검색어 입력과 네이버로 이동
f_name = "Data/네이버_여름여행.txt"

query_txt = "여름여행"
driver.get("https://www.naver.com")
driver.maximize_window()

element = driver.find_element("id","query")
element.send_keys(query_txt)
element.send_keys("\n")


"""
# Step 2. 뉴스 section으로  이동, 화면 출력

driver.find_element("link text","다음").click()
driver.find_element("link text","뉴스").click()

full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')
news_list = soup.find('ul', 'list_news _infinite_list').find_all('li')


for i in news_list:
    try:
        title = i.find('a', 'news_tit').get_text()
        print(title)
        print('\n')
    except:
        pass

    try:
        # contents = i.find('div', 'news_dsc').get_text()
        contents = i.find('a', 'api_txt_lines dsc_txt_wrap').get_text()
        print(contents)
        print('\n')
    except:
        pass



# Step 3: 텍스트를 추출하여 txt 형식으로 저장하기
f_name = "Data/네이버_여름여행_뉴스.txt"
f = open(f_name, 'w', encoding='UTF-8')

for i in news_list:
    try:
        title = i.find('a', 'news_tit').get_text()
        f.write(title +'\n')
    except:
        pass

    try:
        contents = i.find('a', 'api_txt_lines dsc_txt_wrap').get_text()
        f.write(contents+'\n')
    except:
        pass

f.close()
"""