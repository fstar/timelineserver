from dataclasses import dataclass, field
from datetime import datetime
from dataclasses_json import dataclass_json
from typing import List, Optional

from app.utils.decorate import dataclasses_filter_none


@dataclass_json
@dataclass
class TimeLineRequestParam:
    start: Optional[str] = None  # 起始时间
    end: Optional[str] = None  # 结束时间
    key: Optional[str] = None  # 关键词


# ----------- timeline 控件数据结构 --------- #
@dataclass_json
@dataclass
@dataclasses_filter_none
class TimeLineSchema:

    @dataclass
    @dataclasses_filter_none
    class Slide:

        @dataclass
        @dataclasses_filter_none
        class Date:
            year: int
            month: Optional[int] = None
            day: Optional[int] = None
            hour: Optional[int] = None
            minute: Optional[int] = None
            second: Optional[int] = None
            millisecond: Optional[int] = None
            display_date: Optional[str] = None

            @classmethod
            def datetime_to_date(cls, date: datetime):
                return cls(year=date.year, month=date.month, day=date.day)

        @dataclass
        @dataclasses_filter_none
        class Text:
            headline: Optional[str] = None
            text: Optional[str] = None

        @dataclass
        @dataclasses_filter_none
        class Media:
            url: str
            caption: str = None
            credit: str = None
            thumbnail: str = None
            alt: str = None
            title: str = None
            link: str = None
            link_target: str = None

        start_date: Optional[Date] = None
        end_date: Optional[Date] = None
        text: Optional[Text] = None
        media: Optional[Media] = None
        group: Optional[str] = None
        display_date: Optional[str] = None
        background: Optional[str] = None
        autolink: Optional[str] = None
        unique_id: Optional[str] = None

    @dataclass
    @dataclasses_filter_none
    class Era:
        start_date: str
        end_date: str
        text: Optional[str] = None

    events: List[Slide] = field(default_factory=list)
    title: Slide = None
    eras: List[Era] = None
    scale: str = 'human'
