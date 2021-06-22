# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import

from trello import TrelloBase
from trello.compat import force_str


class Checklist(TrelloBase):
    """
    Class representing a Trello checklist.
    """

    def __init__(self, client, obj, trello_card=None):
        """
        :client: Trello client object
        :obj: List of checklists on the card, sorted by position
        :trello_card: ID of the Trello card
        """
        super(Checklist, self).__init__()
        self.client = client
        self.trello_card = trello_card
        self.id = obj['id']
        self.name = obj['name']
        self.items = sorted(obj['checkItems'], key=lambda items: items.get('pos'))
        for i in self.items:
            i['checked'] = i['state'] == "complete"

    def add_checklist_item(self, name, checked=False):
        """Add a checklist item to this checklist

        :name: name of the checklist item
        :checked: True if item state should be checked, False otherwise
        :return: the checklist item json object
        """
        json_obj = self.client.fetch_json(
            '/checklists/' + self.id + '/checkItems',
            http_method='POST',
            post_args={'name': name, 'checked': checked}, )
        json_obj['checked'] = checked
        self.items.append(json_obj)
        return json_obj

    def delete_checklist_item(self, item_or_name):
        """Delete an item on this checklist

        :item_or_name: name or item object of the checklist item to delete 
        """
        ix = self._get_item_index(item_or_name)
        if ix is None:
            return

        self.client.fetch_json(
            '/checklists/'+ self.id +
            '/checkItems/'+ self.items[ix]['id'],
            http_method='DELETE')
        del self.items[ix]

    def clear(self):
        """Clear checklist by removing all checklist items"""
        # copy item list to prevent modifying while iterating, which would break
        # for-loops behaviour
        old_items = items[:] 
        for item in old_items:
            self.delete_checklist_item(item)


    def set_checklist_item(self, name, checked):
        """Set the state of an item on this checklist

        :name: name of the checklist item
        :checked: True if item state should be checked, False otherwise
        """
        ix = self._get_item_index(name)
        if ix is None:
            return

        json_obj = self.client.fetch_json(
            '/cards/' + self.trello_card +
            '/checklist/' + self.id +
            '/checkItem/' + self.items[ix]['id'],
            http_method='PUT',
            post_args={'state': 'complete' if checked else 'incomplete'})

        json_obj['checked'] = checked
        self.items[ix] = json_obj
        return json_obj
    def set_checklist_item_due(self,checklist_item, due):
        """Set the state of an item on this checklist
        :checklist_item: the checklist item object
        :due: due date in isoformat
        """
        
        datestr = due.isoformat()
        json_obj = self.client.fetch_json(
            '/cards/' + self.trello_card +
            '/checklist/' + self.id +
            '/checkItem/' + checklist_item['id'],
            http_method='PUT',
            post_args={'due': datestr})

        ix = self._get_item_index(checklist_item['name'])
        if ix is None:
            return
        self.items[ix] = json_obj
        return json_obj
    def set_checklist_item_member(self,checklist_item, member):
        """Set the state of an item on this checklist
        :checklist_item: the checklist item object
        :member: the member to assign
        """
        json_obj = self.client.fetch_json(
            '/cards/' + self.trello_card +
            '/checklist/' + self.id +
            '/checkItem/' + checklist_item['id'],
            http_method='PUT',
            post_args={'idMember': member.id})

        ix = self._get_item_index(checklist_item['name'])
        if ix is None:
            return
        self.items[ix] = json_obj
        return json_obj
    def _set_remote_attribute(self,name, attribute, value):
        ix = self._get_item_index(name)
        if ix is None:
            return
        self.client.fetch_json(
            '/cards/' + self.trello_card +
            '/checklist/' + self.id +
            '/checkItem/' + self.items[ix]['id'] + attribute,
            http_method='PUT',
            post_args={'due': value}, )
    def rename(self, new_name):
        """Rename this checklist

        :new_name: new name of the checklist
        """

        json_obj = self.client.fetch_json(
            '/checklists/' + self.id + '/name/',
            http_method='PUT',
            post_args={'value': new_name})

        self.name = json_obj['name']

        return json_obj

    def rename_checklist_item(self, name, new_name):
        """Rename the item on this checklist

        :name: name of the checklist item
        :new_name: new name of item
        """
        ix = self._get_item_index(name)
        if ix is None:
            return

        json_obj = self.client.fetch_json(
                '/cards/' + self.trello_card +
                '/checklist/' + self.id +
                '/checkItem/' + self.items[ix]['id'],
                http_method='PUT',
                post_args={'name': new_name})

        self.items[ix] = json_obj
        return json_obj

    def delete(self):
        """Removes this checklist"""
        self.client.fetch_json(
            '/checklists/%s' % self.id,
            http_method='DELETE')

    def _get_item_index(self, item_or_name):
        """Locate the index of the checklist item"""
        try:
            ix = [i for i, item in enumerate(self.items) if
                    item['name'] == item_or_name or item == item_or_name][0]
            return ix
        except ValueError:
            return None

    def __repr__(self):
        return force_str(u'<Checklist %s>' % self.id)
