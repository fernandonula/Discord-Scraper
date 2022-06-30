from mongoengine import connect, disconnect
from .DiscordServers import DiscordServers
from .DiscordMessages import DiscordMessages
from .DiscordChannels import DiscordChannels
import threading
from datetime import datetime


class Storage(object):
    """
    This class contain all code to save and recovery data from  mongo db 
    """

    def __init__(self, mongoconnection):
        self.mongoconnection=mongoconnection
        connect(host=mongoconnection)

    # def __del__(self):
        # disconnect()

    # async import messages method 
    def importMessagesFromDiscord(self, messages, guildId, channelname) :
        # import messages using async way
        thr = threading.Thread(target=self._importMessagesFromDiscord, args=(messages, guildId, channelname), kwargs={})
        thr.start()

    # sync import messages method 
    def _importMessagesFromDiscord(self, messages, guildId, channelname) :
        # all messages loop
        for message in messages:
            content = message[0]["content"]
            # if havent content then go to next message
            if (content):
                author = message[0]["author"]
                try :
                    messageModel = DiscordMessages.objects.get(channelId=message[0]["channel_id"], mId=message[0]["id"])
                except :
                    messageModel = DiscordMessages()
                # ignore if havent author
                if (author) :
                    messageModel.authorName = author["username"]
                    messageModel.authorAvatarId = author["avatar"]
                    messageModel.authorId = author["id"]
                messageModel.content = content
                messageModel.channelId = message[0]["channel_id"]
                messageModel.guildId = guildId
                messageModel.type = message[0]["type"]
                messageModel.channelname = channelname
                messageModel.mId = message[0]["id"]
                # TODO: Convert UTC to local timezone                
                messageModel.mDate = datetime.strptime(message[0]["timestamp"].replace("+00:00", ""),'%Y-%m-%dT%H:%M:%S.%f')
                # try catch to not block python
                try:
                    # Save each message on mongodb
                    messageModel.save()
                except Exception as e:
                    print("Error to save discord message on mongo")
                    print(e)
        return True

    def importServerData(self, data) :
        # import messages using async way
        thr = threading.Thread(target=self._importServerData, args=(), kwargs=data)
        thr.start()

    # import server/guild method 
    def _importServerData(self, **data) :
        print("-------- SERVER DATA ---------- SERVER DATA --------- SERVER DATA")
        if (not data['id']) :
            return False;
        try :
            discordServers = DiscordServers.objects.get(sid=data['id'])
        except :
            discordServers = DiscordServers()
        discordServers.sid = data['id']
        discordServers.name = data['name']
        discordServers.icon = data['icon']
        discordServers.description = data['description']
        discordServers.splash = data['splash']
        discordServers.discovery_splash = data['discovery_splash']
        discordServers.features = data['features']
        discordServers.default_message_notifications = data['default_message_notifications']
        discordServers.mfa_level = data['mfa_level']
        discordServers.explicit_content_filter = data['explicit_content_filter']
        discordServers.max_presences = data['max_presences']
        discordServers.max_members = data['max_members']
        discordServers.max_video_channel_users = data['max_video_channel_users']
        discordServers.vanity_url_code = data['vanity_url_code']
        discordServers.premium_tier = data['premium_tier']
        discordServers.premium_subscription_count = data['premium_subscription_count']
        discordServers.system_channel_flags = data['system_channel_flags']
        discordServers.preferred_locale = data['preferred_locale']
        discordServers.rules_channel_id = data['rules_channel_id']
        discordServers.public_updates_channel_id = data['public_updates_channel_id']
        discordServers.hub_type = data['hub_type']
        discordServers.premium_progress_bar_enabled = data['premium_progress_bar_enabled']
        # try catch to not block python
        try:
            # Save on mongodb
            discordServers.save()
        except Exception as e:
            print("Error to save discord message on mongo")
            print(e)
        return True

    # async import channel data method 
    def importChannelData(self, data) :
        print("-------- CHANNEL DATA ---------- CHANNEL DATA --------- CHANNEL DATA")
        if (not data['id']) :
            return False;
        try :
            discordChannels = DiscordChannels.objects.get(cid=data['id'])
        except :
            discordChannels = DiscordChannels()
        discordChannels = DiscordChannels()
        discordChannels.cid = data['id']
        discordChannels.name = data['name']
        discordChannels.last_message_id = data['last_message_id']
        discordChannels.type = data['type']
        discordChannels.position = data['position']
        discordChannels.flags = data['flags']
        discordChannels.parent_id = data['parent_id']
        discordChannels.topic = data['topic']
        discordChannels.guild_id = data['guild_id']
        discordChannels.last_pin_timestamp = data['last_pin_timestamp']
        discordChannels.rate_limit_per_user = data['rate_limit_per_user']

        # try catch to not block python
        try:
            # Save on mongodb
            discordChannels.save()
        except Exception as e:
            print("Error to save discord message on mongo")
            print(e)
        return True


    def test(self):
        messageModel = DiscordMessages()
        messageModel.title = "Eduardo Marinho"
        messageModel.author = "flow"
        messageModel.contributors = "contr"
        messageModel.url = "https://www.youtube.com/watch?v=Mg_7vNsnoQQ"
        messageModel.save()