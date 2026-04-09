'''from dotenv import load_dotenv
import os
from crewai_tools import SerperDevTool
load_dotenv()

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
tool = SerperDevTool() #checks what the certification actually covers
'''

'''from dotenv import load_dotenv
import os
from crewai_tools import SerperDevTool

load_dotenv()

serper_key = os.getenv('SERPER_API_KEY')
if not serper_key:
    raise ValueError("SERPER_API_KEY is not set in your .env file")

os.environ['SERPER_API_KEY'] = serper_key
tool = SerperDevTool()
'''