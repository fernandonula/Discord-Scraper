from mongoengine import DynamicDocument, StringField, DecimalField, ListField
from bson.objectid import ObjectId


class DiscordServers(DynamicDocument):
    _id = ObjectId()
    sid = StringField(required=True)
    name = StringField(required=True)
    icon = StringField()
    description = StringField()
    splash = StringField()
    discovery_splash = StringField()
    features = ListField(StringField())
    default_message_notifications = DecimalField()
    mfa_level = DecimalField()
    explicit_content_filter = DecimalField()
    max_presences = StringField()
    max_members = DecimalField()
    max_video_channel_users = DecimalField()
    vanity_url_code = StringField()
    premium_tier = DecimalField()
    premium_subscription_count = DecimalField()
    system_channel_flags = DecimalField()
    preferred_locale = StringField()
    rules_channel_id = StringField()
    public_updates_channel_id = StringField()
    hub_type = StringField()

""" Example {
   "id":"692403822265368626",
   "name":"Gala Games",
   "icon":"a_4fdb737f3cc0b8fec432121f19f4e238",
   "description":"Gala Games",
   "splash":"14d16db4388da6d1b2df0bef2e5c211a",
   "discovery_splash":"1047210851c75cda2b67a30fa7179b73",
   "features":[
      "NEW_THREAD_PERMISSIONS",
      "SEVEN_DAY_THREAD_ARCHIVE",
      "PARTNERED",
      "NEWS",
      "AUTO_MODERATION",
      "BANNER"
   ],
   "emojis":[
      {
         "name":"TWD_VOXCarl",
         "roles":[
            
         ],
         "id":"958607974031560764",
         "require_colons":true,
         "managed":false,
         "animated":false,
         "available":true
      }
   ],
   "stickers":[
      {
         "id":"951896330152841266",
         "name":"Ronin",
         "tags":"person_fencing",
         "type":2,
         "format_type":1,
         "description":"",
         "asset":"",
         "available":true,
         "guild_id":"692403822265368626"
      }
   ],
   "default_message_notifications":1,
   "mfa_level":1,
   "explicit_content_filter":2,
   "max_presences":"None",
   "max_members":500000,
   "max_video_channel_users":25,
   "vanity_url_code":"gogalagames",
   "premium_tier":3,
   "premium_subscription_count":202,
   "system_channel_flags":8,
   "preferred_locale":"en-US",
   "rules_channel_id":"738980285588439053",
   "public_updates_channel_id":"739191113843474592",
   "hub_type":"None",
   "premium_progress_bar_enabled":true,
   "nsfw":false,
   "nsfw_level":0
} """