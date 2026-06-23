from app.tasks.celery_app import celery_app


@celery_app.task
def cleanup_old_logs():

    print(
        "Cleaning old logs..."
    )

    return True