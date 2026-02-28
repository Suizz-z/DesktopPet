import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from app.utils.Modle.doubao import DoubaoChatLLM
from app.utils.DB.db import PetAIDB

from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain.agents.structured_output import ToolStrategy

pet_details = {
    "type":"object",
    "properties":{
        "pet_personality":{
            "type":"string",
            "description":"桌宠的性格"
        },
        "pet_speech_style":{
            "type":"string",
            "description":"桌宠的沟通风格"
        }
    }
}

class CMAgent:
    def __init__(self, pet_name, world_prompt):
        self.pet_name = pet_name
        self.pet_story = ""
        self.pet_details = ""
        self.world_prompt = world_prompt
        self.world = ""
        self.db = PetAIDB()
        self.doubaoLLM = DoubaoChatLLM()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        prompts_dir = os.path.join(current_dir, 'prompts')
        self.world_system_prompt = PromptTemplate.from_file(template_file=os.path.join(prompts_dir, "create_world_system_prompt.md"),encoding="utf-8").template
        self.world_user_prompt = PromptTemplate.from_file(template_file=os.path.join(prompts_dir, "create_world_user_prompt copy.md"),encoding="utf-8").template
        self.role_system_prompt = PromptTemplate.from_file(template_file=os.path.join(prompts_dir, "create_role_system_prompt.md"),encoding="utf-8").template
        self.role_user_prompt = PromptTemplate.from_file(template_file=os.path.join(prompts_dir, "create_role_user_prompt.md"),encoding="utf-8").template
        self.details_system_prompt = PromptTemplate.from_file(template_file=os.path.join(prompts_dir, "create_details_system_prompt.md"),encoding="utf-8").template

    def createWorldAgent(self):
        user_prompt = self.world_user_prompt.format(world_prompt=self.world_prompt)
        doubao_chat_agent = create_agent(
            model=self.doubaoLLM,
            system_prompt=self.world_system_prompt,
        )
        for chunk in doubao_chat_agent.stream({"messages": [("user", user_prompt)]}, stream_mode="messages"):
            if chunk[0].content:
                self.world += chunk[0].content  
                yield chunk[0].content

    def createRoleAgent(self):
        user_prompt = self.role_user_prompt.format(pet_name=self.pet_name, world=self.world)
        doubao_chat_agent = create_agent(
            model=self.doubaoLLM,
            system_prompt=self.role_system_prompt,
        )
        for chunk in doubao_chat_agent.stream({"messages": [("user", user_prompt)]}, stream_mode="messages"):
            if chunk[0].content:
                self.pet_story += chunk[0].content  
                yield chunk[0].content
    
    def createPet(self):
        tools = []
        agent = create_agent(
            model=self.doubaoLLM,
            tools=tools,
            response_format=ToolStrategy(pet_details),
            system_prompt=self.details_system_prompt,
        )
        self.pet_details = agent.invoke({"messages": [("user", f"桌宠故事：{self.pet_story}，世界设定：{self.world}")]})

    

if __name__ == "__main__":
    cm_agent = CMAgent("小明", "武侠世界")
    world_agent = cm_agent.createWorldAgent()
    for chunk in world_agent:
        print(chunk, end="", flush=True)
    print("\n")
    role_agent = cm_agent.createRoleAgent()
    for chunk in role_agent:
        print(chunk, end="", flush=True)
    print("\n")
    cm_agent.createPet()
    print(cm_agent.pet_details['structured_response'])
