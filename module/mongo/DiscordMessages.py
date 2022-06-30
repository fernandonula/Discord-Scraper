from mongoengine import DynamicDocument, StringField, DateTimeField, DecimalField, ListField
from datetime import datetime


class DiscordMessages(DynamicDocument):
    authorName = StringField(max_length=120)
    authorAvatarId = StringField(max_length=35)
    authorId = StringField(max_length=20)
    content = StringField(required=True)
    channelId = StringField(required=True, max_length=20)
    guildId = StringField(required=True, max_length=35)
    channelname = StringField(max_length=120)
    type = DecimalField()
    mId = StringField(max_length=20)
    mDate = DateTimeField(required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow)
    attachments = ListField()
    embeds = ListField()
    mentions = ListField()
    components = ListField()