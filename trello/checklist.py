# -*- coding: utf-8 -*-


class Checklist(object):
    """
    Class representing a Trello checklist.
    """

    def __init__(self, client, checked, obj, trello_card=None):
        self.client = client
        self.trello_card = trello_card
        self.id = obj['id']
        self.name = obj['name']
        self.items = obj['checkItems']
        for i in self.items:
            i['checked'] = False
            for cis in checked:
                if cis['idCheckItem'] == i['id'] and cis['state'] == 'complete':
                    i['checked'] = True

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

    def set_checklist_item(self, name, checked):
        """Set the state of an item on this checklist

        :name: name of the checklist item
        :checked: True if item state should be checked, False otherwise
        """

        # Locate the id of the checklist item
        try:
            [ix] = [i for i in range(len(self.items)) if
                    self.items[i]['name'] == name]
        except ValueError:
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

        # Locate the id of the checklist item
        try:
            [ix] = [i for i in range(len(self.items)) if self.items[i]['name'] == name]
        except ValueError:
            return

        json_obj = self.client.fetch_json(
                '/cards/'+self.trello_card +
                '/checklist/'+self.id +
                '/checkItem/'+self.items[ix]['id'],
                http_method='PUT',
                post_args={'name': new_name})

        self.items[ix] = json_obj
        return json_obj

    def delete(self):
        """Removes this checklist"""
        self.client.fetch_json(
            '/checklists/%s' % self.id,
            http_method='DELETE')

    def __repr__(self):
        return '<Checklist %s>' % self.id
