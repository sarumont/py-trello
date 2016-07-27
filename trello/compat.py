import sys

PY2 = sys.version_info < (3, 0)


def force_str(s, encoding='utf-8'):
    """
    Converts `s` to the `str` type, regardless of the Python
    version. This is useful for __repr__ return types, where a `str`
    (bytes) is expected in Python 2 and a `str` (unicode string) is
    expected in Python 3.
    """
    if PY2 and isinstance(s, unicode):  # noqa
        s = s.encode(encoding)
    return s
