from httplib2 import Http
from urllib import urlencode
from models import AuthenticationError,AuthenticationRequired
import json

class Trello:

	def __init__(self, username, password):
		self._client = Http()
		self._cookie = None
		self._username = username
		self._password = password
		self.login()

	def login(self):
		"""Log into Trello"""
		body = {
				'user': self._username,
				'password': self._password,
				'returnUrl': '/'}
		headers = {
				'Content-type': 'application/x-www-form-urlencoded',
				'Accept': 'application/json'}
		response, content = self._client.request(
				'https://trello.com/authenticate',
				'POST',
				headers = headers,
				body = urlencode(body))

		if response and response['set-cookie']:
			# auth was successful
			self._cookie = response['set-cookie']
		else:
			raise AuthenticationError()

	def logout(self):
		"""Log out of Trello. This method is idempotent."""
		if not self._cookie:
			return

		headers = {'Cookie': self._cookie, 'Accept': 'application/json'}
		response, content = self._client.request(
				'https://trello.com/logout',
				'GET',
				headers = headers,
				)

		# TODO: error checking
		self._cookie = None

	def list_boards(self):
		"""
		Returns all boards for your Trello user

		:return: a list of Python objects representing the Trello boards. Each board has the 
		following noteworthy attributes:
			- _id: the board's identifier
			- name: Name of the board
			- closed: Boolean representing whether this board is closed or not
		Other attributes include: 
			invitations, memberships, idMembersWatching, prefs, 
			nActionsSinceLastView, idOrganization

		@todo: the JSON response contains the values needed to dereference idFoo; be nice and expose 
		these, too
		"""
		if not self._cookie:
			raise AuthenticationRequired()

		headers = {'Cookie': self._cookie, 'Accept': 'application/json'}
		response, content = self._client.request(
				'https://trello.com/data/me/boards',
				'GET',
				headers = headers,
				)

		# TODO: error checking

		json_obj = json.loads(content)
		return json_obj['boards']

	def add_card(self, board_id, name):
		"""Adds a card to the first list in the given board

		:board_id: @todo
		:name: @todo
		:returns: @todo
		"""

		if not self._cookie:
			raise AuthenticationRequired()

		headers = {'Cookie': self._cookie, 'Accept': 'application/json'}
		response, content = self._client.request(
				'https://trello.com/data/board/'+board_id+'/current',
				'GET',
				headers = headers,
				)

		# TODO: error checking

		json_obj = json.loads(content)

		# get first list
		list_id = ""
		for board in json_obj.boards:
			if board.lists:
				list_id = board.lists[0]._id

		# TODO: ensure list was found
		request = {
				'token': self._cookie, #TODO: not right - extract token
				'method': 'create',
				'data': {
					'attrs': {
						'name': name,
						'pos': 65536,
						'closed': false,
						'idBoard': board_id,
						"idList": list_id,
						},
					'idParents': [ board_id, list_id ],
					}
				}

		response, content = self._client.request(
				'https://trello.com/api/card',
				'POST',
				headers = headers,
				body = json.dumps(request),
				)

		# TODO: error checking
