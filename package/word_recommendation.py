import google.generativeai as genai
import os

os.environ["GRPC_DNS_RESOLVER"] = "native"

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
        "candidate_count": 1,
        "temperature": 1.0,
}
safety_settings = [{"category": "HARM_CATEGORY_DANGEROUS",
                    "threshold": "BLOCK_NONE", },
                   {"category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_NONE", },
                   {"category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_NONE", },
                   {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_NONE", },
                   {"category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_NONE", }, ]

model = genai.GenerativeModel(model_name = "gemini-pro",
                              generation_config = generation_config,
                              safety_settings = safety_settings)

def generate_content(prompt):
    result = ""
    response = model.generate_content(prompt)
    for chunk in response:
        result += chunk.text
    return result

def recommend_word(phrase):
    uncompleted_word = phrase[phrase.rfind(' ') + 1:]
    prompt = f"다음 조건에 맞게 단어 세 가지를 \",\"로 구분해서 추천해줘.\n" \
            f"- \"{phrase}\" 다음에 올 단어를 추천한다.\n" \
            f"- '{uncompleted_word}'(으)로 시작하는 단어를 추천한다.\n" 
    response = generate_content(prompt)
    word_list = response.split(', ')
    return word_list

def recommend_word_history_base(phrase, word_history):
    uncompleted_word = phrase[phrase.rfind(' ') + 1:]
    prompt = f"사용자는 이전에 다음과 같은 단어들을 입력했어.\n" \
            f"{word_history}\n\n" \
            f"다음 조건에 맞게 단어 세 가지를 \",\"로 구분해서 추천해줘.\n" \
            f"- \"{phrase}\" 다음에 올 단어를 추천한다.\n" \
            f"- '{uncompleted_word}'(으)로 시작하는 단어를 추천한다.\n" \
            f"- 사용자의 이전 입력을 기반으로 추천한다.\n"
    response = generate_content(prompt)
    word_list = response.split(', ')
    return word_list
