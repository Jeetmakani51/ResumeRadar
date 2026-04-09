from fastapi import FastAPI, UploadFile, File
import pdfplumber
from crewai import Crew, Process
from tasks import extraction_task, profiling_task
from agents import Data_Scout, manager
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()


@app.post("/uploadFile/")
async def upload_and_read(file: UploadFile = File(...)):
    file.file.seek(0)
    content = ""

    
    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            # 1. Extract regular text
            content += page.extract_text() or ""
            
            # 2. Extract Tables 
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    clean_row = [str(item) for item in row if item is not None]
                    content += " | ".join(clean_row) + "\n"

    # Define the Crew
    resume_crew = Crew(
        agents=[Data_Scout, manager],
        tasks=[extraction_task, profiling_task],
        process=Process.sequential,
        verbose=True
    )
    
    
    result = resume_crew.kickoff(inputs={
        'resume_text': content,
        'job_description': "We are looking for a Python Developer with experience in FastAPI and AI Agents."
    })

    return {
        "filename": file.filename,
        "length": len(content),
        "ai_analysis": str(result)
    }

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index():
    return FileResponse("static/index.html")
