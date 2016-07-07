# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import
from dateutil import parser as dateparser
from datetime import datetime
from trello.checklist import Checklist
from trello.label import Label

import datetime


class Card(object):
    """
    Class representing a Trello card. Card attributes are stored on
    the object
    """

    @property
    def short_url(self):
        return self.shortUrl

    @property
    def member_id(self):
        return self.idMembers

    @property
    def short_id(self):
        return self.idShort

    @property
    def list_id(self):
        return self.idList

    @property
    def board_id(self):
        return self.idBoard

    @property
    def description(self):
        return self.desc

    @property
    def date_last_activity(self):
        return self.dateLastActivity

    @description.setter
    def description(self, value):
        self.desc = value

    @property
    def idLabels(self):
        return self.label_ids

    @idLabels.setter
    def idLabels(self, values):
        self.label_ids = values

    @property
    def list_labels(self):
        if self.labels:
            return self.labels
        return None

    @property
    def comments(self):
        """
        Lazily loads and returns the comments
        """
        try:
            if self._comments is None:
                self._comments = self.fetch_comments()
        except AttributeError:
            self._comments = None
        return self._comments

    @property
    def checklists(self):
        """
        Lazily loads and returns the checklists
        """
        try:
            if self._checklists is None:
                self._checklists = self.fetch_checklists()
        except AttributeError:
            self._checklists = None
        return self._checklists

    @property
    def attachments(self):
        """
        Lazily loads and returns the attachments
        """
        try:
            if self._attachments is None:
                self._attachments = self.fetch_attachments()
        except AttributeError:
            self._attachments = None
        return self._attachments

    def __init__(self, parent, card_id, name=''):
        """
        :trello_list: reference to the parent list
        :card_id: ID for this card
        """
        if isinstance(parent, List):
            self.trello_list = parent
            self.board = parent.board
        else:
            self.board = parent

        self.client = parent.client
        self.id = card_id
        self.name = name

    @classmethod
    def from_json(cls, parent, json_obj):
        """
        Deserialize the card json object to a Card object

        :trello_list: the list object that the card belongs to
        :json_obj: json object
        """
        if 'id' not in json_obj:
            raise Exception("key 'id' is not in json_obj")
        card = cls(parent,
                   json_obj['id'],
                   name=json_obj['name'].encode('utf-8'))
        card.desc = json_obj.get('desc', '')
        card.due = json_obj.get('due', '')
        card.closed = json_obj['closed']
        card.url = json_obj['url']
        card.member_ids = json_obj['idMembers']
        card.idLabels = json_obj['idLabels']
        card.idList = json_obj['idList']
        card.labels = Label.from_json_list(card.board, json_obj['labels'])
        card.dateLastActivity = dateparser.parse(json_obj['dateLastActivity'])
        return card

    def __repr__(self):
        return '<Card %s>' % self.name

    def fetch(self, eager=True):
        """
        Fetch all attributes for this card
        :param eager: If eager is true comments and checklists will be fetched immediately, otherwise on demand
        """
        json_obj = self.client.fetch_json(
            '/cards/' + self.id,
            query_params={'badges': False})
        self.id = json_obj['id']
        self.name = json_obj['name'].encode('utf-8')
        self.desc = json_obj.get('desc', '')
        self.closed = json_obj['closed']
        self.url = json_obj['url']
        self.shortUrl = json_obj['shortUrl']
        self.idMembers = json_obj['idMembers']
        self.idShort = json_obj['idShort']
        self.idList = json_obj['idList']
        self.idBoard = json_obj['idBoard']
        self.idLabels = json_obj['idLabels']
        self.labels = Label.from_json_list(self.board, json_obj['labels'])
        self.badges = json_obj['badges']
        self.pos = json_obj['pos']
        if json_obj.get('due', ''):
            self.due = json_obj.get('due', '')
        else:
            self.due = ''
        self.checked = json_obj['checkItemStates']
        self.dateLastActivity = dateparser.parse(json_obj['dateLastActivity'])

        self._checklists = self.fetch_checklists() if eager else None
        self._comments = self.fetch_comments() if eager else None
        self._attachments = self.fetch_attachments() if eager else None

    def fetch_comments(self, force=False):
        comments = []

        if (force is True) or (self.badges['comments'] > 0):
            comments = self.client.fetch_json(
                '/cards/' + self.id + '/actions',
                query_params={'filter': 'commentCard'})
            return sorted(comments, key=lambda comment: comment['date'])
        return comments

    def get_list(self):
        obj = self.client.fetch_json('/lists/' + self.idList)
        return List.from_json(board=self, json_obj=obj)

    def get_comments(self):
        """Alias for fetch_comments for backward compatibility. Always contact server"""
        return self.fetch_comments(force=True)

    def fetch_checklists(self):
        checklists = []
        json_obj = self.client.fetch_json(
            '/cards/' + self.id + '/checklists', )
        # Thanks https://github.com/HuffAndPuff for noticing checklist were not sorted
        json_obj = sorted(json_obj, key=lambda checklist: checklist['pos'])
        for cl in json_obj:
            checklists.append(Checklist(self.client, self.checked, cl,
                                        trello_card=self.id))
        return checklists

    def fetch_attachments(self, force=False):
        items = []

        if (force is True) or (self.badges['attachments'] > 0):
            items = self.client.fetch_json(
                '/cards/' + self.id + '/attachments',
                query_params={'filter':'false'})
            return items
        return items

    def get_attachments(self):
        return self.fetch_attachments(force=True)

    def fetch_actions(self, action_filter='createCard', since=None, before=None):
        """
        Fetch actions for this card can give more argv to action_filter,
        split for ',' json_obj is list
        """
        json_obj = self.client.fetch_json(
            '/cards/' + self.id + '/actions',
            query_params={'filter': action_filter, "since": since, "before": before})
        self.actions = json_obj

    def attriExp(self, multiple):
        """
            Provides the option to explore what comes from trello
            :multiple is one of the attributes of GET /1/cards/[card id or shortlink]/actions
        """
        self.fetch_actions(multiple)
        return self.actions


    @staticmethod
    def _movement_as_triplet(source_list, destination_list, movement_datetime):
        return [source_list["name"], destination_list["name"], movement_datetime]


    @staticmethod
    def _movement_as_dict(source_list, destination_list, movement_datetime):
        _movement = {
            "source": source_list,
            "destination": destination_list,
            "datetime": movement_datetime,
        }
        return _movement


    def _list_movements(self, movement_function, filter_by_date_interval=None):
        """
        Returns the list of movements of this card.
        The list of movements is in descending date and time order. First movement is the closest one to now.
        Its structure is a list of dicts where the lists are "source" and "destination" and both are also dicts.
        Date and time of the movement is in key "datetime" as a datetime object.
        :param movement_function: function that returns a representation of the movement.
        :param filter_by_date_interval: Date interval used to filter card movements to return. Optional
        :return: list with the movements.
        """

        action_since = None if not filter_by_date_interval else filter_by_date_interval[0]
        action_before = None if not filter_by_date_interval else filter_by_date_interval[1]
        self.fetch_actions('updateCard:idList,', action_since, action_before)

        movements = []

        for idx in self.actions:
            date_str = idx['date']
            movement_datetime = dateparser.parse(date_str)
            source_list = idx['data']['listBefore']
            destination_list = idx['data']['listAfter']
            movement = movement_function(source_list, destination_list, movement_datetime)
            movements.append(movement)

        return movements


    def listCardMove_date(self):
        """
            Will return the history of transitions of a card from one list to another
            The lower the index the more resent the historical item

            It returns a list of lists. The sublists are triplets of
            starting list, ending list and when the transition occurred.
        """
        return self._list_movements(movement_function=Card._movement_as_triplet)


    def list_movements(self, list_cmp=None, filter_by_date_interval=None):
        """
        Will return the history of transitions of a card from one list to another
        The lower the index the more resent the historical item

        It returns a list of dicts in date and time descending order (the first movement is the earliest).
        Dicts are of the form source: <listobj> destination: <listobj> datetime: <datetimeobj>
        :param: list_cmp Comparison function between lists. For list_cmp(a, b) returns -1 if list a is greater that list b. Returns 1 otherwise.
        :param: filter_by_date_interval: pair of two dates (two strings in YYYY-MM-DD format) to filter card movements by date.
        """

        movement_as_dict_function = Card._movement_as_dict
        if list_cmp:
            def movement_as_dict_function(_source_list, _destination_list, _movement_datetime):
                _movement = Card._movement_as_dict(_source_list, _destination_list, _movement_datetime)
                _source_list_id = _source_list["id"]
                _destination_list_id = _destination_list["id"]
                _movement["moving_forward"] = list_cmp(_source_list_id, _destination_list_id) > 0
                return _movement

        return self._list_movements(movement_function=movement_as_dict_function, filter_by_date_interval=filter_by_date_interval)


    def get_stats_by_list(self, tz, lists, list_cmp=None, done_list=None, time_unit="seconds", card_movements_filter=None):
        """
        Gets several stats about the card by each list of the board:
        - time: The time that the card has been in each column in seconds (minutes or hours).
        - forward_moves: How many times this card has been the source of a forward movement.
        - backward_moves: How many times this card has been the source of a backward movement.

        Returns a dict where the key is list id and value is a dict with keys
        time, forward_moves and backward_moves.

        :param tz: timezone to make comparison timezone-aware
        :param lists: list of board lists.
        :param list_cmp: function that compares two lists a,b given id_a, id_b. If b is in a forward position returns 1 else -1.
        :param time_unit: default to seconds. Allow specifying time in "minutes" or "hours".
        :param done_list: Column that implies that the task is done. If present, time measurement will be stopped if is current task list.
        :param card_movements_filter: Pair of two dates (two strings in YYYY-MM-DD format) that will filter the movements of the card. Optional.
        :return: dict of the form {list_id: {time:<time card was in that list>, forward_moves: <number>, backward_moves: <number> }}
        """

        # Conversion of units
        seconds_to_time_unit = lambda time: time
        if time_unit == "minutes":
            seconds_to_time_unit = lambda time: time / 60.0
        elif time_unit == "hours":
            seconds_to_time_unit = lambda time: time / 3660.0

        # Creation datetime of the card
        creation_datetime = self.create_date

        #  Time in seconds stores the seconds that our card lives in a column
        stats_by_list = {list_.id: {"time":0, "forward_moves":0, "backward_moves":0} for list_ in lists}

        #  Last action date, used to compute the time the card spends between changes
        # of columns
        last_action_datetime = creation_datetime

        # Changes of columns of our card
        # Using list comparison function (if present) to check list position and, hence,
        # if the card movement was forward or backwards
        changes = self.list_movements(list_cmp, card_movements_filter)

        #  If there are no changes in the card, all its life has been in its creation list
        if len(changes) == 0:
            card_life_time = seconds_to_time_unit((datetime.datetime.now(tz) - last_action_datetime).total_seconds())
            stats_by_list[self.idList]["time"] += card_life_time

        else:
            # Changes in card are in reversed order (closer to now are first)
            last_list = None
            for change in reversed(changes):
                source_list = change["source"]
                destination_list = change["destination"]
                change_datetime = change["datetime"]

                # For each column the total number of seconds this card is computed
                source_list_id = source_list["id"]

                time_from_last_list_change = seconds_to_time_unit((change_datetime - last_action_datetime).total_seconds())
                stats_by_list[source_list_id]["time"] += time_from_last_list_change

                # Count if the change is to move forward or backwards
                if "moving_forward" in change:
                    if change["moving_forward"]:
                        stats_by_list[source_list_id]["forward_moves"] += 1
                    else:
                        stats_by_list[source_list_id]["backward_moves"] += 1

                # Our last action has been this change
                last_action_datetime = change_datetime

                # Store the last list
                last_list = destination_list

            # Adding the number of seconds the card has been in its last column (until now)
            # only if the last column is not "Done" column
            if done_list and last_list["id"] != done_list.id:
                time_card_has_spent_in_list_until_now = seconds_to_time_unit((datetime.datetime.now(tz) - last_action_datetime).total_seconds())
                stats_by_list[last_list["id"]]["time"] += time_card_has_spent_in_list_until_now

        return stats_by_list


    @property
    def latestCardMove_date(self):
        """
            returns the date of the last card transition

        """
        self.fetch_actions('updateCard:idList')
        date_str = self.actions[0]['date']
        return dateparser.parse(date_str)

    @property
    def create_date(self):
        """Will return the creation date of the card.

        WARNING: if the card was create via convertion of a checklist item
                it fails. attriExp('convertToCardFromCheckItem') allows to
                test for the condition.
        """
        self.fetch_actions()
        date_str = self.actions[0]['date']
        return dateparser.parse(date_str)

    @property
    def card_created_date(self):
        """Will return the creation date of the card.

        NOTE: This will return the date the card was created, even if it
        was created on another board. The created_date() above actually just
        returns the first activity and has the issue described in the warning.

        The first 8 characters of the card id is a hexadecimal number.
        Converted to a decimal from hexadecimal, the timestamp is an Unix
        timestamp (the number of seconds that have elapsed since January 1,
        1970 midnight UTC.See
        http://help.trello.com/article/759-getting-the-time-a-card-or-board-was-created
        """
        unix_time = int(self.id[:8],16)

        return datetime.fromtimestamp(unix_time)

    @property
    def due_date(self):
        return dateparser.parse(self.due) if self.due else ''

    def set_name(self, new_name):
        """
        Update the name on the card to :new_name:
        """
        self._set_remote_attribute('name', new_name)
        self.name = new_name

    def set_description(self, description):
        self._set_remote_attribute('desc', description)
        self.desc = description

    def set_due(self, due):
        """Set the due time for the card

        :due: a datetime object
        """
        datestr = due.strftime('%Y-%m-%dT%H:%M:%S')
        self._set_remote_attribute('due', datestr)
        self.due = datestr

    def set_pos(self, pos):
        """
        Update card position in list

        :pos: 'top', 'bottom' or int
        """
        self._set_remote_attribute('pos', pos)
        self.pos = pos

    def set_closed(self, closed):
        self._set_remote_attribute('closed', closed)
        self.closed = closed


    def delete_comment(self,comment):
        # Delete this card permanently
        self.client.fetch_json(
            '/cards/' + self.id + '/actions/' + comment['id'] + '/comments',
            http_method='DELETE')

    def delete(self):
        # Delete this card permanently
        self.client.fetch_json(
            '/cards/' + self.id,
            http_method='DELETE')

    def assign(self, member_id):
        self.client.fetch_json(
            '/cards/' + self.id + '/members',
            http_method='POST',
            post_args={'value': member_id})

    def unassign(self, member_id):
        self.client.fetch_json(
            '/cards/' + self.id + '/idMembers/' + member_id,
            http_method='DELETE')

    def subscribe(self):
        self.client.fetch_json(
            '/cards/' + self.id + '/subscribed',
            http_method='PUT',
            post_args={'value': True})

    def comment(self, comment_text):
        """Add a comment to a card."""
        self.client.fetch_json(
            '/cards/' + self.id + '/actions/comments',
            http_method='POST',
            post_args={'text': comment_text})

    def add_label(self, label):
        self.client.fetch_json(
            '/cards/' + self.id + '/idLabels',
            http_method='POST',
            post_args={'value': label.id})

    def remove_label(self, label):
        self.client.fetch_json(
            '/cards/' + self.id + '/idLabels/' + label.id,
            http_method='DELETE')

    def attach(self, name=None, mimeType=None, file=None, url=None):
        """
        Add an attachment to the card. The attachment can be either a
        file or a url. Setting the name and/or mime type is optional.
        :param name: The name of the attachment
        :param mimeType: mime type for the attachement
        :param file: a file-like, binary object that supports read()
        :param url: a URL pointing to the resource to be attached
        """
        if (file and url) or (not file and not url):
            raise Exception('Please provide either a file or url, and not both!')

        kwargs = {}
        if file:
            kwargs['files'] = dict(file=(name, file, mimeType))
        else:
            kwargs['name'] = name
            kwargs['mimeType'] = mimeType
            kwargs['url'] = url

        self._post_remote_data(
            'attachments', **kwargs
        )

    def remove_attachment(self,attachment_id):
        """
        Remove attachment from card
        :param attachment_id: Attachment id
        :return: None
        """
        self.client.fetch_json(
            '/cards/' + self.id + '/attachments/' + attachment_id,
            http_method='DELETE')

    def change_list(self, list_id):
        self.client.fetch_json(
            '/cards/' + self.id + '/idList',
            http_method='PUT',
            post_args={'value': list_id})

    def change_board(self, board_id, list_id=None):
        args = {'value': board_id}
        if list_id is not None:
            args['idList'] = list_id
        self.client.fetch_json(
            '/cards/' + self.id + '/idBoard',
            http_method='PUT',
            post_args=args)

    def add_checklist(self, title, items, itemstates=None):

        """Add a checklist to this card

        :title: title of the checklist
        :items: a list of the item names
        :itemstates: a list of the state (True/False) of each item
        :return: the checklist
        """
        if itemstates is None:
            itemstates = []

        json_obj = self.client.fetch_json(
            '/cards/' + self.id + '/checklists',
            http_method='POST',
            post_args={'name': title}, )

        cl = Checklist(self.client, [], json_obj, trello_card=self.id)
        for i, name in enumerate(items):
            try:
                checked = itemstates[i]
            except IndexError:
                checked = False
            cl.add_checklist_item(name, checked)

        self.fetch()
        return cl

    def _set_remote_attribute(self, attribute, value):
        self.client.fetch_json(
            '/cards/' + self.id + '/' + attribute,
            http_method='PUT',
            post_args={'value': value}, )

    def _post_remote_data(self, attribute, files=None, **kwargs):
        self.client.fetch_json(
            '/cards/' + self.id + '/' + attribute,
            http_method='POST',
            files=files,
            post_args=kwargs)


from trello.trellolist import List
