import dataclasses
from datetime import timedelta, datetime, date
from decimal import Decimal
from enum import Enum, Flag

from flask.json import JSONEncoder
import numpy as np


class PltJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, (timedelta, datetime, date)):
                return str(obj)
            if isinstance(obj, Decimal):
                return float(obj)
            if isinstance(obj, Enum):
                return obj.value
            if isinstance(obj, Flag):
                return obj.value
            if dataclasses.is_dataclass(obj):
                return self._asdict(obj)
            if hasattr(obj, 'to_dict') and callable(obj.to_dict):
                return obj.to_dict()
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            iterable = iter(obj)
        except TypeError as _:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)

    def _asdict(self, obj, *, dict_factory=dict):
        if not dataclasses._is_dataclass_instance(obj):  # pylint: disable=W0212
            raise TypeError('asdict() should be called on dataclass instances')
        return self._asdict_inner(obj, dict_factory)

    def _asdict_inner(self, obj, dict_factory):
        if dataclasses._is_dataclass_instance(obj):  # pylint: disable=W0212
            result = []
            for f in dataclasses.fields(obj):
                value = self._asdict_inner(getattr(obj, f.name), dict_factory)
                if getattr(obj, '__filter_none', False) and value is None:
                    continue
                result.append((f.name, value))
            return dict_factory(result)
        elif isinstance(obj, tuple) and hasattr(obj, '_fields'):
            result = {}
            for index, key in enumerate(obj._fields):
                result[key] = self._asdict_inner(obj[index], dict_factory)
            return result
        elif isinstance(obj, (list, tuple)):
            return type(obj)(self._asdict_inner(v, dict_factory) for v in obj)
        elif isinstance(obj, dict):
            return type(obj)(
                (self._asdict_inner(k, dict_factory), self._asdict_inner(v, dict_factory)) for k, v in obj.items())
        elif hasattr(obj, 'to_dict') and callable(obj.to_dict):
            return obj.to_dict()
        else:
            return obj
