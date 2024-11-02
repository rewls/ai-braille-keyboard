import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import hub
from langchain_chroma import Chroma
from langchain.schema.document import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PipelinePromptTemplate, PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def format_last_word(history):
    return history[history.rfind(" ") + 1:]


def format_question(history):
    return history[-25:]


def recommend_word_rag(history):
    model = ChatGoogleGenerativeAI(
            model="gemini-pro",
            generation_config = genai.types.GenerationConfig(
                max_output_tokens = 10,
                temperature = 0))

    docs = [Document(page_content=history.replace(format_question(history), ""))]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=50,
                                                   chunk_overlap=10)
    splits = text_splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(documents=splits,
                                        embedding=GoogleGenerativeAIEmbeddings(
                                            model="models/embedding-001"))

    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    full_template = """{rag}

    {example}"""
    full_prompt = PromptTemplate.from_template(full_template)

    rag_template = """당신은 단어 추천 작업의 보조자입니다. 단어 추천 개수는 3개입니다. 3개의 단어를 공백없이 ","로 구분하여 답합니다. 각 단어는 주어진 입력에서 마지막 어절로 시작해야합니다. 다음 검색된 문맥 조각은 사용자의 이전 입력입니다. 문맥 조각을 고려해서 질문에 답하세요.

    문맥: {context}

    """
    rag_prompt = PromptTemplate.from_template(rag_template)

    example_prompt = PromptTemplate.from_template(
            "입력: {question}\n마지막 어절: {last_word}\n추천 단어 리스트: {word_list}")

    examples = [
            {
                "question": "안",
                "last_word": "안",
                "word_list": "안녕,안녕하세요,안녕하십니까"
                },
            {
                "question": "잘 부",
                "last_word": "부",
                "word_list": "부탁드립니다,부탁드려요,부탁드리겠습니다"
                },
            {
                "question": "오늘 날",
                "last_word": "날",
                "word_list": "날씨,날씨가,날씨는"
                },
            {
                "question": "이번 주말에 뭐",
                "last_word": "뭐",
                "word_list": "뭐해,뭐할까,뭐하면"
                },
            {
                "question": "도와주셔서 정말 감사",
                "last_word": "감사",
                "word_list": "감사합니다,감사해요,감사드립니다"
                },
            ]

    example_prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        suffix="입력: {history}\n마지막 어절: {last_word}\n추천 단어 리스트:",
        input_variables=["history", "last_word"],
        )

    input_prompts = [
            ("rag", rag_prompt),
            ("example", example_prompt),
            ]

    pipeline_prompt = PipelinePromptTemplate(
            final_prompt=full_prompt, pipeline_prompts=input_prompts
            )

    rag_chain = (
            {"context": retriever | format_docs,
             "question": format_question, "history": RunnablePassthrough(),
             "last_word": format_last_word}
            | pipeline_prompt
            | model
            | StrOutputParser()
            )

    return rag_chain.invoke(history).split(",")


def recommend_word_example(question):
    model = ChatGoogleGenerativeAI(
            model="gemini-pro",
            generation_config = genai.types.GenerationConfig(
                max_output_tokens = 10,
                temperature = 0))

    example_prompt = PromptTemplate.from_template(
            "입력: {question}\n마지막 어절: {last_word}\n추천 단어 리스트: {word_list}")

    examples = [
            {
                "question": "안",
                "last_word": "안",
                "word_list": "안녕,안녕하세요,안녕하십니까"
                },
            {
                "question": "잘 부",
                "last_word": "부",
                "word_list": "부탁드립니다,부탁드려요,부탁드리겠습니다"
                },
            {
                "question": "오늘 날",
                "last_word": "날",
                "word_list": "날씨,날씨가,날씨는"
                },
            {
                "question": "이번 주말에 뭐",
                "last_word": "뭐",
                "word_list": "뭐해,뭐할까,뭐하면"
                },
            {
                "question": "도와주셔서 정말 감사",
                "last_word": "감사",
                "word_list": "감사합니다,감사해요,감사드립니다"
                },
            ]

    prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        prefix="당신은 단어 추천 작업의 보조자입니다. 단어 추천 개수는 3개입니다. 3개의 단어를 공백없이 \",\"로 구분하여 답합니다. 각 단어는 주어진 입력에서 마지막 어절로 시작해야합니다.",
        suffix="입력: {question}\n마지막 어절: {last_word}\n추천 단어 리스트:",
        input_variables=["question", "last_word"],
        )

    rag_chain = (
            {"question": RunnablePassthrough(), "last_word": format_last_word}
            | prompt 
            | model
            | StrOutputParser()
            )

    return rag_chain.invoke(question).split(",")


def recommend_word(history):
    model = genai.GenerativeModel(
            model_name = "gemini-pro",
            generation_config = genai.types.GenerationConfig(
                max_output_tokens = 10,
                temperature = 0))
    last_word = history[history.rfind(" ") + 1:]
    prompt = f"""
    당신은 단어 추천 작업의 보조자입니다. 단어 추천 개수는 3개입니다. 3개의 단어를 공백없이 \",\"로 구분하여 답합니다. 각 단어는 주어진 입력에서 마지막 어절로 시작해야합니다.
    
    입력: {history}
    마지막 어절: {last_word}
    추천 단어 리스트:"""
    response = model.generate_content(prompt)
    word_list = response.text.split(",")
    return word_list


if __name__ == "__main__":
    import time
    start_time = time.time()
    print(recommend_word("오늘 회사에서 중요한 발표를 했어요. 발표를 준비하면서 많이 긴장되었지만, 무사히 마칠 수 있어서 정말 다행입니다. 발표를 준비하면서 많은 동료들의 도움을 받았어요. 동료들이 도와준 덕분에 발표를 잘 마칠 수 있었어요. 발표가 끝나고 나니 긴장이 풀리면서 피로가 몰려왔어요. 하지만 중요한 일을 잘 마쳤다는 생각에 기분이 좋았어요. 오늘 발표를 통해 많은 것을 배울 수 있었어요. 앞으로도 더 열심히 노력해야겠다는 다짐을 하게 되었습니다. 오늘 하루도 무사히 마칠 수 있어서 다"))
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print(recommend_word_example("오늘 회사에서 중요한 발표를 했어요. 발표를 준비하면서 많이 긴장되었지만, 무사히 마칠 수 있어서 정말 다행입니다. 발표를 준비하면서 많은 동료들의 도움을 받았어요. 동료들이 도와준 덕분에 발표를 잘 마칠 수 있었어요. 발표가 끝나고 나니 긴장이 풀리면서 피로가 몰려왔어요. 하지만 중요한 일을 잘 마쳤다는 생각에 기분이 좋았어요. 오늘 발표를 통해 많은 것을 배울 수 있었어요. 앞으로도 더 열심히 노력해야겠다는 다짐을 하게 되었습니다. 오늘 하루도 무사히 마칠 수 있어서 다"))
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print(recommend_word_rag("오늘 회사에서 중요한 발표를 했어요. 발표를 준비하면서 많이 긴장되었지만, 무사히 마칠 수 있어서 정말 다행입니다. 발표를 준비하면서 많은 동료들의 도움을 받았어요. 동료들이 도와준 덕분에 발표를 잘 마칠 수 있었어요. 발표가 끝나고 나니 긴장이 풀리면서 피로가 몰려왔어요. 하지만 중요한 일을 잘 마쳤다는 생각에 기분이 좋았어요. 오늘 발표를 통해 많은 것을 배울 수 있었어요. 앞으로도 더 열심히 노력해야겠다는 다짐을 하게 되었습니다. 오늘 하루도 무사히 마칠 수 있어서 정말 다"))
    print("--- %s seconds ---" % (time.time() - start_time))
