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

# 네이버 검색창을 찾아 검색어 입력
element = driver.find_element("id", "query")
element.send_keys(query_txt)
element.send_keys("\n")

# Step 2. 블로그 section으로 이동
driver.find_element("link text", "블로그").click()

full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')


# 블로그 내용이 저장된 태그 찾기
content_list = soup.find('ul', 'lst_view _fe_view_infinite_scroll_append_target').find_all('li')

# Step 3. 제목과 내용 추출
for i in content_list:
    try:
        title = i.find('a', 'title_link').get_text()
        print(title)
        print()
    except:
        pass

    try:
        contents_1 = i.find('a', 'dsc_link').get_text()
        print(contents_1)
        print()
    except:
        pass

# Step 4. 제목과 내용 추출을 txt형식 파일에 저장

f_name = "Data/네이버_여름여행.txt"
f = open(f_name, 'w', encoding='UTF-8')

for i in content_list:
    try:
        title = i.find('a', 'title_link').get_text()
        f.write(title + "\n")
    except:
        pass

    try:
        contents_1 = i.find('a', 'dsc_link').get_text()
        f.write(contents_1 + "\n")
        f.write("\n")
    except:
        pass

f.close()

#================================================
# Step 5.검색어 입력과 네이버로 이동
driver.get("https://www.naver.com")
driver.maximize_window()

element = driver.find_element("id","query")
element.send_keys(query_txt)
element.send_keys("\n")

print('='*20)
# Step 6. 뉴스 section으로  이동, 화면 출력

driver.find_element("link text","다음").click()
driver.find_element("link text","뉴스").click()

full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')

# 뉴스 세션에서  제목과 내용이 저장된 태그 찾기
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



# Step 7: 텍스트를 추출하여 txt 형식으로 저장하기
f_name = "Data/네이버_여름여행.txt"
f = open(f_name, 'a', encoding='UTF-8')

for i in news_list:
    try:
        title = i.find('a', 'news_tit').get_text()
        f.write(title +'\n')
    except:
        pass

    try:
        contents = i.find('a', 'api_txt_lines dsc_txt_wrap').get_text()
        f.write(contents+'\n')
        f.write("\n")
    except:
        pass

f.close()