# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import

from trello import TrelloBase
from trello.compat import force_str
from trello.member import Member


class BatchError:
    """
    Class representing a BatchError
    """
    def __init__(self, status_code, name, message):
        super(BatchError, self).__init__()
        self.status_code = status_code
        self.name = name
        self.message = message

    @classmethod
    def from_json(cls, json_obj):
        return BatchError(json_obj['statusCode'], json_obj['name'], json_obj['message'])

    def __repr__(self):
        return force_str(u'<BatchError %s>' % self.name)
