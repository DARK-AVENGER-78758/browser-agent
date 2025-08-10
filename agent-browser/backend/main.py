import os
import sys
import uuid
import subprocess
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import openai
import re

# Load environment variables
load_dotenv()

# Path to backend's .venv Python executable
PYTHON_EXECUTABLE = r"C:\Users\aniru\Desktop\Agentic-browser - Copy\agent-browser\backend\.venv\Scripts\python.exe"

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure OpenRouter API client
client = openai.OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Health check
@app.get("/")
def root():
    return {"message": "Backend is up and running."}

# Request model
class TaskRequest(BaseModel):
    task: str

# Generate script
@app.post("/generate-script")
async def generate_script(req: TaskRequest):
    # Master prompt to ensure reliable Playwright scripts
    prompt = f"""
You are an expert Automation Agent. Generate a **fully working Python Playwright script** to perform the following task:
{req.task}

Strict, Non-Negotiable Rules:
1. Always import Playwright exactly like this:
   from playwright.sync_api import sync_playwright
2. Always wrap the automation in:
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)
       page = browser.new_page()
       ...
       browser.close()
3. Place all automation code inside a function named automate_task().
4. Include all required imports at the top of the script.
5. The script must be runnable as a standalone file:
   if __name__ == "__main__":
       automate_task()
6. At the end of the automation, print a clear success message.
7. Do NOT use async/await, only synchronous Playwright API.
8. The code must run without modification if Playwright is installed.
9. Respond ONLY with the Python code inside a ```python fenced code block.

Now, generate the correct Python script.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=500
        )

        code = response.choices[0].message.content

        # Extract only the code from triple backticks
        match = re.search(r"```(?:python)?(.*?)```", code, re.DOTALL)
        if match:
            code = match.group(1).strip()

        # Save to backend/scripts folder
        script_id = str(uuid.uuid4())
        os.makedirs("backend/scripts", exist_ok=True)
        script_path = f"backend/scripts/{script_id}.py"
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(code)

        return {"script_id": script_id, "script": code}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Execute script (wait until finished, no terminal popup)
@app.post("/execute-script/{script_id}")
async def execute_script(script_id: str):
    script_path = f"backend/scripts/{script_id}.py"
    if not os.path.exists(script_path):
        raise HTTPException(status_code=404, detail="Script not found.")

    try:
        startupinfo = None
        creationflags = 0
        if sys.platform.startswith("win"):
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            creationflags = subprocess.CREATE_NO_WINDOW

        result = subprocess.run(
            [PYTHON_EXECUTABLE, script_path],
            capture_output=True,
            text=True,
            startupinfo=startupinfo,
            creationflags=creationflags
        )

        # Only say "no output" if absolutely nothing was printed
        output_message = result.stdout.strip() if result.stdout.strip() else "No output from script."

        return {
            "stdout": output_message,
            "stderr": result.stderr.strip(),
            "returncode": result.returncode
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run sample script
@app.post("/run-sample-script")
def run_sample_script():
    script_path = os.path.join("backend", "scripts", "sample_open_linkedin.py")
    if not os.path.exists(script_path):
        raise HTTPException(status_code=404, detail="Sample script not found.")

    try:
        startupinfo = None
        creationflags = 0
        if sys.platform.startswith("win"):
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            creationflags = subprocess.CREATE_NO_WINDOW

        result = subprocess.run(
            [PYTHON_EXECUTABLE, script_path],
            capture_output=True,
            text=True,
            startupinfo=startupinfo,
            creationflags=creationflags
        )

        return {
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "returncode": result.returncode
        }

    except Exception as e:
        return JSONResponse(content={"status": "Failed", "error": str(e)}, status_code=500)