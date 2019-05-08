import json

class ConversationHistory:
    def __init__(self):
        self.conversationContainer = []

    def readConversationHistory(self):
        print(self.conversationContainer)

    def getConversationHistory(self):
        return self.conversationContainer

    def addConversation(self, conversation):
        conversationContainerLength = len(self.conversationContainer) + 1
        conversation["id"] = conversationContainerLength
        self.conversationContainer.append(conversation)

    def clearConversationHistory(self):
        self.conversationContainer = []

    def getJSON(self):
        return json.dumps(self.conversationContainer)

    def printJSON(self):
        print(json.dumps(self.conversationContainer, indent=4))

if __name__ == '__main__':
    convHis = ConversationHistory()
    conversation = {
        "source": "192.168.0.1",
        "target": "192.168.0.2",
        "duration": "00:23:47:09",
        "status": "ended-properly",
        "messages-sent": 13,
        "messages-sent-by-source": 7,
        "messages-sent-by-target": 6,
        "breaks": 0,
        "breaks-taken-by-source": 0,
        "breaks-taken-by-target": 0
        }
    conversationSub = {
        "source": "192.168.0.4",
        "target": "192.168.0.1",
        "duration": "00:13:47:09",
        "status": "ended-properly",
        "messages-sent": 13,
        "messages-sent-by-source": 7,
        "messages-sent-by-target": 6,
        "breaks": 1,
        "breaks-taken-by-source": 1,
        "breaks-taken-by-target": 1
    }
    convHis.readConversationHistory()
    convHis.addConversation(conversation)
    convHis.addConversation(conversationSub)
    convHis.readConversationHistory()
    convHis.printJSON()