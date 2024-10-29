#Step 1. 필요한 모듈을 실행합니다.
from konlpy.tag import *
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter


#Step 2한글 형태소 분석기
# Okt(Open Korean Text)와 Kkma(Korean morpheme analyzer)
okt = Okt()
kkma = Kkma( )

print("Kkma:",kkma.nouns("나는 사과, 사과 , 복숭아, 복숭아가 좋아요"))
print("okt:",okt.nouns("나는 사과, 사과 , 복숭아, 복숭아가 좋아요"))


#Step 3. 텍스트 파일을 불러와서 형태소 분석
#Step 3. 키워드를 추출하고 빈도조사
data1 = open("Data/파이썬_텍스트분석예제.txt", encoding="utf-8").read( )
print(data1)

data2 = okt.nouns(data1)
print("1.추출된 키워드:", data2)
data3 = Counter(data2)
print("2.단어별 빈도수:",data3)


#Step 4. 불용어 제거하기
sword = open("Data/불용어목록.txt",encoding="utf-8").read()
print(sword)

data4 = [ each_word for each_word in data2
          if each_word not in sword ]

print("1차 불용어 제거 결과")
print(data4)

#글자수로 불용어 제거하기
data5 = []
for i in data4 :
    if len(i) >= 2 :
       data5.append(i)

print("2차 불용어 제거")
print(data5)

# Step 5. 단어별 빈도수 집계하기
data6 = Counter(data5)
print(data6)

data7 = data6.most_common(10)
print(data7)

for i, j in data7:
    print ( i, j)
print("---------------")

#워드 클라우드를 그리기 위하여 데이터를 정리
data8 = dict(data7)
print(data8)


#Step 6. 워드 클라우드 그리기  #H2GTRM.TTF  HMKMG.TTF

wordcloud = WordCloud(font_path="c:\\windows\\fonts\\H2GTRM.TTF" ,
                       relative_scaling=0.5,
                       background_color="white"
                     ).generate_from_frequencies(data8)


plt.figure(figsize=(8,4))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()



#네트워크형_ 워드클라우드
import matplotlib.pyplot as plt
import networkx as nx

# 한글 폰트 설정 (필요한 경우)
plt.rcParams['font.family'] = 'Batang'

# 데이터
print(data8)

#네트워크 중심노드
center_word = "좋아하는과일"  # 중심 노드(단어)
words = list(data8.keys())
frequencies = list(data8.values())

# 그래프 초기화
G = nx.Graph()

# 중심 노드 추가
G.add_node(center_word, size=3000)  # 중심 노드의 크기 설정

# 주변 노드 추가 및 연결
for word, freq in zip(words, frequencies):
    G.add_node(word, size=freq * 300)  # 주변 노드 크기 설정
    G.add_edge(center_word, word)  # 중심 노드와 연결

# 스타 네트워크 레이아웃 설정
pos = nx.spring_layout(G, center=(0, 0), k=5, iterations=100)

# 노드 그리기
sizes = [nx.get_node_attributes(G, 'size')[node] for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=sizes, node_color='skyblue', alpha=1)

# 라벨 그리기
# nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")
nx.draw_networkx_labels(G, pos, font_size=13, font_family="Batang")
# 간선 그리기
nx.draw_networkx_edges(G, pos, width=2, alpha=0.8, edge_color='darkgray')

# 그래프 출력
plt.show()