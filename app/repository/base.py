from app.database import db_session


class DataBaseRepository:

    def __init__(self) -> None:
        self.session = db_session()
