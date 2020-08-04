# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import

import datetime
from operator import itemgetter

import pytz
from dateutil import parser as dateparser

from trello import TrelloBase
from trello.attachments import Attachments
from trello.checklist import Checklist
from trello.compat import force_str
from trello.label import Label
from trello.organization import Organization
from trello.customfield import CustomField, CustomFieldText, CustomFieldCheckbox, CustomFieldNumber, CustomFieldDate, CustomFieldList


class Card(TrelloBase):
    """
    Class representing a Trello card. Card attributes are stored on
    the object

    https://developers.trello.com/advanced-reference/card
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

    @property
    def labels(self):
        if self._labels:
            return self._labels
        return None

    @property
    def custom_fields(self):
        """
        Lazily loads and returns the custom fields
        """
        if self.customFields is None:
            self.customFields = self.fetch_custom_fields()
        return self.customFields

    @property
    def comments(self):
        """
        Lazily loads and returns the comments
        """
        if self._comments is None:
            self._comments = self.fetch_comments()
        return self._comments

    @property
    def checklists(self):
        """
        Lazily loads and returns the checklists
        """
        if self._checklists is None:
            self._checklists = self.fetch_checklists()
        return self._checklists

    @property
    def plugin_data(self):
        """
        Lazily loads and returns the plugin data
        """
        if self._plugin_data is None:
            self._plugin_data = self.fetch_plugin_data()
        return self._plugin_data

    @property
    def attachments(self):
        """
        Lazily loads and returns the attachments
        """
        if self._attachments is None:
            self._attachments = self.fetch_attachments()
        return self._attachments

    def __init__(self, parent, card_id, name=''):
        """
        :parent: reference to the parent trello list
        :card_id: ID for this card
        """
        super(Card, self).__init__()
        if isinstance(parent, List):
            self.trello_list = parent
            self.board = parent.board
        else:
            self.board = parent

        self.client = parent.client
        self.id = card_id
        self.name = name

        self.customFields = None
        self._checklists = None
        self._comments = None
        self._plugin_data = None
        self._attachments = None
        self._labels = None
        self._json_obj = None

    @classmethod
    def from_json(cls, parent, json_obj):
        """
        Deserialize the card json object to a Card object

        :parent: the list object that the card belongs to
        :json_obj: json object

        :rtype: Card
        """
        if 'id' not in json_obj:
            raise Exception("key 'id' is not in json_obj")
        card = cls(parent,
                   json_obj['id'],
                   name=json_obj['name'])
        card._json_obj = json_obj
        card.desc = json_obj.get('desc', '')
        card.due = json_obj.get('due', '')
        card.is_due_complete = json_obj['dueComplete']
        card.closed = json_obj['closed']
        card.url = json_obj['url']
        card.pos = json_obj['pos']
        card.shortUrl = json_obj['shortUrl']
        card.idMembers = json_obj['idMembers']
        card.member_ids = json_obj['idMembers']
        card.idLabels = json_obj['idLabels']
        card.idBoard = json_obj['idBoard']
        card.idList = json_obj['idList']
        card.idShort = json_obj['idShort']
        card.badges = json_obj['badges']
        card.customFields = card.fetch_custom_fields(json_obj=json_obj)
        card.countCheckItems = json_obj['badges']['checkItems']
        card._labels = Label.from_json_list(card.board, json_obj['labels'])
        card.dateLastActivity = dateparser.parse(json_obj['dateLastActivity'])
        if "attachments" in json_obj:
            card._attachments = []
            for attachment_json in json_obj["attachments"]:
                card._attachments.append(attachment_json)
        if 'actions' in json_obj:
            card.actions = json_obj['actions']
        return card

    def __repr__(self):
        return force_str(u'<Card %s>' % self.name)

    def fetch(self, eager=True):
        """
        Fetch all attributes for this card

        :param eager: If eager, comments, checklists and attachments will be fetched immediately, otherwise on demand
        """
        json_obj = self.client.fetch_json(
            '/cards/' + self.id,
            query_params={'badges': False, 'customFieldItems': 'true'})
        self.id = json_obj['id']
        self.name = json_obj['name']
        self.desc = json_obj.get('desc', '')
        self.closed = json_obj['closed']
        self.url = json_obj['url']
        self.shortUrl = json_obj['shortUrl']
        self.idMembers = json_obj['idMembers']
        self.idShort = json_obj['idShort']
        self.idList = json_obj['idList']
        self.idBoard = json_obj['idBoard']
        self.idLabels = json_obj['idLabels']
        self._labels = Label.from_json_list(self.board, json_obj['labels'])
        self.badges = json_obj['badges']
        self.pos = json_obj['pos']
        if json_obj.get('due', ''):
            self.due = json_obj.get('due', '')
        else:
            self.due = ''
        self.checked = json_obj['checkItemStates']
        self.dateLastActivity = dateparser.parse(json_obj['dateLastActivity'])

        self._customFields = self.fetch_custom_fields(json_obj=json_obj)
        self._plugin_data = self.fetch_plugin_data() if eager else None
        self._checklists = self.fetch_checklists() if eager else None
        self._comments = self.fetch_comments() if eager else None
        self._attachments = self.fetch_attachments() if eager else None

    def fetch_custom_fields(self, json_obj=None):
        """
        Fetch current set of custom fields from card or json_obj.
        """
        if json_obj is None:
            json_obj = self.client.fetch_json(
                '/cards/' + self.id,
                query_params={'badges': False, 'customFieldItems': 'true'})
        return CustomField.from_json_list(
            self, json_obj.get('customFieldItems', {}))

    def fetch_comments(self, force=False, limit=None):
        comments = []

        if (force is True) or (self.badges['comments'] > 0):
            query_params = {'filter': 'commentCard,copyCommentCard'}
            if limit is not None:
                query_params['limit'] = limit
            comments = self.client.fetch_json(
                '/cards/' + self.id + '/actions',
                query_params=query_params)
            return sorted(comments, key=lambda comment: comment['date'])
        return comments

    def get_list(self):
        obj = self.client.fetch_json('/lists/' + self.idList)
        return List.from_json(board=self, json_obj=obj)

    def get_comments(self):
        """Alias for fetch_comments for backward compatibility.
        Always contact server
        """
        return self.fetch_comments(force=True)

    def fetch_checklists(self):

        if self.countCheckItems == 0:
            return []
        
        if not hasattr(self, "checked") or self.checked is None:
            self.fetch(eager=False)

        checklists = []
        json_obj = self.client.fetch_json(
            '/cards/' + self.id + '/checklists', )
        # Thanks https://github.com/HuffAndPuff for noticing checklist
        # were not sorted
        json_obj = sorted(json_obj, key=lambda checklist: checklist['pos'])
        for cl in json_obj:
            checklists.append(Checklist(self.client, self.checked, cl,
                                        trello_card=self.id))
        return checklists

    def fetch_plugin_data(self):
        items = self.client.fetch_json(
            '/cards/' + self.id + '/pluginData')
        return items

    def fetch_attachments(self, force=False):
        if (force is True) or (self.badges['attachments'] > 0):
            items = self.client.fetch_json(
                '/cards/' + self.id + '/attachments',
                query_params={'filter':'false'})
            return items
        return []

    def get_attachments(self):
        return [Attachments.from_json(attachments_json) for attachments_json in self.fetch_attachments(force=True)]

    def fetch_actions(self, action_filter='createCard', since=None, before=None, action_limit=50):
        """
        Fetch actions for this card can give more argv to action_filter,
        split for ',' json_obj is list
        """
        query_params={'filter': action_filter, 'limit': action_limit}
        if since:
            query_params["since"] = since

        if before:
            query_params["before"] = before

        json_obj = self.client.fetch_json(
            '/cards/' + self.id + '/actions',
            query_params=query_params)

        self.actions = json_obj
        return self.actions

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
        if not hasattr(self, "actions") or self.actions is None:
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
        """Will return the history of transitions of a card from one list to
        another. The lower the index the more recent the historical item.

        It returns a list of lists. The sublists are triplets of
        starting list, ending list and when the transition occurred.
        """
        return self._list_movements(movement_function=Card._movement_as_triplet)

    def list_movements(self, list_cmp=None, filter_by_date_interval=None):
        """Will return the history of transitions of a card from one list to
        another. The lower the index the more recent the historical item.

        It returns a list of dicts in date and time descending order (the
        first movement is the most recent).
        Dicts are of the form source:
        <listobj> destination: <listobj> datetime: <datetimeobj>

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

    def get_stats_by_list(self, lists, list_cmp=None, done_list=None, time_unit="seconds", card_movements_filter=None):
        """Gets several stats about the card by each list of the board:
        - time: The time that the card has been in each column in seconds (minutes or hours).
        - forward_moves: How many times this card has been the source of a forward movement.
        - backward_moves: How many times this card has been the source of a backward movement.

        Returns a dict where the key is list id and value is a dict with keys
        time, forward_moves and backward_moves.

        :param lists: list of board lists.
        :param list_cmp: function that compares two lists a,b given id_a, id_b. If b is in a forward position returns 1 else -1.
        :param time_unit: default to seconds. Allow specifying time in "minutes" or "hours".
        :param done_list: Column that implies that the task is done. If present, time measurement will be stopped if is current task list.
        :param card_movements_filter: Pair of two dates (two strings in YYYY-MM-DD format) that will filter the movements of the card. Optional.
        :return: dict of the form {list_id: {time:<time card was in that list>, forward_moves: <number>, backward_moves: <number> }}
        """
        tz = pytz.timezone(Organization.TIMEZONE)

        # Conversion of units
        seconds_to_time_unit = lambda time: time
        if time_unit == "minutes":
            seconds_to_time_unit = lambda time: time / 60.0
        elif time_unit == "hours":
            seconds_to_time_unit = lambda time: time / 3660.0

        # Creation datetime of the card
        creation_datetime = self.created_date

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
            # Changes in card are ordered to get the dates in order
            last_list = None

            ordered_changes = sorted(changes, key=itemgetter("datetime"))
            # For each arrival to a list, its datetime will be used to compute
            # the time this card is in that destination list
            for change in ordered_changes:
                source_list = change["source"]
                destination_list = change["destination"]
                change_datetime = change["datetime"]

                # For each column the total number of seconds this card is computed
                source_list_id = source_list["id"]

                time_from_last_list_change = seconds_to_time_unit((change_datetime - last_action_datetime).total_seconds())

                # In case the source or destination list is not a list of this board, ignore them
                if source_list_id not in stats_by_list or not destination_list["id"] not in stats_by_list:
                    continue

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
                if done_list and last_list and last_list["id"] and last_list["id"] in stats_by_list and\
                    last_list["id"] != done_list.id:
                    time_card_has_spent_in_list_until_now = seconds_to_time_unit((datetime.datetime.now(tz) - last_action_datetime).total_seconds())
                    stats_by_list[last_list["id"]]["time"] += time_card_has_spent_in_list_until_now

        return stats_by_list

    @property
    def latestCardMove_date(self):
        """Returns the date of the last card transition"""
        self.fetch_actions('updateCard:idList')
        if self.actions is None or len(self.actions) == 0:
            return None
        date_str = self.actions[0]['date']
        return dateparser.parse(date_str)

    @property
    def created_date(self):
        """Will return the creation date of the card.

        WARNING: if the card was create via convertion of a checklist item
                it fails. attriExp('convertToCardFromCheckItem') allows to
                test for the condition.
        """
        if not hasattr(self, "creation_date"):
            localtz = pytz.timezone(Organization.TIMEZONE)
            self.creation_date = localtz.localize(datetime.datetime.fromtimestamp(int(self.id[0: 8], 16)))
        return self.creation_date

    @property
    def card_created_date(self):
        """Will return the creation date of the card.

        NOTE: This will return the date the card was created, even if it
        was created on another board. The created_date() above actually just
        returns the first activity and has the issue described in the warning.

        The first 8 characters of the card id is a hexadecimal number.
        Converted to a decimal from hexadecimal, the timestamp is an Unix
        timestamp (the number of seconds that have elapsed since January 1,
        1970 midnight UTC. See
        http://help.trello.com/article/759-getting-the-time-a-card-or-board-was-created
        """
        unix_time = int(self.id[:8], 16)

        return datetime.datetime.fromtimestamp(unix_time)

    @property
    def due_date(self):
        return dateparser.parse(self.due) if self.due else ''

    def set_name(self, new_name):
        """Update the name on the card to :new_name:

        :new_name: str
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
        datestr = due.isoformat()
        self._set_remote_attribute('due', datestr)
        self.due = datestr

    def set_due_complete(self):
        """Set due complete

        :return: None
        """
        self._set_due_complete(True)

    def remove_due_complete(self):
        """Remove due complete

        :return: None
        """
        self._set_due_complete(False)


    def remove_due(self):
        """
        Remove the due datetime of this card.
        """
        self._set_remote_attribute('due', None)
        self.due = ''

    def set_pos(self, pos):
        """
        Update card position in list

        :pos: 'top', 'bottom' or int
        """
        self._set_remote_attribute('pos', pos)
        self.pos = pos
        
    def set_custom_field(self, value, custom_field):
        """Update card custom field
        
        Arguments:
            value {[str, int, date, bool]} -- Value depending on the type of custom_field
            custom_field {custom field object} -- Custom Field Object (board.get_custom_field_definitions()[0])

        """
        if custom_field.field_type in ['text', 'number', 'date', 'checked']:
            if value == "":
                post_args = {'value': ""}
            else:
                post_args = {'value': {str(custom_field.field_type): value}}
        else:
            if value == "":
                list_field_id = ""
            else:
                try:
                    list_field_id = [
                        x for x, y in custom_field.list_options.items() if y == value][0]
            post_args = {'idValue': list_field_id}

        self.client.fetch_json(
            '/card/' + self.id + '/customField/' + custom_field.id + '/item',
            http_method='PUT',
            post_args=post_args)

    def set_closed(self, closed):
        self._set_remote_attribute('closed', closed)
        self.closed = closed

    def delete_comment(self, comment):
        # Delete this comment permanently
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
        """Add a comment to a card.

        :comment_text: str
        """
        comment_data = self.client.fetch_json(
            '/cards/' + self.id + '/actions/comments',
            http_method='POST',
            post_args={'text': comment_text})
        return comment_data

    def update_comment(self, comment_id, comment_text):
        """Update a comment."""
        comment_data = self.client.fetch_json(
            '/actions/' + comment_id,
            http_method='PUT',
            post_args={'text': comment_text}
        )
        return comment_data

    def add_label(self, label):
        self.client.fetch_json(
            '/cards/' + self.id + '/idLabels',
            http_method='POST',
            post_args={'value': label.id})

    def create_label(self, name, color):
        self.client.fetch_json(
            "/cards/" + self.id + "/labels",
            http_method='POST',
            post_args={"name": name, "color": color})

    def remove_label(self, label):
        self.client.fetch_json(
            '/cards/' + self.id + '/idLabels/' + label.id,
            http_method='DELETE')

    def add_member(self, member):
        self.client.fetch_json(
            '/cards/' + self.id + '/idMembers',
            http_method='POST',
            post_args={'value': member.id})

    def remove_member(self, member):
        self.client.fetch_json(
            '/cards/' + self.id + '/idMembers/' + member.id,
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

        return self._post_remote_data('attachments', **kwargs)

    def remove_attachment(self, attachment_id):
        """
        Remove attachment from card
        :param attachment_id: Attachment id
        :return: None
        """
        self.client.fetch_json(
            '/cards/' + self.id + '/attachments/' + attachment_id,
            http_method='DELETE')

    def change_pos(self, position):
        self.client.fetch_json(
            '/cards/' + self.id + '/pos',
            http_method='PUT',
            post_args={'value': position})

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

    def _set_due_complete(self, is_complete):
        """Set due is complete or not complete

        https://developers.trello.com/advanced-reference/card#put-1-cards-card-id-or-shortlink-dueComplete
        :param is_complete: boolean
        :return: None
        """
        self.client.fetch_json('/cards/' + self.id + '/dueComplete',
                               http_method='PUT',
                               post_args={'value': is_complete})

    def _set_remote_attribute(self, attribute, value):
        self.client.fetch_json(
            '/cards/' + self.id + '/' + attribute,
            http_method='PUT',
            post_args={'value': value}, )

    def _post_remote_data(self, attribute, files=None, **kwargs):
        return self.client.fetch_json(
            '/cards/' + self.id + '/' + attribute,
            http_method='POST',
            files=files,
            post_args=kwargs)

    def get_custom_field_by_name(self, cf_name):
        """
        Returns existing custom field by name or creates a new one.
        """
        for cf in self.customFields:
            if cf.name == cf_name:
                return cf

        cf_class = None
        cf_def_id = None
        for definition in self.board.get_custom_field_definitions():
            if definition.name == cf_name:
                cf_def_id = definition.id
                cf_class = {
                    'checkbox': CustomFieldCheckbox,
                    'date': CustomFieldDate,
                    'list': CustomFieldList,
                    'number': CustomFieldNumber,
                    'text': CustomFieldText,
                }.get(definition.field_type)
        if cf_class is None:
            raise ValueError('Unknown custom field name specified ({})'.format(cf_name))
        return cf_class(self, 'unknown', cf_def_id, '')

from trello.trellolist import List
