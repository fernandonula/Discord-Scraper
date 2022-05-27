from mongoengine import Document, StringField, DateTimeField, DecimalField
from datetime import datetime


class DiscordMessageModels(Document):
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