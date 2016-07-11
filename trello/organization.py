# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import
from trello.board import Board
from trello.compat import force_str
from trello.member import Member


class Organization(object):

    """
    Class representing an organization
    """
    def __init__(self, client, organization_id, name=''):
        self.client = client
        self.id = organization_id
        self.name = name

    @classmethod
    def from_json(cls, trello_client, json_obj):
        """
        Deserialize the board json object to a Organization object

        :trello_client: the trello client
        :json_obj: the board json object
        """
        organization = Organization(trello_client, json_obj['id'], name=json_obj['name'])
        organization.description = json_obj.get('desc', '')
        # cannot close an organization
        # organization.closed = json_obj['closed']
        organization.url = json_obj['url']
        return organization

    def __repr__(self):
        return force_str(u'<Organization %s>' % self.name)

    def fetch(self):
        """Fetch all attributes for this organization"""
        json_obj = self.client.fetch_json('/organizations/' + self.id)
        self.name = json_obj['name']
        self.description = json_obj.get('desc', '')
        self.closed = json_obj['closed']
        self.url = json_obj['url']

    def all_boards(self):
        """Returns all boards on this organization"""
        return self.get_boards('all')

    def get_boards(self, list_filter):
        '''Get boards using filter

        :rtype: Board
        '''
        # error checking
        json_obj = self.client.fetch_json(
            '/organizations/' + self.id + '/boards',
            query_params={'lists': 'none', 'filter': list_filter})
        return [Board.from_json(organization=self, json_obj=obj) for obj in json_obj]

    def get_board(self, field_name):
        '''Get board

        :rtype: Board
        '''
        # error checking
        json_obj = self.client.fetch_json(
            '/organizations/' + self.id + '/boards',
            query_params={'filter': 'open', 'fields': field_name})
        return [Board.from_json(organization=self, json_obj=obj) for obj in json_obj]

    def get_members(self):
        json_obj = self.client.fetch_json(
            '/organizations/' + self.id + '/members',
            query_params={'filter': 'all'})
        return [Member.from_json(trello_client=self.client, json_obj=obj) for obj in json_obj]
