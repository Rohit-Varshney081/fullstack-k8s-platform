from celery.result import AsyncResult
from fastapi import APIRouter

from app.tasks.report_tasks import (
    generate_report
)
from app.tasks.celery_app import (
    celery_app
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post("/report")
def report():

    task = generate_report.delay(
        "monthly-report"
    )

    return {
        "task_id": task.id
    }
    
@router.get("/{task_id}")
def task_status(task_id):

    task = AsyncResult(
        task_id,
        app=celery_app
    )

    return {
        "state": task.state,
        "result": str(task.result)
    }