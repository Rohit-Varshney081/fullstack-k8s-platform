from celery import Celery
from celery.schedules import crontab
from app.core.config import settings

celery_app = Celery(
    "worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True
)

celery_app.conf.beat_schedule = {

    "cleanup-logs-every-hour": {

        "task":
        "app.tasks.periodic_tasks.cleanup_old_logs",

        "schedule":
        crontab(minute=0)
    }
}

celery_app.autodiscover_tasks(
    [
        "app.tasks"
    ]
)

celery_app.conf.imports = (
    "app.tasks.report_tasks",
    "app.tasks.periodic_tasks",
    "app.tasks.email_tasks",
    "app.tasks.sample_task",
)