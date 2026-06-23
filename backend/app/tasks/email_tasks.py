from app.tasks.celery_app import celery_app


@celery_app.task(
    queue="email_queue",
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    max_retries=5
)
def send_email(
    self,
    email,
    subject
):

    print(
        f"Sending email to {email}"
    )

    return True