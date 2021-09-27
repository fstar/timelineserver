from datetime import datetime, timedelta
from typing import List

from sqlalchemy import or_

from app.repository.base import DataBaseRepository
from app.models.timeline import SlideModel, SlideMediaModel
from app.schemas.timeline import TimeLineSchema


class TimeLineRepository(DataBaseRepository):

    def add(self, timeline: SlideModel, timeline_media: SlideMediaModel = None):
        """新增一条 timeline, 如果有 timeline_media 则新增一条 timeline_media"""
        self.session.add(timeline)
        if timeline_media is not None:
            timeline_media.time_line_id = timeline.id
            self.session.add(timeline_media)
        self.session.commit()

    def get_all(self):
        """获取 所有的 timeline"""
        query = self.session.query(SlideModel,
                                   SlideMediaModel).outerjoin(SlideMediaModel,
                                                              SlideModel.id == SlideMediaModel.slide_id).all()
        return [self.__model_to_schema(i.SlideModel, i.SlideMediaModel) for i in query]

    def get(self, timeline_id: str):
        """根据 id 获取 timeline"""
        query = self.session.query(SlideModel, SlideMediaModel).outerjoin(
            SlideMediaModel, SlideModel.id == SlideMediaModel.slide_id).filter(SlideModel.id == timeline_id).first()
        return self.__model_to_schema(query.SlideModel, query.SlideMediaModel)

    def delete(self, timeline_ids: List[str]):
        """根据 timeline_id 删除 timeline 和 timeline_media 条目"""
        self.session.query(SlideModel).filter(SlideModel.id.in_(timeline_ids)).delete()
        self.session.query(SlideMediaModel).filter(SlideMediaModel.time_line_id.in_(timeline_ids)).delete()

    def search(self, key=None, start_time=None, end_time=None):
        """根据 key 和 起止时间 查询 timeline list"""
        if end_time is None:
            end_time = datetime.now()
        if start_time is None:
            start_time = end_time - timedelta(years=1)
        query = self.session.query(SlideModel, SlideMediaModel).outerjoin(
            SlideMediaModel, SlideModel.id == SlideMediaModel.time_line_id).filter(
                SlideModel.start_date >= start_time).filter(SlideModel.end_date <= end_time)
        if key is not None:
            filter_or = or_(SlideModel.headline.like(f'%{key}%'), SlideModel.text.like(f'%{key}%'),
                            SlideModel.tags.like(f'%{key}%'), SlideModel.group.like(f'%{key}%'))
            query = query.filter(filter_or)
        query = query.all()
        return [self.__model_to_schema(i.SlideModel, i.SlideMediaModel) for i in query]

    def __model_to_schema(self, slide: SlideModel, slide_media: SlideMediaModel = None) -> TimeLineSchema.Slide:
        """model 对象转 schemas"""
        if slide_media is not None:
            media_schema = TimeLineSchema.Slide.Media(
                url=slide_media.url,
                caption=slide_media.caption,
                thumbnail=slide_media.thumbnail,
                link=slide_media.thumbnail,
            )
        else:
            media_schema = None

        slide_schema = TimeLineSchema.Slide(
            start_date=TimeLineSchema.Slide.Date.datetime_to_date(slide.start_date),
            end_date=TimeLineSchema.Slide.Date.datetime_to_date(slide.end_date),
            text=TimeLineSchema.Slide.Text(headline=slide.headline, text=slide.text),
            media=media_schema,
            group=slide.group,
            display_date=slide.display_date,
            unique_id=str(slide.id),
        )
        return slide_schema
