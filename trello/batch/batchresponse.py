# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import

from trello import TrelloBase
from trello.compat import force_str
from trello.member import Member


class BatchResponse:
    """
    Class representing a BatchError
    """
    def __init__(self, payload, success):
        super(BatchResponse, self).__init__()
        self.payload = payload
        self.success = success

    def __repr__(self):
        return force_str(u'<BatchResponse %s>' % self.success)
