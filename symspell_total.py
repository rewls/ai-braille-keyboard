import pandas as pd
from symspellpy import SymSpell, Verbosity
from hangul_utils import split_syllables, join_jamos

def is_hangul_char(char):
    return '가' <= char <= '힣'

def safe_split_syllables(term):
    # 한글만 분해하고, 다른 문자는 그대로 둠
    return ''.join([split_syllables(char) if is_hangul_char(char) else char for char in term])

# CSV 파일 읽기
vocab = pd.read_csv("ko_50k.txt", sep=" ", names=["term", "count"])

# 자소 단위로 분해
vocab['term'] = vocab['term'].map(safe_split_syllables)

# 분해된 결과 저장
vocab.to_csv("ko_50k_decomposed.txt", sep=" ", header=None, index=None, encoding='utf-8')

# 결과 출력
print(vocab.head())

# SymSpell 초기화
sym_spell = SymSpell(max_dictionary_edit_distance=2)

# 사전 데이터 로드
dictionary_path = "ko_50k_decomposed.txt"

# 파일을 utf-8 인코딩으로 읽기
with open(dictionary_path, 'r', encoding='utf-8') as file:
    sym_spell.load_dictionary_stream(file, term_index=0, count_index=1)

# 사용자 입력 받기
term = input("철자 교정을 원하는 단어를 입력하세요: ")
term_decomposed = split_syllables(term)

# 제안어 검색
suggestions = sym_spell.lookup(term_decomposed, Verbosity.ALL, max_edit_distance=2)

# 편집 거리가 가장 작은 제안어 찾기
if suggestions:
    best_suggestion = min(suggestions, key=lambda x: x.distance)
    complete_word = join_jamos(best_suggestion.term)
    print(f"최고 제안어: {complete_word} (원본: {best_suggestion.term}, 거리: {best_suggestion.distance}, 빈도: {best_suggestion.count})")
else:
    print("제안어를 찾을 수 없습니다.")
