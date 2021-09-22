from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List, Optional


@dataclass_json
@dataclass
class TimeLineRequestParam:
    start: Optional[str] = None  # 起始时间
    end: Optional[str] = None  # 结束时间
    key: Optional[str] = None  # 关键词


# ----------- timeline 控件数据结构 --------- #
@dataclass_json
@dataclass
class TimeLineJson:

    @dataclass
    class Slide:

        @dataclass
        class Date:
            year: int
            month: int = None
            day: int = None
            hour: int = None
            minute: int = None
            second: int = None
            millisecond: int = None
            display_date: str = None

        @dataclass
        class Text:
            headline: str = None
            text: str = None

        @dataclass
        class Media:
            url: str
            caption: str
            credit: str
            thumbnail: str
            alt: str
            title: str
            link: str
            link_target: str

        start_date: Date = None
        end_date: Date = None
        text: Text = None
        media: Media = None
        group: str = None
        display_date: str = None
        background: str = None
        autolink: str = None
        unique_id: str = None

    @dataclass
    class Era:
        start_date: str
        end_date: str
        text: str = None

    events: List[Slide] = field(default_factory=list)
    title: Slide = None
    eras: Era = None
    scale: str = 'human'
