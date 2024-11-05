# 인공지능1  파일 키워드 분석
#Step 1. 필요한 모듈을 실행합니다.
from konlpy.tag import *
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter





#Step 2 . 키워드 추출

#형태소 분석기
okt = Okt()

#텍스트 파일 읽기
data1 = open("Data/인공지능.txt",encoding="utf-8").read( )

#키워드 추출
data2 = okt.nouns(data1)
print("1.추출된 키워드:", data2)


# Step 3. 용어 정리 작업 1
data3=[]
for a in data2 :
    if a == "제목":
        data3.append(a.replace("제목"," "))
    elif a=="내용":
        data3.append(a.replace("내용"," "))
    else :
        data3.append(a)
print(data3)


#Step 4. 추출된 단어들의 빈도를 조사

data4 = Counter(data3)
data5 = data4.most_common(120)
print("상위 120개 단어 ")
print("2.단어별 빈도수:",data5)

for i, j in data5:
    print(i, j)
print()





#Step 5. 파일을 이용하여 불용어 제거하기
sword = open("Data/인공지능gsub.txt",encoding="utf-8").read()
data6 = [ each_word for each_word in data3
          if each_word not in sword ]

#글자수로 불용어 제거하기
data7 = []
for i in data6 :
    if len(i) >=2 :
        data7.append(i)

print("\n")




# Step 6. 단어별 빈도수 집계하기
data8 = Counter(data7)
data9 = data8.most_common(50)
print(data9)

for i, j in data9:
    print(i,j)

print("\n")



# Step 7. 용어정리 2

print( " 용어정리 2" )
data10=[]
for a in data7 :
    if a == "인공":
        data10.append(a.replace("인공","인공지능"))
    elif a=="지능":
        data10.append(a.replace("지능", ""))
    elif a=="머신":
        data10.append(a.replace("머신","머신러닝 "))
    elif a == "러닝":
        data10.append(a.replace("러닝", ""))
    else :
        data10.append(a)

print(data10)


# Step 8. 불용어 목록 작성 2 및 불용어 제거

print( " 불용어 목록 작성 2  " )

sword = open("Data/인공지능gsub2.txt",encoding="utf-8").read()
data11 = [ each_word for each_word in data10
          if each_word not in sword ]

# Step 9. 최종 단어 확인

data12 = Counter(data11)
data13 = data12.most_common(30)
print(data13)

for i, j in data13:
    print(i,j)
print("\n")

word = dict(data13)



#Step 10. 워드 클라우드 그리기 1

wordcloud = WordCloud(font_path="c:\\windows\\fonts\\H2GTRM.TTF" ,
                       relative_scaling=0.3,
                       background_color="white"
                     ).generate_from_frequencies(word)
plt.figure(figsize=(10,8))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()




# 워드 클라우드 그리기 2

import numpy as np
from PIL import Image      # pip install Image

korea = np.array(Image.open("Data\korea.png"))
save_image= ("Data\korea_AI.png")

wc = WordCloud(font_path="c:\\windows\\fonts\\H2GTRM.TTF" ,
                       relative_scaling=0.3, mask = korea,
                       background_color="white",
                     ).generate_from_frequencies(word)


plt.figure(figsize=(10,10))
plt.imshow(wc)
plt.axis('off')
plt.savefig(save_image)
plt.show()


# 방사형 네트워크  워드클라우드

#워드 클라우드를 그리기 위하여 데이터를 정리
import matplotlib.pyplot as plt
import networkx as nx

# 한글 폰트 설정 (필요한 경우)
plt.rcParams['font.family'] = 'Batang'
plt.figure(figsize=(10,10))

# 데이터 정의
print(data13)
center_word = "인공지능"  # 중심 노드(단어)
words = list(word.keys())
frequencies = list(word.values())

# 그래프 초기화
G = nx.Graph()

# 중심 노드 추가
G.add_node(center_word, size=3000)  # 중심 노드의 크기 설정

# 주변 노드 추가 및 연결
for word, freq in zip(words, frequencies):
    G.add_node(word, size=freq * 200)  # 주변 노드 크기 설정
    G.add_edge(center_word, word)  # 중심 노드와 연결

# 네트워크 레이아웃 설정
pos = nx.spring_layout(G, center=(0, 0), k=6, iterations=100)

# 노드 그리기
sizes = [nx.get_node_attributes(G, 'size')[node] for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=sizes, node_color='darkgray', alpha=1)
# 라벨 그리기
nx.draw_networkx_labels(G, pos, font_size=14, font_family="Batang")
# 간선 그리기
nx.draw_networkx_edges(G, pos, width=3, alpha=0.8, edge_color='yellowgreen')

plt.savefig("인공지능방사형네트워크.png")
plt.show()
plt.close()
