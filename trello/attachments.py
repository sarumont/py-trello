# -*- coding: utf-8 -*-


class Attachments(object):
    """
    https://developers.trello.com/advanced-reference/card#get-1-cards-card-id-or-shortlink-attachments
    """
    def __init__(self, id, bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews, url):
        self.id = id
        self.bytes = bytes
        self.date = date
        self.edge_color = edgeColor
        self.idMember = idMember
        self.is_upload = isUpload
        self.mime_type = mimeType
        self.name = name
        self.previews = previews
        self.url = url

    @staticmethod
    def from_json(json_obj):
        id = json_obj.get("id")
        bytes = json_obj.get("bytes")
        date = json_obj.get("date")
        edgeColor = json_obj.get("edgeColor")
        idMember = json_obj.get("idMember")
        isUpload = json_obj.get("isUpload")
        mimeType = json_obj.get("mimeType")
        name = json_obj.get("name")
        previews = json_obj.get("previews")
        url = json_obj.get("url")

        return Attachments(id, bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews, url)

    def __repr__(self):
        return u"<Attachments {0}>".format(self.name)
