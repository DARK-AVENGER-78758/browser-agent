import os
import uuid
import subprocess
import re
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Path to backend's .venv Python executable
PYTHON_EXECUTABLE = r"C:\Users\aniru\Desktop\Agentic-browser - Copy\agent-browser\backend\.venv\Scripts\python.exe"

app = FastAPI()

# Enable CORS to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure OpenRouter API (OpenAI SDK)
client = openai.OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# ----------------- ROUTES -----------------

@app.get("/")
def root():
    return {"message": "Backend is up and running."}

class TaskRequest(BaseModel):
    task: str

@app.post("/generate-script")
async def generate_script(req: TaskRequest):
    prompt = f"""
You are an Automation Agent. Generate a Python Playwright script that can perform this task:
{req.task}

Requirements:
- Use Playwright's sync API.
- The browser must launch with headless=False.
- The code must be inside a function named 'automate_task'.
- Add 'input("Press Enter to exit...")' after browser actions to keep it open.
- Ensure all necessary imports are present.
- The code should run standalone.

Respond ONLY with the complete code.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=700
        )

        code = response.choices[0].message.content

        # Extract code block content if it's inside triple backticks
        code_block = re.search(r"```python(.*?)```", code, re.DOTALL)
        if code_block:
            code = code_block.group(1).strip()

        # Ensure headless=False and input pause are present
        if 'headless=False' not in code:
            code = re.sub(r'launch\((.*?)\)', r'launch(headless=False)', code)
        
        if 'input(' not in code:
            code += '\n\ninput("Press Enter to exit...")'

        # Save script to backend/scripts/
        script_id = str(uuid.uuid4())
        os.makedirs("backend/scripts", exist_ok=True)
        script_path = f"backend/scripts/{script_id}.py"

        with open(script_path, "w") as f:
            f.write(code)

        return {"script_id": script_id, "script": code}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/execute-script/{script_id}")
async def execute_script(script_id: str):
    script_path = f"backend/scripts/{script_id}.py"
    if not os.path.exists(script_path):
        raise HTTPException(status_code=404, detail="Script not found.")

    try:
        # Detached subprocess to open browser visibly
        subprocess.Popen(
            [PYTHON_EXECUTABLE, script_path],
            creationflags=subprocess.CREATE_NEW_CONSOLE  # Important for Windows
        )
        return {"status": "Script execution started."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/run-sample-script")
def run_sample_script():
    script_path = os.path.join("backend", "scripts", "sample_open_linkedin.py")
    if not os.path.exists(script_path):
        raise HTTPException(status_code=404, detail="Sample script not found.")

    try:
        subprocess.Popen([PYTHON_EXECUTABLE, script_path], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
        return JSONResponse(content={"status": "Sample script execution started."})
    except Exception as e:
        return JSONResponse(content={"status": "Failed", "error": str(e)}, status_code=500)
