import os
from dotenv import load_dotenv
import sys
from dotenv import load_dotenv
import json
import base64
from volcenginesdkarkruntime import Ark 

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from app.utils.Modle.doubao import DoubaoChatLLM
from app.utils.DB.db import PetAIDB

from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain.agents.structured_output import ToolStrategy

load_dotenv()

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

dialog_schema = {
    "type":"object",
    "properties":{
        "dialog_list":{
            "type":"array",
            "items":{
                "type":"string",
                "description":"桌宠的简单话术"
            },
            "description":"桌宠的对话列表，包含8-10句简单话术"
        }
    },
    "required":["dialog_list"]
}

class CMAgent:
    def __init__(self, pet_name, world_prompt):
        self.pet_name = pet_name
        self.pet_story = ""
        self.pet_details = ""
        self.world_prompt = world_prompt
        self.world = ""
        self.pet_appearance = ""
        self.dialog = ""
        self.db = PetAIDB()
        self.doubaoLLM = DoubaoChatLLM()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        prompts_dir = os.path.join(current_dir, 'prompts')
        self.world_system_prompt = PromptTemplate.from_file(template_file=os.path.join(prompts_dir, "create_world_system_prompt.md"),encoding="utf-8").template
        self.world_user_prompt = PromptTemplate.from_file(template_file=os.path.join(prompts_dir, "create_world_user_prompt copy.md"),encoding="utf-8").template
        self.role_system_prompt = PromptTemplate.from_file(template_file=os.path.join(prompts_dir, "create_role_system_prompt.md"),encoding="utf-8").template
        self.role_user_prompt = PromptTemplate.from_file(template_file=os.path.join(prompts_dir, "create_role_user_prompt.md"),encoding="utf-8").template
        self.details_system_prompt = PromptTemplate.from_file(template_file=os.path.join(prompts_dir, "create_details_system_prompt.md"),encoding="utf-8").template
        self.dialog_system_prompt = PromptTemplate.from_file(template_file=os.path.join(prompts_dir, "create_dialog_system_prompt.md"),encoding="utf-8").template

    def createWorldAgent(self):
        """创建世界设定Agent"""
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
        """创建桌宠背景故事Agent"""
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
        """创建桌宠性格设定Agent"""
        tools = []
        agent = create_agent(
            model=self.doubaoLLM,
            tools=tools,
            response_format=ToolStrategy(pet_details),
            system_prompt=self.details_system_prompt,
        )
        self.pet_details = agent.invoke({"messages": [("user", f"桌宠故事：{self.pet_story}，世界设定：{self.world}")]})
        return self.pet_details

    def createDialogAgent(self):
        """创建桌宠对话Agent"""
        tools = []
        agent = create_agent(
            model=self.doubaoLLM,
            tools=tools,
            response_format=ToolStrategy(dialog_schema),
            system_prompt=self.dialog_system_prompt,
        )
        self.dialog = agent.invoke({"messages": [("user", f"桌宠故事：{self.pet_story}，世界设定：{self.world},桌宠性格：{self.pet_details['structured_response']['pet_personality']},沟通风格：{self.pet_details['structured_response']['pet_speech_style']}")]})
        dialog_list = self.dialog['structured_response']['dialog_list']
        dialog_list_clean = [line.replace('\n', '') for line in dialog_list]
        self.dialog_list = dialog_list_clean
        return self.dialog_list

    def getPetAppearance(self):
        """获取桌宠外观"""
        agent = create_agent(
            model=self.doubaoLLM,
        )
        self.pet_appearance = agent.invoke({"messages": [("system", "根据用户提供的世界观与人物故事，描写出该人物外形形象的主要特征，不需要进行其他分析。"),("user", f"桌宠故事：{self.pet_story}，世界设定：{self.world}")]})
        print(self.pet_appearance['messages'][-1].content)
        return self.pet_appearance['messages'][-1].content


    def createPetImage(self):
        """创建桌宠图片"""
        client = Ark(
            base_url="https://ark.cn-beijing.volces.com/api/v3", 
            api_key=os.environ.get("ARK_API_KEY"), 
        )
        image_prompt = self.getPetAppearance()
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        role_image_path = os.path.join(current_dir, "role.png")
        
        with open(role_image_path, 'rb') as f:
            image_data = f.read()
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            image_data_url = f"data:image/png;base64,{image_base64}"
        
        imagesResponse = client.images.generate( 
            model="doubao-seedream-5-0-260128", 
            prompt=f"参考这张图片，纯白背景，不要修改猫猫主题形象。{image_prompt}",
            image=image_data_url,
            size="1728x2304",
            output_format="png",
            response_format="url",
            watermark=False
        ) 
        return imagesResponse.data[0].url

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
    print("\n")
    dialog_list = cm_agent.createDialogAgent()
    print(dialog_list)
    print("\n")
    image = cm_agent.createPetImage()
    print(image)
