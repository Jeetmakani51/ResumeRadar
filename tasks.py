from crewai import Task
#from tools import tool
from agents import Data_Scout,manager

extraction_task=Task(
    description="Analyze the following raw resume text: {resume_text}. "
                        "Carefully extract the candidate's full name, contact information, "
                        "list of technical skills, and total years of professional experience.",
    expected_output="A structured summary of the candidate's profile including Name, "
                            "Skills, and Experience. Do not hallucinate; if information is missing, say 'Not Found'.",
    #tools=[tool],
    agent=Data_Scout,
)

profiling_task=Task(
    description="Review the extracted candidate profile provided by the Scout. "
                        "Compare their skills against this Job Description: {job_description}. "
                        "Determine if the candidate is a 'Match', 'Potential', or 'No Match'.",
    expected_output="A final evaluation report. Include a 'Fit Score' (0-100) and "
                            "a 3-sentence justification of your decision.",
    #tools=[tool],
    agent=manager,
    context=[extraction_task]
)