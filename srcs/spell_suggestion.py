import pandas as pd
from symspellpy import SymSpell, Verbosity
from hangul_utils import split_syllables, join_jamos

def is_hangul_char(char):
    return '가' <= char <= '힣'

#자모 분해
def safe_split_syllables(term):
    return ''.join([split_syllables(char) if is_hangul_char(char) else char for char in term])

# 오타 교정 함수
def correct_spelling(user_input, input_file="ko_50k.txt", output_file="ko_50k_decomposed.txt"):
    # CSV 파일 읽기 및 자소 단위로 분해하여 저장
    vocab = pd.read_csv(input_file, sep=" ", names=["term", "count"])
    vocab['term'] = vocab['term'].map(safe_split_syllables)
    vocab.to_csv(output_file, sep=" ", header=None, index=None, encoding='utf-8')

    # SymSpell 초기화 및 사전 로드
    sym_spell = SymSpell(max_dictionary_edit_distance=2)
    with open(output_file, 'r', encoding='utf-8') as file:
        sym_spell._load_dictionary_stream(file, term_index=0, count_index=1)

    # 오타 교정 제안
    term_decomposed = split_syllables(user_input)
    suggestions = sym_spell.lookup(term_decomposed, Verbosity.ALL, max_edit_distance=2)
    if not suggestions:
        return None
    best_suggestion = min(suggestions, key=lambda sugg: sugg.distance)
    if best_suggestion.distance == 0:
        return None

    # 결과 반환
    results = join_jamos(best_suggestion.term)
    audio_msg = f"오타가 감지되었습니다. {results}로 교정하시겠습니까?"
    print(audio_msg)
    os.system(f'espeak -v ko "{audio_msg}" --stdout | sox -t wav - -r 48000 -c 2 -t wav - gain -n bass +3 treble +6 | aplay -D hw:0,0')
    return results

# 스크립트 테스트 코드 추후 삭제
if __name__ == "__main__":
    user_input = input("오타 교정을 테스트할 단어를 입력하세요: ")
    result = correct_spelling(user_input)
    if result:
        print(f"교정 결과: {result}")
    else:
        print("오타가 없거나 제안어를 찾을 수 없습니다.")
