from app.schemas.timeline import TimeLineSchema
from app.repository.timeline import TimeLineRepository


class TimeLineService:

    def __init__(self) -> None:
        self.timeline_repository = TimeLineRepository()

    def get_all(self) -> TimeLineSchema:
        events = self.timeline_repository.get_all()
        timeline_schema = TimeLineSchema(events=events)

        return timeline_schema
