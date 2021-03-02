# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import

from trello import TrelloBase
# from trello.member import Member
# from trello.card import Card
from trello.compat import force_str
# from trello.trellolist import List
# from trello.label import Label
# from trello.checklist import Checklist
# from trello.customfield import CustomFieldDefinition
from dateutil import parser as dateparser


class PowerUp(TrelloBase):
	"""
	Class representing a Trello Power-Up.
	"""

	def __init__(self,client=None,board=None, power_up_id=None, name='',author=''):
		"""
		Valid values: calendar, cardAging, recap, voting
		:board_id: ID for the board
		"""
		super(PowerUp, self).__init__()
		if board is None:
			self.client = client
		else:
			self.client = board.client
		self.id = power_up_id
		self.board = board
		self.name = name
				

	@classmethod
	def from_json(cls, trello_client=None,power_up_id=None, board=None, json_obj=None):
		"""
		Deserialize the board json object to a Board object

		:trello_client: the trello client
		:json_obj: the powerup json object

		Alternative contrustraction:

		Deserialize the powerup json object to a powerup object
		:json_obj: the json powerup object
		"""
		if json_obj is None:
			power_up = PowerUp(client=trello_client)
		else:
			power_up = PowerUp(power_up_id=json_obj['id'], name=json_obj.get('name',''))
		
		power_up.id_plugin = json_obj.get('idPlugin','')
		power_up.author = json_obj.get('author','')
		power_up.description = json_obj.get('description', '')
		power_up.public = json_obj.get('public','')
		power_up.url = json_obj.get('url','')
		power_up.organization_owner_id = json_obj.get('idOrganizationOwner','')
		power_up.overview = json_obj.get('overview','')
		power_up.json = json_obj
		return power_up
	def __repr__(self):
		return force_str(u'<Power Up %s>' % self.name)
