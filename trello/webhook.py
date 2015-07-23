# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import


class WebHook(object):
    """Class representing a Trello webhook."""

    def __init__(self, client, token, hook_id=None, desc=None, id_model=None,
                 callback_url=None, active=False):
        self.id = hook_id
        self.desc = desc
        self.id_model = id_model
        self.callback_url = callback_url
        self.active = active
        self.client = client
        self.token = token

    def delete(self):
        """Removes this webhook from Trello"""
        self.client.fetch_json(
            '/webhooks/%s' % self.id,
            http_method='DELETE')
