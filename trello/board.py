# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import

from trello.base import TrelloBase
from trello.member import Member
from trello.card import Card
from trello.compat import force_str
from trello.trellolist import List
from trello.label import Label
from trello.checklist import Checklist
from trello.customfield import CustomFieldDefinition
from dateutil import parser as dateparser


class Board(TrelloBase):
	"""
	Class representing a Trello board. Board attributes are stored as normal
	Python attributes; access to all sub-objects, however, is always
	an API call (Lists, Cards).
	"""

	def __init__(self, client=None, board_id=None, organization=None, name=''):
		"""
		:trello: Reference to a Trello object
		:board_id: ID for the board

		Alternative Constructor

		:organization: reference to the parent organization
		:board_id: ID for this board

		"""
		super(Board, self).__init__()
		if organization is None:
			self.client = client
		else:
			self.organization = organization
			self.client = organization.client
		self.id = board_id
		self.name = name
		self.date_last_activity = self.get_last_activity()
		self.customFieldDefinitions = None

	@classmethod
	def from_json(cls, trello_client=None, organization=None, json_obj=None):
		"""
		Deserialize the board json object to a Board object

		:trello_client: the trello client
		:json_obj: the board json object

		Alternative contrustraction:

		Deserialize the board json object to a board object

		:organization: the organization object that the board belongs to
		:json_obj: the json board object
		"""
		if organization is None:
			board = Board(client=trello_client, board_id=json_obj['id'], name=json_obj['name'])
		else:
			board = Board(organization=organization, board_id=json_obj['id'], name=json_obj['name'])

		board.description = json_obj.get('desc', '')
		board.closed = json_obj['closed']
		board.url = json_obj['url']

		return board

	def __repr__(self):
		return force_str(u'<Board %s>' % self.name)

	def fetch(self):
		"""Fetch all attributes for this board"""
		json_obj = self.client.fetch_json('/boards/' + self.id)
		self.name = json_obj['name']
		self.description = json_obj.get('desc', '')
		self.closed = json_obj['closed']
		self.url = json_obj['url']
		self.customFieldDefinitions = None

	# Saves a Trello Board
	def save(self):
		json_obj = self.client.fetch_json(
				'/boards/',
				http_method='POST',
				post_args={'name': self.name, "desc": self.description, "defaultLists": False}, )
		# Set initial data from Trello
		self.from_json(json_obj=json_obj)
		self.id = json_obj["id"]

	def set_name(self, name):
		self.client.fetch_json(
				'/boards/{board_id}/name'.format(board_id=self.id),
				http_method='PUT',
				post_args={'value': name})
		self.name = name

	def set_description(self, desc):
		self.client.fetch_json(
				'/boards/{board_id}/desc'.format(board_id=self.id),
				http_method='PUT',
				post_args={'value': desc})
		self.description = desc

	def set_organization(self, desc):
		self.client.fetch_json(
				'/boards/{board_id}/idOrganization'.format(board_id=self.id),
				http_method='PUT',
				post_args={'value': desc})
		self.description = desc

	def close(self):
		self.client.fetch_json(
				'/boards/' + self.id + '/closed',
				http_method='PUT',
				post_args={'value': 'true', }, )
		self.closed = True

	def open(self):
		self.client.fetch_json(
				'/boards/' + self.id + '/closed',
				http_method='PUT',
				post_args={'value': 'false', }, )
		self.closed = False

	def get_list(self, list_id):
		"""Get list

		:rtype: List
		"""
		obj = self.client.fetch_json('/lists/' + list_id)
		return List.from_json(board=self, json_obj=obj)

	def all_lists(self):
		"""Returns all lists on this board

		:rtype: list of List
		"""
		return self.get_lists('all')

	def open_lists(self):
		"""Returns all open lists on this board

		:rtype: list of List
		"""
		return self.get_lists('open')

	def closed_lists(self):
		"""Returns all closed lists on this board

		:rtype: list of List
		"""
		return self.get_lists('closed')

	def get_lists(self, list_filter):
		"""Get lists from filter

		:rtype: list of List
		"""
		# error checking
		json_obj = self.client.fetch_json(
				'/boards/' + self.id + '/lists',
				query_params={'cards': 'none', 'filter': list_filter})
		return [List.from_json(board=self, json_obj=obj) for obj in json_obj]

	def list_lists(self, list_filter='all'):
		"""Get lists from filter

		:rtype: list of List
		"""
		return self.get_lists(list_filter=list_filter)

	def get_custom_field_definitions(self):
		"""Get all custom field definitions for this board

		:rtype: list of CustomFieldDefinition
		"""
		if self.customFieldDefinitions is None:
			json_obj = self.client.fetch_json('/boards/' + self.id + '/customFields')
			self.customFieldDefinitions = CustomFieldDefinition.from_json_list(self, json_obj)
		return self.customFieldDefinitions

	def get_labels(self, fields='all', limit=50):
		"""Get label

		:rtype: list of Label
		"""
		json_obj = self.client.fetch_json(
				'/boards/' + self.id + '/labels',
				query_params={'fields': fields, 'limit': limit})
		return Label.from_json_list(self, json_obj)

	def get_checklists(self, cards='all'):
		"""Get checklists

		:rtype: list of Checklist
		"""
		checklists = []
		json_obj = self.client.fetch_json(
				'/boards/' + self.id + '/checklists',
				query_params={'cards': cards})
		json_obj = sorted(json_obj, key=lambda checklist: checklist['pos'])
		for cl in json_obj:
			checklists.append(Checklist(self.client, cl.get('checkItemStates', []), cl,
					trello_card=cl.get('idCard')))
		return checklists

	def add_list(self, name, pos=None):
		"""Add a list to this board

		:name: name for the list
		:pos: position of the list: "bottom", "top" or a positive number
		:return: the list
		:rtype: List
		"""
		arguments = {'name': name, 'idBoard': self.id}
		if pos:
			arguments["pos"] = pos
		obj = self.client.fetch_json(
				'/lists',
				http_method='POST',
				post_args=arguments, )
		return List.from_json(board=self, json_obj=obj)

	def add_label(self, name, color):
		"""Add a label to this board

		:name: name of the label
		:color: the color, either green, yellow, orange
			red, purple, blue, sky, lime, pink, or black
		:return: the label
		:rtype: Label
		"""
		obj = self.client.fetch_json(
				'/labels',
				http_method='POST',
				post_args={'name': name, 'idBoard': self.id, 'color': color}, )
		return Label.from_json(board=self, json_obj=obj)

	def delete_label(self, label_id):
		"""Delete a label from this board

		:label_id: the ID of the label to delete.
		:return: the label
		:rtype: json
		"""
		json_obj = self.client.fetch_json(
			    '/labels/{0}'.format(label_id),
			    http_method='DELETE',
		    	post_args={'id': label_id}, )
		return json_obj

	def all_cards(self):
		"""Returns all cards on this board

		:rtype: list of Card
		"""
		filters = {
			'filter': 'all',
			'fields': 'all'
		}
		return self.get_cards(filters)

	def open_cards(self):
		"""Returns all open cards on this board

		:rtype: list of Card
		"""
		filters = {
			'filter': 'open',
			'fields': 'all'
		}
		return self.get_cards(filters)

	def closed_cards(self):
		"""Returns all closed cards on this board

		:rtype: list of Card
		"""
		filters = {
			'filter': 'closed',
			'fields': 'all'
		}
		return self.get_cards(filters)

	def get_cards(self, filters=None, card_filter=""):
		"""
		:filters: dict containing query parameters. Eg. {'fields': 'all'}
		:card_filter: filters on card status ('open', 'closed', 'all')

		More info on card queries:
		https://trello.com/docs/api/board/index.html#get-1-boards-board-id-cards

		:rtype: list of Card
		"""
		json_obj = self.client.fetch_json(
				'/boards/' + self.id + '/cards/' + card_filter,
				query_params=filters
		)

		return list([Card.from_json(self, json) for json in json_obj])

	def all_members(self):
		"""Returns all members on this board

		:rtype: list of Member
		"""
		filters = {
			'filter': 'all',
			'fields': 'all'
		}
		return self.get_members(filters)

	def normal_members(self):
		"""Returns all normal members on this board

		:rtype: list of Member
		"""
		filters = {
			'filter': 'normal',
			'fields': 'all'
		}
		return self.get_members(filters)

	def admin_members(self):
		"""Returns all admin members on this board

		:rtype: list of Member
		"""
		filters = {
			'filter': 'admins',
			'fields': 'all'
		}
		return self.get_members(filters)

	def owner_members(self):
		"""Returns all owner members on this board

		:rtype: list of Member
		"""
		filters = {
			'filter': 'owners',
			'fields': 'all'
		}
		return self.get_members(filters)

	def get_members(self, filters=None):
		"""Get members with filter

		:filters: dict containing query parameters.
			Eg. {'fields': 'all', 'filter': 'admins'}

		More info on possible filters:
		https://developers.trello.com/advanced-reference/board#get-1-boards-board-id-members

		:rtype: list of Member
		"""
		json_obj = self.client.fetch_json(
				'/boards/' + self.id + '/members',
				query_params=filters)
		members = list()
		for obj in json_obj:
			m = Member(self.client, obj['id'])
			m.status = obj.get('status', '')
			m.id = obj.get('id', '')
			m.bio = obj.get('bio', '')
			m.url = obj.get('url', '')
			m.username = obj['username']
			m.full_name = obj['fullName']
			m.initials = obj.get('initials', '')
			m.member_type = obj.get('memberType', '')
			members.append(m)

		return members

	# Add a member to a board
	def add_member(self, member, member_type="normal"):
		json_obj = self.client.fetch_json(
				'/boards/{0}/members/{1}'.format(self.id, member.id),
				http_method='PUT',
				post_args={'idMember': member.id, "type": member_type},
		)
		return json_obj

	# Removes an existing member of a board
	def remove_member(self, member):
		json_obj = self.client.fetch_json(
				'/boards/{0}/members/{1}'.format(self.id, member.id),
				http_method='DELETE',
				post_args={'idMember': member.id},
		)
		return json_obj

	def fetch_actions(self, action_filter, action_limit=50, before=None, since=None):
		"""Returns all actions that conform to the given filters.

		:action_filter: str of possible actions separated by comma
			ie. 'createCard,updateCard'
		:action_limit: int of max items returned
		:before: datetime obj
		:since: datetime obj

		More info on action filter values:
		https://developers.trello.com/advanced-reference/board#get-1-boards-board-id-actions

		:rtype: json list of past actions
		"""
		query_params = {'filter': action_filter, 'limit': action_limit}

		if since:
			query_params["since"] = since

		if before:
			query_params["before"] = before

		json_obj = self.client.fetch_json('/boards/' + self.id + '/actions',
				query_params=query_params)

		self.actions = json_obj
		return self.actions

	def get_last_activity(self):
		"""Return the date of the last action done on the board.

		:rtype: datetime.datetime
		"""
		json_obj = self.client.fetch_json(
                '/boards/{0}/dateLastActivity'.format(self.id))
		if json_obj['_value']:
			return dateparser.parse(json_obj['_value'])
