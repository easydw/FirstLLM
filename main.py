import util
from langchain.memory import ConversationBufferMemory
import streamlit as st

def test():
    # apikey = "sk-juMgledj3GhuZWdoFc28145bEd404b83Ba0d912f0780108b"
    apikey = util.openfile("apikey.txt")
    print(apikey)
    memory = ConversationBufferMemory(return_messages=True)
    # ret1 = get_chat_response("宇宙速度有几个,不要问我问题,直接回答", memory, api_key=apikey)
    # print("第一个问题回答:")
    # print(ret1)
    # ret2 = get_chat_response("解释第二速度,不要问我问题,直接回答", memory, api_key=apikey)
    # print("第二个问题回答:")
    # print(ret2)

    ret1 = util.get_chat_response("水缸中两个体积相同的球,A球漂浮,B球沉底,分析两个球浮力大小,不要问我问题,直接回答", memory, api_key=apikey)
    print("第一个问题回答:")
    print(ret1)
    print("第二个问题回答:")
    ret2 = util.get_chat_response("解释下B球的现象,不要问我问题,直接回答", memory, api_key=apikey)
    print(ret2)

# test()
def newTalk():
    if "memory" in st.session_state:
        del st.session_state["memory"]

st.title("仿真chatGPT")
# 左侧
with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API Key:", type="password")
    st.markdown("[获取OpenAI API Key](https://api.xty.app/)")
    st.button("新对话", on_click=newTalk)
# 右侧
# 初始化内存对象
if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory()
    st.session_state["messages"] = [{"role": "ai",
                                    "content": "你好,我是AI助手,有什么可以帮您的?"}]
# 展示message中的各项信息
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

# 接受用户输入
prompt = st.chat_input()
if prompt:
    if not openai_api_key:
        st.info("请输入您的OpenAI API Key")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    # 调用和等待chatGPT的返回
    with st.spinner("AI正在思考中, 请等待..."):
        # st.balloons()
        response = util.get_chat_response(prompt, st.session_state["memory"],
                               api_key=openai_api_key)
        st.session_state["messages"].append({"role": "ai", "content": response})
        st.chat_message("ai").write(response)
