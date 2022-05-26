from mongoengine import Document, StringField, URLField, DecimalField

class MessageModel(Document):
    authorName = StringField(max_length=120)
    authorAvatarId = StringField(max_length=35)
    authorId = StringField(max_length=20)
    content = StringField(required=True)
    channelId = StringField(required=True, max_length=20)
    guildId = StringField(required=True, max_length=35)
    type = DecimalField()
    mId = StringField(max_length=20)