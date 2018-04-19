# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import

from trello import TrelloBase
from trello.compat import force_str


class Member(TrelloBase):
    """
    Class representing a Trello member.
    """

    def __init__(self, client, member_id, full_name=''):
        super(Member, self).__init__()
        self.client = client
        self.id = member_id
        self.full_name = full_name

    def __repr__(self):
        return force_str(u'<Member %s>' % self.id)

    def fetch(self):
        """Fetch all attributes for this member"""
        json_obj = self.client.fetch_json(
            '/members/' + self.id,
            query_params={'badges': False})
        self.status = json_obj['status']
        self.id = json_obj.get('id', '')
        self.bio = json_obj.get('bio', '')
        self.url = json_obj.get('url', '')
        self.username = json_obj['username']
        self.full_name = json_obj['fullName']
        self.initials = json_obj['initials']
        return self

    def fetch_comments(self):
        if self.badges['comments'] > 0:
            comments = self.client.fetch_json(
                '/members/' + self.id + '/actions',
                query_params={'filter': 'commentCard'})
            return sorted(comments, key=lambda comment: comment['date'])
        return []

    def fetch_cards(self):
        """ Fetches all the cards for this member """
        cards = self.client.fetch_json(
            '/members/' + self.id + '/cards',
            query_params={'filter': 'visible'})
        return sorted(cards, key=lambda card: card['dateLastActivity'])

    def fetch_notifications(self, filters = []):
        """ Fetches all the notifications for this member """
        notifications = self.client.fetch_json(
            '/members/' + self.id + '/notifications',
            query_params={'filter': ",".join(filters)})
        return sorted(notifications, key=lambda notification: notification['date'])

    def get_boards(self, list_filter):
        """Get boards using filter

        :rtype: list of Board
        """
        from trello.board import Board
        from trello.organization import Organization
        json_obj = self.client.fetch_json(
            '/members/' + self.id + '/boards',
            query_params={'lists': 'none', 'filter': list_filter})
        organizations = {obj['idOrganization']: self.client.get_organization(obj['idOrganization']) for obj in json_obj if obj['idOrganization']}
        return [Board.from_json(trello_client=self.client, organization=organizations.get(obj['idOrganization']), json_obj=obj) for obj in json_obj]

    @classmethod
    def from_json(cls, trello_client, json_obj):
        """
        Deserialize the organization json object to a member object

        :trello_client: the trello client
        :json_obj: the member json object
        """

        member = Member(trello_client, json_obj['id'], full_name=json_obj['fullName'])
        member.username = json_obj.get('username', '')
        member.initials = json_obj.get('initials', '')
        # cannot close an organization
        # organization.closed = json_obj['closed']
        return member
