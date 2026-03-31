
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agents import Supervisor

app = FastAPI()
supervisor = Supervisor()

# Allow frontend to connect (Vercel, localhost, or others)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/run")
async def run_campaign(data: dict):
    objective = data["objective"]
    result = supervisor.run_campaign(objective)
    return result

@app.get("/")
def home():
    return {"message": "Marketing AI Backend Running"}
