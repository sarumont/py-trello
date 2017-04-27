# -*- coding: utf-8 -*-


class TrelloBase(object):
	def __init__(self):
		self.id = None

	def __hash__(self):
		class_name = type(self).__name__
		return hash(class_name) ^ hash(self.id)

	def __eq__(self, other):
		if isinstance(other, type(self)):
			return hash(self) == hash(other)
		raise NotImplementedError
