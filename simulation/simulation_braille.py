from package import braille as br
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

n_phrase = len(phrases)

word_lists = [] 
for i in range(n_phrase):
    tmp = re.split('[ ,.?!]', phrases[i])
    word_lists.append([x for x in tmp if x != ''])

braille_phrases = ["⠣⠒⠉⠻⠚⠠⠝⠬",
           "⠥⠉⠮⠀⠉⠂⠠⠠⠕⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
           "⠨⠎⠢⠠⠕⠢⠀⠠⠕⠁⠇⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
           "⠨⠕⠈⠪⠢⠀⠚⠽⠺⠀⠨⠍⠶⠕⠃⠉⠕⠊",
           "⠨⠽⠠⠿⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦⠠⠪⠃⠉⠕⠊",
           "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠫⠢⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
           "⠥⠉⠮⠀⠨⠎⠉⠱⠁⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂⠠⠫⠬",
           "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠚⠗",
           "⠋⠎⠙⠕⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
           "⠉⠗⠕⠂⠀⠣⠰⠕⠢⠀⠼⠓⠠⠕⠝⠀⠘⠽⠃⠈⠝⠌⠠⠪⠃⠉⠕⠊"]

reduced_phrases_set = [["⠣⠒⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴",
                        "⠨⠎⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎",
                        "⠕⠘⠾⠀⠙⠪⠀⠑⠣⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠝⠀⠻⠀⠘⠥⠀⠫⠂⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃⠈⠝⠌⠠⠪⠃⠉⠕⠊"],
                       ["⠣⠒⠉⠻⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠠⠿⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦⠠⠪⠃⠉⠕⠊",
                        "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠫⠢⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂⠠⠫⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃⠠⠪⠃⠉⠕⠊"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠠⠕⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠠⠿⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦⠠⠪⠃⠉⠕⠊",
                        "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠣⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴",
                        "⠨⠎⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦⠠⠪⠃⠉⠕⠊",
                        "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠫⠢⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠚⠗",
                        "⠋⠎⠙⠕⠀⠚⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒⠉⠻⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠠⠕⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦⠠⠪⠃⠉⠕⠊",
                        "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠣⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠀⠫⠂⠠⠫⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠙⠕⠀⠚⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠀⠉⠂⠫⠀⠨⠥⠴",
                        "⠨⠎⠢⠠⠕⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠺⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎",
                        "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠫⠢⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁",
                        "⠋⠎⠙⠕⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠰⠕⠢⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠀⠉⠂⠠⠠⠕⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎",
                        "⠕⠘⠾⠀⠙⠪⠀⠑⠣⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠀⠨⠎⠉⠱⠁⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠠⠕⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠺⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠠⠿⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦",
                        "⠕⠘⠾⠀⠙⠪⠀⠑⠫⠢⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠉⠱⠁⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠙⠕⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠠⠕⠝⠀⠘⠽⠃"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠠⠠⠕⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎",
                        "⠕⠘⠾⠀⠙⠪⠀⠑⠫⠢⠕⠂⠵⠀⠊⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃⠈⠝⠌⠠⠪⠃⠉⠕⠊"],
                       ["⠣⠒⠉⠻⠚⠠⠝⠬",
                        "⠥⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠠⠿⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦⠠⠪⠃⠉⠕⠊",
                        "⠕⠘⠾⠀⠙⠪⠀⠑⠫⠢⠕⠂⠵⠀⠊⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠀⠨⠎⠉⠱⠁⠝⠀⠻⠚⠧⠀⠘⠥⠀⠫⠂⠠⠫⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠚⠗",
                        "⠋⠎⠙⠕⠀⠚⠒⠀⠨⠒⠀⠚⠂",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒⠉⠻⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠠⠠⠕⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠀⠠⠕⠁⠇⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠺⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦",
                        "⠕⠘⠾⠀⠙⠪⠀⠑⠣⠕⠂⠵⠀⠊⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠀⠨⠎⠉⠱⠁⠝⠀⠻⠚⠧⠀⠘⠥⠀⠫⠂",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃⠈⠝⠌⠠⠪⠃⠉⠕⠊"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠀⠠⠕⠁⠇⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠠⠿⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎",
                        "⠕⠘⠾⠀⠙⠪⠀⠑⠣⠕⠂⠵⠀⠊⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂⠠⠫⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠠⠕⠢⠀⠠⠕⠁⠇⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠺⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦⠠⠪⠃⠉⠕⠊",
                        "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠣⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠉⠱⠁⠝⠀⠻⠚⠧⠀⠘⠥⠀⠫⠂⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠠⠕⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠺⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎",
                        "⠕⠘⠾⠀⠙⠪⠀⠑⠫⠢⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠙⠕⠀⠚⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒⠉⠻⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠠⠕⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠺⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎",
                        "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠣⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂⠠⠫⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠰⠕⠢⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠀⠚⠽⠺⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎",
                        "⠕⠘⠾⠀⠙⠪⠀⠑⠫⠢⠕⠂⠵⠀⠊⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂⠠⠫⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠀⠉⠪⠅⠮⠀⠸⠎",
                        "⠕⠘⠾⠀⠙⠪⠀⠑⠣⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠉⠱⠁⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂⠠⠫⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃⠈⠝⠌⠠⠪⠃⠉⠕⠊"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠺⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦",
                        "⠕⠘⠾⠀⠙⠪⠀⠑⠫⠢⠕⠂⠵⠀⠊⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠙⠕⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠀⠉⠂⠠⠠⠕⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠠⠕⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦⠠⠪⠃⠉⠕⠊",
                        "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠣⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠉⠱⠁⠝⠀⠻⠚⠧⠀⠘⠥⠀⠫⠂",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃⠈⠝⠌⠠⠪⠃⠉⠕⠊"],
                       ["⠣⠒⠉⠻⠚⠠⠝⠬",
                        "⠥⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠺⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎",
                        "⠕⠘⠾⠀⠙⠪⠀⠑⠣⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠉⠱⠁⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃⠈⠝⠌⠠⠪⠃⠉⠕⠊"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦⠠⠪⠃⠉⠕⠊",
                        "⠕⠘⠾⠀⠙⠪⠀⠑⠣⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂⠠⠫⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁",
                        "⠋⠎⠙⠕⠀⠚⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠺⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠠⠿⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦⠠⠪⠃⠉⠕⠊",
                        "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠣⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠉⠱⠁⠝⠀⠻⠀⠘⠥⠐⠎⠀⠫⠂⠠⠫⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠠⠠⠕⠫⠀⠨⠥⠴",
                        "⠨⠎⠢⠠⠕⠢⠀⠠⠕⠁⠇⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠺⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠠⠿⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦⠠⠪⠃⠉⠕⠊",
                        "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠫⠢⠕⠂⠵⠀⠊⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠰⠕⠢⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒⠉⠻⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠺⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠠⠿⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎",
                        "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠣⠕⠂⠵⠀⠊⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂⠠⠫⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠙⠕⠀⠚⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠰⠕⠢⠀⠼⠓⠝⠀⠘⠽⠃⠈⠝⠌⠠⠪⠃⠉⠕⠊"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠠⠕⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦",
                        "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠣⠕⠂⠵⠀⠊⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂⠠⠫⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠙⠕⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃⠈⠝⠌⠠⠪⠃⠉⠕⠊"],
                       ["⠣⠒⠉⠻⠚⠠⠝⠬",
                        "⠥⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠠⠕⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠺⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎",
                        "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠣⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠝⠀⠻⠀⠘⠥⠀⠫⠂⠠⠫⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁",
                        "⠋⠎⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒",
                        "⠥⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠠⠿⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎",
                        "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠣⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠉⠮⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂⠠⠫⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠙⠕⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠠⠕⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠠⠿⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦⠠⠪⠃⠉⠕⠊",
                        "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠣⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂⠠⠫⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃⠈⠝⠌⠠⠪⠃⠉⠕⠊"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴",
                        "⠨⠎⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠀⠉⠪⠅⠮⠀⠸⠎",
                        "⠕⠘⠾⠀⠙⠪⠀⠑⠣⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠀⠨⠎⠝⠀⠻⠚⠧⠀⠘⠥⠐⠎⠀⠫⠂⠠⠫⠬",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠰⠕⠢⠀⠼⠓⠝⠀⠘⠽⠃"],
                       ["⠣⠒⠚⠠⠝⠬",
                        "⠥⠉⠮⠀⠉⠂⠫⠀⠨⠥⠴⠠⠪⠃⠉⠕⠊",
                        "⠨⠎⠢⠀⠠⠕⠁⠀⠑⠄⠕⠌⠈⠝⠀⠚⠠⠝⠬",
                        "⠨⠕⠈⠪⠢⠀⠚⠽⠀⠨⠍⠶⠕⠃⠉⠕⠊",
                        "⠨⠽⠚⠃⠉⠕⠊⠀⠨⠥⠈⠪⠢⠀⠉⠪⠅⠮⠀⠸⠎⠀⠫⠦⠠⠪⠃⠉⠕⠊",
                        "⠕⠘⠾⠀⠙⠪⠐⠥⠨⠝⠁⠓⠪⠀⠑⠫⠢⠕⠂⠵⠀⠊⠣⠪⠢⠀⠨⠍⠕⠃⠉⠕⠊",
                        "⠥⠀⠨⠎⠉⠱⠁⠝⠀⠻⠚⠧⠀⠘⠥⠀⠫⠂",
                        "⠠⠗⠶⠕⠂⠀⠰⠍⠁⠚⠗",
                        "⠋⠎⠙⠕⠀⠚⠒⠀⠨⠒⠀⠚⠂⠐⠗⠬",
                        "⠉⠗⠕⠂⠀⠣⠀⠼⠓⠝⠀⠘⠽⠃"]]

n_test = len(reduced_phrases_set)
word_recommendation_clicks = [len(word_list) for word_list in word_lists]
send_clicks = [len(phrase) for phrase in phrases]

braille_clicks = []
reduced_braille_clicks = [0 for _ in range(n_phrase)]
clicks = []
reduced_clicks = []
ratio = []

for phrase in braille_phrases:
    braille_clicks.append(br.calculate_click(phrase));

for i in range(n_test):
    for j in range(len(reduced_phrases_set[i])):
        reduced_braille_clicks[j] += br.calculate_click(reduced_phrases_set[i][j]);

for i in range(n_phrase):
    reduced_braille_clicks[i] /= n_test
    clicks.append(braille_clicks[i] + send_clicks[i])
    reduced_clicks.append(reduced_braille_clicks[i] + send_clicks[i] + word_recommendation_clicks[i])
    ratio.append(1 - reduced_clicks[i]/clicks[i])

print(clicks)
print(reduced_clicks)
print(ratio)
print(sum(ratio)/n_phrase)