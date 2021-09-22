import uuid
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy_utils.types import UUIDType
from flask_appbuilder import Model


class TimeLine(Model):
    __tablename__ = 'time_line'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4, index=True)
    year = Column(Integer, index=True)  # 年
    month = Column(Integer, index=True)  # 月
    day = Column(Integer, index=True)  # 日
    person = Column(String(500), index=True)  # 人
    content = Column(Text)  # 事件
    location = Column(String(500))  # 地点
    tags = Column(String(500), index=True)  # 标签
