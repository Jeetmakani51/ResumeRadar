import os
from dotenv import load_dotenv
from crewai import Agent, LLM  
#from tools import tool

load_dotenv()

gemini_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.5
)

Data_Scout = Agent(
    role='Technical Resume Parser',
    goal='Identify and extract the candidate name, core technical skills, and years of experience',
    backstory='You are an expert at scanning messy text and finding specific technical details.',
    verbose=True,
    memory=False,
    #tools=[tool],
    llm=gemini_llm, 
    allow_delegation=False 
)

manager = Agent(
    role='Senior Technical Recruiter',
    goal='Score the candidate based on their extracted skills and fit for the given job description.',
    backstory='You provide the final verdict on whether we should hire someone.',
    llm=gemini_llm,
    #tools=[tool],
    allow_delegation=False
)