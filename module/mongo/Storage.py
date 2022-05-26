from mongoengine import connect, disconnect
from . import MessageModel
import threading


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
                messageModel = MessageModel()
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
                # try catch to not block python
                try:
                    # Save each message on mongodb
                    messageModel.save()
                except:
                    print("Error to save discord message on mongo")
                    print(message)

    def test(self):
        messageModel = MessageModel()
        messageModel.title = "Eduardo Marinho"
        messageModel.author = "flow"
        messageModel.contributors = "contr"
        messageModel.url = "https://www.youtube.com/watch?v=Mg_7vNsnoQQ"
        messageModel.save()