from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

class DoubaoChatLLM(ChatOpenAI):
    def __init__(self):
        super().__init__(
            openai_api_key=os.environ.get("ARK_API_KEY"), 
            openai_api_base="https://ark.cn-beijing.volces.com/api/v3",   
            model="doubao-seed-2-0-pro-260215",
        )



if __name__ == "__main__":
    agent = DoubaoChatLLM()
    doubao_chat_agent = create_agent(
        model=agent
    )
    full_response = ""
    for chunk in doubao_chat_agent.stream({"messages": [("user", "你好")]},stream_mode="messages"):
        if chunk[0].content:
            full_response += chunk[0].content
            print(chunk[0].content, end="", flush=True)
    print("\nfull_response:", full_response)