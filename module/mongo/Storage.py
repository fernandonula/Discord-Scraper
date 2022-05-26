from mongoengine import connect, disconnect
from . import DiscordMessageModels
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
    def importMessagesFromDiscord(self, messages, guildId) :
        # import messages using async way
        thr = threading.Thread(target=self._importMessagesFromDiscord, args=(messages, guildId), kwargs={})
        thr.start()

    # sync import messages method 
    def _importMessagesFromDiscord(self, messages, guildId) :
        # all messages loop
        for message in messages:
            content = message[0]["content"]
            # if havent content then go to next message
            if (content):
                author = message[0]["author"]
                messageModel = DiscordMessageModels()
                # ignore if havent author
                if (author) :
                    messageModel.authorName = author["username"]
                    messageModel.authorAvatarId = author["avatar"]
                    messageModel.authorId = author["id"]
                messageModel.content = content
                messageModel.channelId = message[0]["channel_id"]
                messageModel.guildId = guildId
                messageModel.type = message[0]["type"]
                messageModel.mId = message[0]["id"]
                # TODO: Convert UTC to local timezone                
                messageModel.mDate = datetime.strptime(message[0]["timestamp"].replace("+00:00", ""),'%Y-%m-%dT%H:%M:%S.%f')
                # try catch to not block python
                try:
                    # Save each message on mongodb
                    messageModel.save()
                    return True
                except:
                    print("Error to save discord message on mongo")
                    print(message)
        return False

    def test(self):
        messageModel = DiscordMessageModels()
        messageModel.title = "Eduardo Marinho"
        messageModel.author = "flow"
        messageModel.contributors = "contr"
        messageModel.url = "https://www.youtube.com/watch?v=Mg_7vNsnoQQ"
        messageModel.save()