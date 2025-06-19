from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from app.models import ExcuseRequest
from app.generator import generate_excuse
from app.apology import generate_apology
from app.storage import save_excuse, load_excuses
from app.proof import generate_proof
from app.emergency import generate_emergency_alert
from app.voice import text_to_speech
from app.scheduler import schedule_excuse, run_scheduled_job
from app.predictor import predict_next_absence
from app.ranker import rank_excuse

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

class EmergencyRequest(BaseModel):
    method: str
    description: str

app = FastAPI()

jobstores = {
    "default": SQLAlchemyJobStore(url="sqlite:///jobs.sqlite")
}
scheduler = BackgroundScheduler(jobstores=jobstores)
scheduler.start()

@app.post("/generate_excuse/")
def create_excuse(req: ExcuseRequest):
    if req.schedule_at:
        schedule_excuse(req, scheduler)
        return {"status": "Excuse scheduled", "scheduled_for": str(req.schedule_at)}

    excuse = generate_excuse(req.scenario, req.urgency, req.language)
    ranking = rank_excuse(excuse, req.urgency)
    save_excuse(req.scenario, ranking, req.urgency, excuse)
    proof_path = generate_proof(excuse, req.scenario)
    audio_path = text_to_speech(excuse, req.language)
    return {
        "excuse": excuse,
        "ranking_score": ranking,
        "proof_file": proof_path,
        "audio_file": audio_path
    }

@app.post("/generate_apology/")
def create_apology(req: ExcuseRequest):
    apology = generate_apology(req.scenario, req.urgency, req.language)
    return {"apology": apology}

@app.get("/history/")
def get_history():
    return load_excuses()

@app.post("/generate-emergency/")
def trigger_emergency(req: EmergencyRequest):
    result = generate_emergency_alert(req.description)
    return {
        "status": "success",
        "description": req.description,
        "text_alert": result["text_alert"],
        "voice_alert": result["voice_alert"],
        "message": result["message"]
    }

@app.get("/")
def read_root():
    return {"message": "Intelligent Excuse Generator API is running."}

@app.get("/favicon.ico")
def favicon():
    return {}

@app.on_event("startup")
def auto_predict_and_schedule():
    next_time = predict_next_absence()
    if next_time:
        print(f"🤖 Predicting user will miss something at {next_time}")
        fake_req = ExcuseRequest(
            scenario="Automatically predicted absence",
            urgency="moderate",
            language="en",
            schedule_at=next_time
        )
        scheduler.add_job(
            run_scheduled_job,
            trigger='date',
            run_date=next_time,
            args=[fake_req]
        )

@app.post("/rank_excuse/")
def get_rank(data: ExcuseRequest):
    excuse = generate_excuse(data.scenario, data.urgency, data.language)
    score = rank_excuse(excuse, data.urgency)
    return {
        "excuse": excuse,
        "ranking_score": score
    }
