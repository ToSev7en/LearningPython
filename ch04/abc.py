"""
class CacheBase:

    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError
"""

import abc

class CacheBase(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass

class RedisCache(CacheBase):
    pass


redis_cache = RedisCache()

# redis_cache.set('title','Hello World!')