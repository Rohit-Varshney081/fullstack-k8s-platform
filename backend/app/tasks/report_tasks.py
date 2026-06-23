import time

from app.tasks.celery_app import celery_app


@celery_app.task
def generate_report(
    report_name
):

    time.sleep(10)

    return {
        "report": report_name,
        "status": "completed"
    }