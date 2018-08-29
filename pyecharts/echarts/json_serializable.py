from pyecharts.utils import remove_key_with_none_value


class JsonSerializable(object):
    # TODO Serializable/Encoder
    # TODO Use __pye_json__
    
    def __init__(self):
        self._config = {}

    def __setitem__(self, key, value):
        self._config[key] = value

    def __getitem__(self, key):
        return self._config.get(key)

    def update(self, **kwargs):
        self._config.update(**kwargs)

    @property
    def config(self):
        return remove_key_with_none_value(self._config)
