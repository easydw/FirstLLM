# 下面代码可以应用于OpenAI,也可以应用与本地部署的Ollama中的模型.
# 只需要更换以下api_key、api_url、api_model即可,其他代码不需要修改

from openai import OpenAI
import streamlit as st

# 从环境变量中获取 API 密钥和自定义 base URL
# OpenAI代理网站
api_key = "sk-juMgledj3GhuZWdoFc28145bEd404b83Ba0d912f0780108b"
api_url = "https://api.xty.app/v1"
api_model = "gpt-3.5-turbo"

# 创建 OpenAI 客户端实例
client = OpenAI(api_key=api_key, base_url=api_url)

def run_Api(promt):
    completion = client.chat.completions.create(
        model=api_model,
        # messages=promt,
        messages=[
            {'role': 'system', 'content': '你是一位崔永元风格的脱口秀演员'},
            {"role": "user", "content": promt}],
        temperature=0.8,
        top_p=0.8,
        stream=False
    )
    return completion.choices[0].message.content

# 调用方法: 实时现实
def runapi_real(promt):
    completion = client.chat.completions.create(
        model=api_model,
        messages=[
            {'role': 'system', 'content': '你是一位崔永元风格的脱口秀演员'},
            {"role": "user", "content": promt}],
        temperature=0.8,
        top_p=0.8,
        stream=True
    )
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")


def mainchat(input):
    user_input = input
    print("输入完成，等待返回...")
    # 执行方法
    msgret = run_Api(user_input)
    # 结果输出
    print(msgret)
    return msgret

# 定义 mainchat 函数
def mainchat(input):
    user_input = input
    retmsg = "输入完成，等待返回..."
    # 执行方法
    msgret = run_Api(user_input)
    retmsg += f"\n{msgret}"
    # 结果输出
    print(msgret)
    return retmsg

# Streamlit 页面布局
st.title("聊天应用")

# 输入框
user_input = st.text_input("请输入内容:")

# 提交按钮
if st.button("提交"):
    # 调用 mainchat 方法
    result = mainchat(user_input)
    # 在页面上显示结果
    st.write("返回结果:")
    st.write(result)

