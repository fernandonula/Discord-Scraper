from mongoengine import DynamicDocument, StringField, DecimalField, ListField

class DiscordChannels(DynamicDocument):
    cid = StringField(required=True)
    name = StringField(required=True)
    last_message_id = StringField()
    type = DecimalField()
    position = DecimalField()
    flags = DecimalField()
    parent_id = StringField()
    topic = StringField()
    guild_id = StringField(required=True)
    last_pin_timestamp = StringField()
    rate_limit_per_user = DecimalField()


""" Example {
   "id":"694726186638770236",
   "last_message_id":"990817180138475580",
   "type":5,
   "name":"📢global-announcements",
   "position":2,
   "flags":0,
   "parent_id":"None",
   "topic":"None",
   "guild_id":"692403822265368626",
   "permission_overwrites":[
      {
         "id":"978790542643195917",
         "type":0,
         "allow":"137439332416",
         "deny":"0"
      }
   ],
   "last_pin_timestamp":"2022-05-08T18:36:51+00:00",
   "rate_limit_per_user":0,
   "nsfw":false
} """