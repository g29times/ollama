# https://kimi.moonshot.cn/chat/cncmjtg3r0738pmi74rg
import streamlit as st
from llm import send_chat_request
import traceback

# 助手基类
class Assistant:
    def __init__(self, name):
        self.name = name
        self._exception_occurred = False

    def respond(self, sub, prompt):
        self._exception_occurred = False  # 重置异常状态
        # 这里可以是一些逻辑来生成响应
        try:
            # 尝试调用外联方法send_chat_request
            return send_chat_request(self.name, prompt)
        except Exception as e:
            traceback.print_exc()
            self._exception_occurred = True  # 标记异常发生
            # 如果发生异常，返回默认语句
            return f"{sub} An error occurred :("
            # return "An error occurred. I'm unable to process your request."

# 马里奥助手
class MarioAssistant(Assistant):
    def __init__(self):
        super().__init__("mario")

    def respond(self, sub, prompt):
        # 马里奥特有的响应逻辑
        # return f"{self.name} says: Let's go to the Mushroom Kingdom!"
        return super().respond(f"{self.name} says: ", prompt)

        # # 马里奥特有的开头
        # marioe_say = "Hi! I'm Mario. "
        # # 调用基类的respond方法获取通用回答
        # response = super().respond(prompt)
        # # 如果没有异常发生，直接返回基类的回答
        # if not self._exception_occurred:
        #     return response
        # # 如果异常发生，添加马里奥的特定开头
        # return f"{marioe_say}{response}"

# 变形金刚助手
class MJAssistant(Assistant):
    def __init__(self):
        super().__init__("mj")

    def respond(self, sub, prompt):
        # 变形金刚特有的响应逻辑
        # return f"{self.name} says: Autobots, roll out!"
        return super().respond(f"{self.name} says: Hi, I'm QQ, I can do prompt refine!", prompt)

# 助手工厂
def get_assistant(name):
    if name == "mario":
        # if "messages" not in st.session_state:
        #     st.session_state["messages"] = [{"role": "assistant", "content": "💬 Hi! I'm Mario. How can I help you?"}]
        # # 显示聊天记录
        # messages = st.session_state.get("messages", [])
        # for msg in messages:
        #     st.chat_message(msg["role"]).write(msg["content"])
        return MarioAssistant()
    elif name == "mj":
        # if "messages" not in st.session_state:
        #     st.session_state["messages"] = [{"role": "assistant", "content": "💬 Hi! I'm QQ. How can I help you?"}]
        # # 显示聊天记录
        # messages = st.session_state.get("messages", [])
        # for msg in messages:
        #     st.chat_message(msg["role"]).write(msg["content"])
        return MJAssistant()
    else:
        return None

# 主程序
def main():
    st.title("🍄 Hello Chatbot")
    st.caption("🚀 Choose your assistant! ❤️")

    # 鉴权 https://www.myaiexp.com/blog/ai/duo-mo-tai-yu-yan-mo
    st.write("Welcome to the World! You can proceed by providing your API Key")
    # 定义一个预期的API Key值
    EXPECTED_API_KEY = "654321"

    with st.expander("Provide Your API Key"):
        my_api_key = st.text_input("API Key=654321", key="google_api_key", type="password")

    if not my_api_key:
    # 如果API Key为空或值不正确，显示错误信息并停止程序
        st.info("Enter the API Key to continue")
        st.stop()

    # 检查API Key的值是否正确
    if my_api_key != EXPECTED_API_KEY:
        st.error("Invalid API Key. Please enter the correct API Key.")
        st.stop()

    # 选择多个助手 https://kimi.moonshot.cn/chat/cne2r26cp7ff5ft3lhdg
    selected_assistant_name = st.selectbox("Select your assistant", ["mario", "mj"])
    if selected_assistant_name:
        assistant = get_assistant(selected_assistant_name)
        if assistant:
            st.session_state["assistant"] = assistant

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "💬 Hi! How can I help you?"}]

    # 显示聊天记录
    messages = st.session_state.get("messages", [])
    for msg in messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # 用户输入
    if prompt := st.chat_input("💬 Type a message"):
        user_role = "user"
        message = {"role": user_role, "content": prompt}
        st.session_state["messages"].append(message)
        st.chat_message(user_role).write(prompt)

        # 生成助手响应
        response = assistant.respond(selected_assistant_name, prompt)
        response_message = {"role": "assistant", "content": response}
        st.session_state["messages"].append(response_message)
        st.chat_message("assistant").write(response)

if __name__ == "__main__":
    main()