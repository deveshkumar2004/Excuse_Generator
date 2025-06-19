from app.generator import generate_excuse
from app.storage import save_excuse
from app.proof import generate_proof
from app.voice import text_to_speech
from datetime import datetime


def schedule_excuse(req, scheduler):
    scheduler.add_job(
        func=run_scheduled_job,
        trigger='date',
        run_date=req.schedule_at,
        args=[req]
    )


def run_scheduled_job(req):
    excuse = generate_excuse(req.scenario, req.urgency, req.language)
    save_excuse(req.scenario, req.urgency, excuse)
    generate_proof(excuse, req.scenario)
    text_to_speech(excuse, req.language)
    