# -*- coding: utf-8 -*-
from dateutil import parser as dateparser

from trello.base import TrelloBase


class Attachments(TrelloBase):
    """
    https://developers.trello.com/advanced-reference/card#get-1-cards-card-id-or-shortlink-attachments
    """
    def __init__(self, id, bytes, date, edge_color, idMember, is_upload, mime_type, name, previews, url):
        super(Attachments, self).__init__()
        self.id = id
        self.bytes = bytes
        self.date = dateparser.parse(date)
        self.edge_color = edge_color
        self.idMember = idMember
        self.is_upload = is_upload
        self.mime_type = mime_type
        self.name = name
        self.previews = previews
        self.url = url

    @staticmethod
    def from_json(json_obj):
        id = json_obj.get("id")
        bytes = json_obj.get("bytes")
        date = json_obj.get("date")
        edge_color = json_obj.get("edgeColor")
        idMember = json_obj.get("idMember")
        is_upload = json_obj.get("isUpload")
        mime_type = json_obj.get("mimeType")
        name = json_obj.get("name")
        previews = [AttachmentsPreview.from_json(preview_json) for preview_json in json_obj.get("previews")]
        url = json_obj.get("url")

        return Attachments(id, bytes, date, edge_color, idMember, is_upload, mime_type, name, previews, url)

    def __repr__(self):
        return u"<Attachments {0}>".format(self.name)


class AttachmentsPreview(object):
    def __init__(self, bytes, url, width, height, is_scaled):
        self.bytes = bytes
        self.url = url
        self.width = width
        self.height = height
        self.is_scaled = is_scaled

    @staticmethod
    def from_json(json_obj):
        bytes = json_obj.get("bytes")
        url = json_obj.get("url")
        width = json_obj.get("width")
        height = json_obj.get("height")
        is_scaled = json_obj.get("scaled")

        return AttachmentsPreview(bytes, url, width, height, is_scaled)

    def __repr__(self):
        return u"<Attachments Preview {0}x{1}".format(self.width, self.height)
