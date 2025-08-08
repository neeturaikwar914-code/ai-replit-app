from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS so frontend can access this
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Replit App is live!"}

@app.post("/run")
def run_code(data: dict):
    code = data.get("code", "")
    try:
        exec_globals = {}
        exec(code, exec_globals)
        return {"output": "Code executed successfully!"}
    except Exception as e:
        return {"output": str(e)}
