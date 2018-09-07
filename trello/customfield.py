# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import

import time
import sys
from trello import TrelloBase
from trello.compat import force_str

is_python3 = sys.version_info.major == 3
if is_python3:
	unicode = str


class CustomFieldDefinition(TrelloBase):
	"""
	Class representing a Trello CustomFieldDefinition.
	"""
	def __init__(self, client, customFieldDefinition_id, name, field_type, list_options):
		super(CustomFieldDefinition, self).__init__()
		self.client = client
		self.id = customFieldDefinition_id
		self.name = name
		self.field_type = field_type
		self.list_options = list_options

	@classmethod
	def from_json(cls, board, json_obj):
		"""
		Deserialize the board's custom field json object to a CustomFieldDefinition object

		:param board: the parent board the custom field is on
		:param json_obj: the board's customField json object
		"""
		list_options = {}
		if json_obj['type'] == 'list':
			for option in json_obj['options']:
				list_options[option['id']] = option['value']['text']

		customFieldDefinition = CustomFieldDefinition(
			board.client,
			customFieldDefinition_id=json_obj['id'],
			name=json_obj['name'],
			field_type=json_obj['type'],
			list_options=list_options,
		)
		return customFieldDefinition

	@classmethod
	def from_json_list(cls, board, json_objs):
		return [cls.from_json(board, obj) for obj in json_objs]

	def __repr__(self):
		return force_str(u'<CustomFieldDefinition %s>' % (self.name,))


class CustomField(TrelloBase):
	"""
	Class representing a Trello CustomField.
	"""
	_type = ''

	def __init__(self, card, customField_id, customFieldDefinition_id, value):
		super(CustomField, self).__init__()
		self.client = card.client
		self.card = card
		self.id = customField_id
		self.definition_id = customFieldDefinition_id
		self._value = value

	@property
	def type(self):
		"""
		Returns the type of the custom field.
		:return: either 'list', 'checkbox', 'date', 'text' or 'number', str
		"""
		return self._type

	@property
	def name(self):
		"""
		Returns the user-readable name of the custom field by querying the
		custom field definitions.
		:return: the name of the custom field as str or None
		"""
		for definition in self.card.board.get_custom_field_definitions():
			if definition.id == self.definition_id:
				return definition.name
		return None

	@classmethod
	def from_json(cls, card, json_obj):
		"""
		Deserialize the custom field json object to a CustomField object

		:param card: the parent card the custom field is on
		:param json_obj: the customField json object
		"""
		raise Exception('Not Implemented')

	@classmethod
	def get_class(cls, board, json_obj):
		"""
		:param board: the board the custom field is used on
		:param json_obj: the customField json object
		:return: the python class that coresponds to the given custom field data
		"""
		definition_id = json_obj['idCustomField']
		for definition in board.get_custom_field_definitions():
			if definition.id == definition_id:
				return {
					'checkbox': CustomFieldCheckbox,
					'date': CustomFieldDate,
					'list': CustomFieldList,
					'number': CustomFieldNumber,
					'text': CustomFieldText,
				}[definition.field_type]
		return None

	@classmethod
	def from_json_list(cls, card, json_objs):
		return [cls.get_class(card.board, obj).from_json(card, obj) for obj in json_objs]

	def __repr__(self):
		return force_str(u'<CustomField%s %s=%r>' % (self.type.capitalize(), self.name, self.value))

	@property
	def value(self):
		raise Exception('Not Implemented')

	@value.setter
	def value(self, value):
		raise Exception('Not Implemented')


class CustomFieldText(CustomField):
	"""
	Class representing a Trello text custom field.
	"""
	_type = 'text'

	@classmethod
	def from_json(cls, card, json_obj):
		"""
		Deserialize the custom field json object to a CustomField object

		:card: the parent card the custom field is on
		:json_obj: the customField json object
		"""
		customField = cls(
			card,
			customField_id=json_obj['id'],
			customFieldDefinition_id=json_obj['idCustomField'],
			value=json_obj['value']['text'],
		)
		return customField

	@property
	def value(self):
		"""
		Returns the custom field value as unicode
		:return: the custom field value as unicode
		"""
		return self._value

	@value.setter
	def value(self, value):
		"""
		Sets the new value,
		:param value: the new value as unicode
		"""
		assert isinstance(value, unicode), "Given value is no unicode!"
		self.client.fetch_json(
			'/card/' + self.card.id + '/customField/' + self.definition_id + '/item',
			http_method='PUT',
			post_args={'value': { 'text': value, }, }, )
		self._value = value


class CustomFieldCheckbox(CustomField):
	_type = 'checkbox'

	@classmethod
	def from_json(cls, card, json_obj):
		"""
		Deserialize the custom field json object to a CustomField object

		:card: the parent board the custom field is on
		:json_obj: the customField json object
		"""
		customField = cls(
			card,
			customField_id=json_obj['id'],
			customFieldDefinition_id=json_obj['idCustomField'],
			value=(json_obj['value']['checked'] == u'true'),
		)
		return customField

	@property
	def value(self):
		"""
		Returns the custom field value as bool
		:return: the custom field value as bool
		"""
		return self._value

	@value.setter
	def value(self, value):
		"""
		Sets the new value,
		:param value: the new value as bool
		"""
		assert isinstance(value, bool), "Given value is no bool!"
		self.client.fetch_json(
			'/card/' + self.card.id + '/customField/' + self.definition_id + '/item',
			http_method='PUT',
			post_args={'value': { 'checked': u"true" if value else u"false", }, }, )
		self._value = value


class CustomFieldDate(CustomField):
	_type = 'date'

	@classmethod
	def from_json(cls, card, json_obj):
		"""
		Deserialize the custom field json object to a CustomField object

		:card: the parent card the custom field is on
		:json_obj: the customField json object
		"""
		customField = cls(
			card,
			customField_id=json_obj['id'],
			customFieldDefinition_id=json_obj['idCustomField'],
			value=json_obj['value']['date'],
		)
		return customField

	@property
	def value(self):
		"""
		Returns the custom field value as unicode in the format
		%Y-%m-%dT%H:%M:%S.000Z.
		:return: the custom field value as unicode
		"""
		return self._value

	@value.setter
	def value(self, value):
		"""
		Sets the new value,
		:param value: the new value as unicode in format %Y-%m-%dT%H:%M:%S.000Z
		"""
		assert isinstance(value, str) or isinstance(value, unicode), "Given value is no str or unicode!"
		time.strptime(value, '%Y-%m-%dT%H:%M:%S.000Z')
		self.client.fetch_json(
			'/card/' + self.card.id + '/customField/' + self.definition_id + '/item',
			http_method='PUT',
			post_args={'value': { 'date': value, }, }, )
		self._value = value


class CustomFieldList(CustomField):
	_type = 'list'

	@classmethod
	def from_json(cls, card, json_obj):
		"""
		Deserialize the custom field json object to a CustomField object

		:card: the parent card the custom field is on
		:json_obj: the customField json object
		"""
		customField = cls(
			card,
			customField_id=json_obj['id'],
			customFieldDefinition_id=json_obj['idCustomField'],
			value=json_obj['idValue'],
		)
		return customField

	def _id2str(self, _id):
		for definition in self.card.board.get_custom_field_definitions():
			if definition.id == self.definition_id:
				return definition.list_options.get(_id)
		raise Exception('Definition not found')

	def _str2id(self, text):
		for definition in self.card.board.get_custom_field_definitions():
			if definition.id == self.definition_id:
				for key, val in definition.list_options.items():
					if val == text:
						return key
				return None
		raise Exception('Definition not found')

	@property
	def value(self):
		"""
		Returns the custom field value as unicode.
		:return: the custom field value as unicode
		"""
		return self._id2str(self._value)

	@value.setter
	def value(self, value):
		"""
		Sets the new value, that must exist in custom field definition.
		:param value: the new value as unicode
		"""
		assert isinstance(value, str) or isinstance(value, unicode), "Given value is no str or unicode!"
		newvalue = self._str2id(value)
		assert newvalue is not None, "Unknown value has been specified!"
		self.client.fetch_json(
			'/card/' + self.card.id + '/customField/' + self.definition_id + '/item',
			http_method='PUT',
			post_args={'idValue': newvalue,}, )
		self._value = newvalue


class CustomFieldNumber(CustomField):
	_type = 'number'

	@classmethod
	def from_json(cls, card, json_obj):
		"""
		Deserialize the custom field json object to a CustomField object

		:card: the parent card the custom field is on
		:json_obj: the customField json object
		"""
		customField = cls(
			card,
			customField_id=json_obj['id'],
			customFieldDefinition_id=json_obj['idCustomField'],
			value=float(json_obj['value']['number']),
		)
		return customField

	@property
	def value(self):
		"""
		Returns the custom field value as unicode.
		:return: the custom field value as unicode
		"""
		return self._value

	@value.setter
	def value(self, value):
		"""
		Sets the new value,
		:param value: the new value as unicode
		"""
		assert isinstance(value, int) or isinstance(value, float), "Given value is no int or float!"
		self.client.fetch_json(
			'/card/' + self.card.id + '/customField/' + self.definition_id + '/item',
			http_method='PUT',
			post_args={'value': { 'number': str(value), }, }, )
		self._value = value
