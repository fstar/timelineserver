def dataclasses_filter_none(cls):
    """针对 dataclasses 的类, 生成 json 的时候过滤掉 None 的属性"""
    setattr(cls, '__filter_none', True)
    return cls
