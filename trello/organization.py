# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import

from trello import TrelloBase
from trello.compat import force_str
from trello.member import Member


class Organization(TrelloBase):

    TIMEZONE = 'UTC'

    """
    Class representing an organization
    """
    def __init__(self, client, organization_id, name=''):
        super(Organization, self).__init__()
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
        organization.url = json_obj['url']
        return organization

    def __repr__(self):
        return force_str(u'<Organization %s>' % self.name)

    def fetch(self):
        """Fetch all attributes for this organization"""
        json_obj = self.client.fetch_json('/organizations/' + self.id)
        self.name = json_obj['name']
        self.description = json_obj.get('desc', '')
        self.url = json_obj['url']

    def all_boards(self):
        """Returns all boards on this organization"""
        return self.get_boards('all')

    def get_boards(self, list_filter):
        """Get boards using filter

        :rtype: list of Board
        """
        from trello.board import Board
        json_obj = self.client.fetch_json(
            '/organizations/' + self.id + '/boards',
            query_params={'lists': 'none', 'filter': list_filter})
        return [Board.from_json(organization=self, json_obj=obj) for obj in json_obj]

    def get_board(self, field_name):
        """Get board

        :rtype: list of Board
        """
        from trello.board import Board
        json_obj = self.client.fetch_json(
            '/organizations/' + self.id + '/boards',
            query_params={'filter': 'open', 'fields': field_name})
        return [Board.from_json(organization=self, json_obj=obj) for obj in json_obj]

    def get_members(self):
        json_obj = self.client.fetch_json(
            '/organizations/' + self.id + '/members',
            query_params={'filter': 'all',
                          'fields': 'id,fullName,username,initials'})
        return [Member.from_json(trello_client=self.client, json_obj=obj) for obj in json_obj]

    def add_member(self, member, member_type="normal"):
        json_obj = self.client.fetch_json(
                '/organizations/{0}/members/{1}'.format(self.id, member.id),
                http_method='PUT',
                post_args={'idMember': member.id, "type": member_type},
        )
        return json_obj

    def remove_member(self, member):
        json_obj = self.client.fetch_json(
                '/organizations/{0}/members/{1}'.format(self.id, member.id),
                http_method='DELETE',
                post_args={'idMember': member.id},
        )
        return json_obj
