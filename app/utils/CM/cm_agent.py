import os
from dotenv import load_dotenv

from Modle.doubao import doubao
from DB.db import PetAIDB
from langchain.agents import create_agent
