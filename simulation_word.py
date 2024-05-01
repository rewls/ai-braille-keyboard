from package import word_recommendation as wr
import re

phrases = ["안녕하세요",
           "오늘 날씨가 좋습니다",
           "점심 식사 맛있게 하세요",
           "지금 회의 중입니다",
           "죄송합니다 조금 늦을 것 같습니다",
           "이번 프로젝트 마감일은 다음 주입니다",
           "오늘 저녁에 영화 보러 갈까요",
           "생일 축하해",
           "커피 한 잔 할래요",
           "내일 아침 8시에 뵙겠습니다"]
n_test = 30

n_phrase = len(phrases)
word_lists = [] 
match_counts = []
reduced_phrases = []
for i in range(n_phrase):
    tmp = re.split('[ ,.?!]', phrases[i])
    word_lists.append([x for x in tmp if x != ''])
    match_counts.append([])
    for j in range(len(phrases[i].split(' '))):
        match_counts[i].append(0)

for i in range(n_test):
    reduced_word_lists = []
    reduced_phrases = []
    for j in range(n_phrase):
        reduced_word_lists.append(word_lists[j].copy())
        reduced_phrases.append(' '.join(word_lists[j]))
    for j in range(n_phrase):
        for k in range(len(word_lists[j])):
            phrase = ' '.join(word_lists[j][:k])
            phrase = phrase + ' ' + word_lists[j][k][0]
            recommended_word_list = wr.recommend_word(phrase)
            print(phrase, recommended_word_list)
            for word in recommended_word_list:
                if word in ' '.join(word_lists[j][k:]):
                    match_counts[j][k] += 1
                    reduced_phrases[j] = reduced_phrases[j].replace(word[1:], "")
                    break
        print(reduced_phrases[j])
    print()

for i in range(n_phrase):
    for j in range(len(word_lists[i])):
        print(f"{i}번째 문장, {j}번째 단어 {word_lists[i][j]}: {match_counts[i][j] / n_test}")
