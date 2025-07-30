import diskcache

cache = diskcache.Cache(".cache")

def get_from_cache(key: str):
    return cache.get(key, default=None)

def store_in_cache(key: str, value):
    cache.set(key, value)
