from httplib2 import Http
from urllib import urlencode
from models import AuthenticationError,AuthenticationRequired
import json

client = Http()
cookie = ""

def login(username, password):
	"""Log into Trello
	
	:username: Trello username or e-mail
	:password: Trello password
	"""
	body = {'user': username, 'password': password, 'returnUrl': '/'}
	headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
	response, content = client.request(
			'https://trello.com/authenticate',
			'POST',
			headers = headers,
			body = urllib.urlencode(body))

	if response and response['set-cookie']:
		# auth was successful
		cookie = response['set-cookie']
	else:
		raise AuthenticationError()

def list_boards():
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
	if not cookie:
		raise AuthenticationRequired()

	headers = {'Cookie': cookie, 'Accept': 'application/json'}
	response, content = client.request(
			'https://trello.com/data/me/boards',
			'GET',
			headers = headers,
			)

	# TODO: error checking

	json_obj = json.loads(content)
	return json_obj.boards
