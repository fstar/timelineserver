import uuid
from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy_utils.types import UUIDType
from flask_appbuilder import Model


class SlideModel(Model):
    __tablename__ = 'slide'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4, index=True)
    start_date = Column(DateTime, index=True)  # 开始时间
    end_date = Column(DateTime, index=True)  # 结束时间
    headline = Column(Text)  # 标题
    text = Column(Text)  # 内容
    group = Column(String(500))  # 分组
    display_date = Column(Text)  # 标题
    tags = Column(String(500), index=True)  # 标签


class SlideMediaModel(Model):
    __tablename__ = 'slide_media'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4, index=True)
    slide_id = Column(String(16))  # TimeLine id
    url = Column(String(500))  # 展示图片
    caption = Column(Text)  # 说明
    thumbnail = Column(String(500))  # 缩略图
    link = Column(String(500))  # 跳转连接


class EraModel(Model):
    __tablename__ = 'era'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4, index=True)
    slide_id = Column(String(16))  # TimeLine id
    start_date = Column(DateTime, index=True)  # 开始时间
    end_date = Column(DateTime, index=True)  # 结束时间
    text = Column(Text)  # 内容
