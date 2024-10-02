from langchain.chains.conversation.base import ConversationChain
from langchain_openai import ChatOpenAI

def openfile(pam_filename):
    content = ""
    with open(pam_filename, 'r', encoding='utf-8') as file:
        content = file.read()  # 读取并打印文件内容
    return content


def get_chat_response(prompt, memory, api_key):
    api_url = "https://api.xty.app/v1"
    api_model = "gpt-3.5-turbo"
    model = ChatOpenAI(model=api_model, openai_api_key=api_key, base_url=api_url)
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]