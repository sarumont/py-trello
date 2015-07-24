# -*- coding: utf-8 -*-


class ResourceUnavailable(Exception):
    """Exception representing a failed request to a resource"""

    def __init__(self, msg, http_response):
        Exception.__init__(self)
        self._msg = msg
        self._status = http_response.status_code

    def __str__(self):
        return "%s (HTTP status: %s)" % (self._msg, self._status)


class Unauthorized(ResourceUnavailable):
    pass


class TokenError(Exception):
    pass
