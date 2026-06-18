from app.db.mongodb import database


class AuditService:

    async def log_event(
        self,
        event_name,
        payload
    ):

        await database.audit_logs.insert_one(
            {
                "event": event_name,
                "payload": payload
            }
        )