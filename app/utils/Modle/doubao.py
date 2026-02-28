from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

doubao = ChatOpenAI(
    # Replace with your API Key     
    openai_api_key=os.environ.get("ARK_API_KEY"), 
    # The base URL for model invocation
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",   
    # Replace with Model ID
    model="doubao-seed-2-0-pro-260215",

)

doubao_chat_agent = create_agent(
    model=doubao
)

if __name__ == "__main__":
    print("AI回复：", end="", flush=True)
    for chunk in doubao_chat_agent.stream({"messages": [("user", "你好")]},stream_mode="messages"):
        if chunk[0].content:
            print(chunk[0].content, end="", flush=True)
